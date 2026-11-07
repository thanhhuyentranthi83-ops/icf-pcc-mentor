"use client";

import React, { createContext, useContext, useEffect, useState } from "react";
import { UserProfile, Section } from "@/types";
import { getUsers, saveUser } from "@/lib/db";
import { SEED_USERS } from "@/lib/seedData";

export const GUEST_USER: UserProfile = {
  id: "guest",
  email: "",
  fullName: "Học Viên Khách",
  role: "student",
  tier: "free",
  tierExpiresAt: null,
  streakCount: 0,
  lastActiveDate: new Date().toISOString().split("T")[0],
  selectedStickerPack: "sprout_seed",
  minimalMode: false,
  soundEnabled: true
};

interface AuthContextType {
  user: UserProfile;
  isAuthenticated: boolean;
  isGuest: boolean;
  loading: boolean;
  allDemoUsers: UserProfile[];
  login: (email: string, fullName?: string) => Promise<{ success: boolean; user?: UserProfile; error?: string }>;
  logout: () => Promise<void>;
  switchUser: (userId: string) => void;
  updateCurrentUser: (partial: Partial<UserProfile>) => void;
  isSuperAdmin: boolean;
  isEditor: boolean;
  isBilling: boolean;
  isStudent: boolean;
  canAccessSection: (section: Section) => boolean;
  canAccessPaidContent: () => boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [users, setUsers] = useState<UserProfile[]>(SEED_USERS);
  const [currentUser, setCurrentUser] = useState<UserProfile>(GUEST_USER);
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(true);

  // Check server session on initial load
  useEffect(() => {
    let mounted = true;

    async function checkSession() {
      try {
        const res = await fetch("/api/auth/me", { cache: "no-store" });
        if (res.ok) {
          const data = await res.json();
          if (data.authenticated && data.user && mounted) {
            setCurrentUser(data.user);
            setIsAuthenticated(true);
            setLoading(false);
            return;
          }
        }
      } catch (err) {
        console.warn("Session check error, fallback to local:", err);
      }

      // Check legacy local storage fallback
      try {
        const loaded = getUsers();
        if (loaded && loaded.length > 0 && mounted) {
          setUsers(loaded);
        }
        const savedId = localStorage.getItem("icf_pcc_current_user_id");
        if (savedId && savedId !== "guest" && mounted) {
          const matched = loaded.find((u: UserProfile) => u.id === savedId) || SEED_USERS.find((u: UserProfile) => u.id === savedId);
          if (matched) {
            // Auto login to server with this email
            try {
              const loginRes = await fetch("/api/auth/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email: matched.email, fullName: matched.fullName })
              });
              if (loginRes.ok) {
                const lData = await loginRes.json();
                if (lData.user && mounted) {
                  setCurrentUser(lData.user);
                  setIsAuthenticated(true);
                  setLoading(false);
                  return;
                }
              }
            } catch {
              // fallback below
            }
            setCurrentUser(matched);
            setIsAuthenticated(true);
          }
        }
      } catch {
        // ignore
      }

      if (mounted) {
        setLoading(false);
      }
    }

    checkSession();

    return () => {
      mounted = false;
    };
  }, []);

  const login = async (email: string, fullName?: string) => {
    try {
      const res = await fetch("/api/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: email.trim().toLowerCase(), fullName })
      });

      const data = await res.json();
      if (!res.ok || !data.success) {
        return { success: false, error: data.error || "Đăng nhập thất bại" };
      }

      const loggedUser: UserProfile = data.user;
      setCurrentUser(loggedUser);
      setIsAuthenticated(true);
      try {
        localStorage.setItem("icf_pcc_current_user_id", loggedUser.id);
      } catch {
        // ignore
      }
      return { success: true, user: loggedUser };
    } catch (err: any) {
      console.error("Login call error:", err);
      return { success: false, error: err.message || "Lỗi mạng" };
    }
  };

  const logout = async () => {
    try {
      await fetch("/api/auth/logout", { method: "POST" });
    } catch {
      // ignore
    }
    setCurrentUser(GUEST_USER);
    setIsAuthenticated(false);
    try {
      localStorage.removeItem("icf_pcc_current_user_id");
    } catch {
      // ignore
    }
  };

  const switchUser = async (userId: string) => {
    const target = users.find((u) => u.id === userId) || SEED_USERS.find((u: UserProfile) => u.id === userId);
    if (target) {
      await login(target.email, target.fullName);
    }
  };

  const updateCurrentUser = (partial: Partial<UserProfile>) => {
    const updated = { ...currentUser, ...partial };
    saveUser(updated);
    setCurrentUser(updated);
    setUsers((prev) => prev.map((u) => (u.id === updated.id ? updated : u)));
  };

  const isSuperAdmin = isAuthenticated && currentUser.role === "super_admin";
  const isEditor = isAuthenticated && (currentUser.role === "editor" || isSuperAdmin);
  const isBilling = isAuthenticated && (currentUser.role === "billing" || isSuperAdmin);
  const isStudent = currentUser.role === "student";

  const canAccessPaidContent = () => {
    if (isSuperAdmin || isEditor || isBilling) return true;
    if (currentUser.tier === "free") return false;
    if (currentUser.tierExpiresAt) {
      return new Date(currentUser.tierExpiresAt) > new Date();
    }
    return true;
  };

  const canAccessSection = (section: Section) => {
    if (section.isFree) return true;
    return canAccessPaidContent();
  };

  return (
    <AuthContext.Provider
      value={{
        user: currentUser,
        isAuthenticated,
        isGuest: !isAuthenticated,
        loading,
        allDemoUsers: users,
        login,
        logout,
        switchUser,
        updateCurrentUser,
        isSuperAdmin,
        isEditor,
        isBilling,
        isStudent,
        canAccessSection,
        canAccessPaidContent
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used within AuthProvider");
  }
  return ctx;
}
