"use client";

import React, { createContext, useContext, useEffect, useState } from "react";
import { UserProfile, Section, FeatureKey, EnrollmentRecord } from "@/types";
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

export interface EntitlementCheckStatus {
  granted: boolean;
  reason?: "not_enrolled" | "expired" | "revoked" | "preview" | "admin" | "no_active_package";
  preview?: boolean;
  requiredPackageName?: string;
  requiredPackageId?: string;
  expiresAt?: string | null;
}

interface AuthContextType {
  user: UserProfile;
  isAuthenticated: boolean;
  isGuest: boolean;
  loading: boolean;
  allDemoUsers: UserProfile[];
  userEnrollments: EnrollmentRecord[];
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
  checkEntitlement: (target: { courseId?: string; moduleId?: string; lessonId?: string; feature?: FeatureKey }) => EntitlementCheckStatus;
  requestEnrollment: (packageId: string, type?: "register" | "renew", note?: string) => Promise<{ success: boolean; message?: string; error?: string }>;
  refreshEnrollments: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [users, setUsers] = useState<UserProfile[]>(SEED_USERS);
  const [currentUser, setCurrentUser] = useState<UserProfile>(GUEST_USER);
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [userEnrollments, setUserEnrollments] = useState<EnrollmentRecord[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  const fetchUserEnrollments = async () => {
    try {
      const res = await fetch("/api/enrollments", { cache: "no-store" });
      if (res.ok) {
        const data = await res.json();
        if (data.success && data.enrollments) {
          setUserEnrollments(Array.isArray(data.enrollments) ? data.enrollments : []);
        }
      }
    } catch (err) {
      console.warn("Failed to fetch user enrollments:", err);
    }
  };

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
            fetchUserEnrollments();
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
                  fetchUserEnrollments();
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
      fetchUserEnrollments();
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
    setUserEnrollments([]);
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
    if (currentUser.tier === "free" && userEnrollments.length === 0) return false;
    const now = new Date().toISOString();
    const hasActiveEnr = userEnrollments.some(e => e.status === "active" && (!e.expiresAt || e.expiresAt > now));
    if (hasActiveEnr) return true;
    if (currentUser.tier && currentUser.tier !== "free") {
      if (!currentUser.tierExpiresAt || currentUser.tierExpiresAt > now) {
        return true;
      }
    }
    return false;
  };

  const canAccessSection = (section: Section) => {
    if (section.isFree) return true;
    return canAccessPaidContent();
  };

  const checkEntitlement = (target: {
    courseId?: string;
    moduleId?: string;
    lessonId?: string;
    feature?: FeatureKey;
  }): EntitlementCheckStatus => {
    // 1. Check preview lessons
    if (target.lessonId === "mod1-les1" || target.lessonId === "mod6-les1") {
      return { granted: true, reason: "preview", preview: true };
    }

    // 2. Unauthenticated
    if (!isAuthenticated || currentUser.id === "guest") {
      return {
        granted: false,
        reason: "not_enrolled",
        requiredPackageName: "Gói Học Thử hoặc Nền Tảng Khai Vấn",
        requiredPackageId: "pkg-trial"
      };
    }

    // 3. Super admin, editor, billing
    if (isSuperAdmin || isEditor || isBilling) {
      return { granted: true, reason: "admin" };
    }

    const now = new Date().toISOString();
    const active = userEnrollments.filter(e => e.status === "active" && (!e.expiresAt || e.expiresAt > now));
    const expired = userEnrollments.filter(e => e.status === "expired" || (e.expiresAt && e.expiresAt < now));

    // Support legacy tier if set
    if (currentUser.tier && currentUser.tier !== "free") {
      if (!currentUser.tierExpiresAt || currentUser.tierExpiresAt > now) {
        return { granted: true };
      }
    }

    if (active.length === 0) {
      if (expired.length > 0) {
        const lastExp = expired[0];
        return {
          granted: false,
          reason: "expired",
          requiredPackageName: lastExp.packageName,
          requiredPackageId: lastExp.packageId,
          expiresAt: lastExp.expiresAt
        };
      }
      return {
        granted: false,
        reason: "not_enrolled",
        requiredPackageName: target.feature === "mock_exam_sjt" ? "Gói Luyện Thi ICF Credentialing" : "Gói Nền Tảng Khai Vấn",
        requiredPackageId: target.feature === "mock_exam_sjt" ? "pkg-exam-prep" : "pkg-foundation"
      };
    }

    // If student has active enrollment, check permission
    const hasAll = active.some(e => e.packageId === "pkg-pcc-master");
    if (hasAll) {
      return { granted: true, expiresAt: active[0].expiresAt };
    }

    if (target.feature === "mock_exam_sjt") {
      const hasExam = active.some(e => e.packageId === "pkg-exam-prep" || e.packageId === "pkg-pcc-master");
      if (hasExam) return { granted: true };
      return {
        granted: false,
        reason: "not_enrolled",
        requiredPackageName: "Gói Luyện Thi ICF Credentialing",
        requiredPackageId: "pkg-exam-prep"
      };
    }

    // Default for active package holders
    return { granted: true, expiresAt: active[0].expiresAt };
  };

  const requestEnrollment = async (
    packageId: string,
    type: "register" | "renew" = "register",
    note: string = ""
  ) => {
    try {
      const res = await fetch("/api/enrollments/request", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ packageId, type, userNote: note })
      });
      const data = await res.json();
      if (data.success) {
        return { success: true, message: data.message };
      }
      return { success: false, error: data.error || "Gửi yêu cầu thất bại" };
    } catch (err: any) {
      return { success: false, error: err.message || "Lỗi kết nối máy chủ" };
    }
  };

  return (
    <AuthContext.Provider
      value={{
        user: currentUser,
        isAuthenticated,
        isGuest: !isAuthenticated,
        loading,
        allDemoUsers: users,
        userEnrollments,
        login,
        logout,
        switchUser,
        updateCurrentUser,
        isSuperAdmin,
        isEditor,
        isBilling,
        isStudent,
        canAccessSection,
        canAccessPaidContent,
        checkEntitlement,
        requestEnrollment,
        refreshEnrollments: fetchUserEnrollments
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
