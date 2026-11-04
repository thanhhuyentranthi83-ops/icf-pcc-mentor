"use client";

import React, { createContext, useContext, useEffect, useState } from "react";
import { UserProfile, Section } from "@/types";
import { getUsers, saveUser } from "@/lib/db";
import { SEED_USERS } from "@/lib/seedData";

interface AuthContextType {
  user: UserProfile;
  allDemoUsers: UserProfile[];
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
  // Default to 1-Month student for a full student experience demo, or load from storage
  const [currentUserId, setCurrentUserId] = useState<string>("usr-1m");

  useEffect(() => {
    try {
      const loaded = getUsers();
      if (loaded && loaded.length > 0) {
        setUsers(loaded);
      }
      const savedId = localStorage.getItem("icf_pcc_current_user_id");
      if (savedId) {
        setCurrentUserId(savedId);
      }
    } catch {
      // ignore
    }
  }, []);

  const currentUser = users.find((u) => u.id === currentUserId) || users[0] || SEED_USERS[0];

  const switchUser = (userId: string) => {
    setCurrentUserId(userId);
    try {
      localStorage.setItem("icf_pcc_current_user_id", userId);
    } catch {
      // ignore
    }
  };

  const updateCurrentUser = (partial: Partial<UserProfile>) => {
    const updated = { ...currentUser, ...partial };
    saveUser(updated);
    setUsers((prev) => prev.map((u) => (u.id === updated.id ? updated : u)));
  };

  const isSuperAdmin = currentUser.role === "super_admin";
  const isEditor = currentUser.role === "editor" || isSuperAdmin;
  const isBilling = currentUser.role === "billing" || isSuperAdmin;
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
        allDemoUsers: users,
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
