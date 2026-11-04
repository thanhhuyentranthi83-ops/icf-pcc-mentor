"use client";

import React, { createContext, useContext, useEffect, useState } from "react";
import { playMindfulnessBell } from "@/lib/audio";

interface SoundContextType {
  soundEnabled: boolean;
  toggleSound: () => void;
  ringBell: () => void;
}

const SoundContext = createContext<SoundContextType | undefined>(undefined);

export function SoundProvider({ children }: { children: React.ReactNode }) {
  const [soundEnabled, setSoundEnabled] = useState(true);

  useEffect(() => {
    try {
      const saved = localStorage.getItem("icf_pcc_sound");
      if (saved !== null) {
        setSoundEnabled(saved === "true");
      }
    } catch {
      // ignore
    }
  }, []);

  const toggleSound = () => {
    const next = !soundEnabled;
    setSoundEnabled(next);
    try {
      localStorage.setItem("icf_pcc_sound", String(next));
    } catch {
      // ignore
    }
    if (next) {
      playMindfulnessBell(0.3);
    }
  };

  const ringBell = () => {
    if (soundEnabled) {
      playMindfulnessBell(0.35);
    }
  };

  return (
    <SoundContext.Provider value={{ soundEnabled, toggleSound, ringBell }}>
      {children}
    </SoundContext.Provider>
  );
}

export function useSound() {
  const ctx = useContext(SoundContext);
  if (!ctx) {
    throw new Error("useSound must be used within SoundProvider");
  }
  return ctx;
}
