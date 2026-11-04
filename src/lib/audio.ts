/**
 * Web Audio API - Realistic Tibetan Singing Bowl / Mindfulness Bell Synthesizer
 * Plays a resonant, calming chime with gentle acoustic harmonics
 */

let audioCtx: AudioContext | null = null;

function getAudioContext(): AudioContext | null {
  if (typeof window === "undefined") return null;
  if (!audioCtx) {
    const AudioContextClass = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext;
    if (AudioContextClass) {
      audioCtx = new AudioContextClass();
    }
  }
  if (audioCtx && audioCtx.state === "suspended") {
    audioCtx.resume();
  }
  return audioCtx;
}

export function playMindfulnessBell(volume = 0.4) {
  try {
    const ctx = getAudioContext();
    if (!ctx) return;

    const now = ctx.currentTime;
    const masterGain = ctx.createGain();
    masterGain.gain.setValueAtTime(volume, now);
    masterGain.connect(ctx.destination);

    // Fundamental frequencies of a serene Tibetan bowl
    const frequencies = [340, 510, 850, 1190];
    const gains = [0.6, 0.25, 0.1, 0.05];
    const decayTimes = [6.0, 4.5, 3.0, 2.0];

    frequencies.forEach((freq, i) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();

      osc.type = "sine";
      // Slight pitch wobble for organic bowl resonance
      osc.frequency.setValueAtTime(freq, now);
      osc.frequency.exponentialRampToValueAtTime(freq * 0.998, now + decayTimes[i]);

      gain.gain.setValueAtTime(0.001, now);
      // Soft gentle strike attack
      gain.gain.exponentialRampToValueAtTime(gains[i], now + 0.04);
      // Long soothing decay
      gain.gain.exponentialRampToValueAtTime(0.0001, now + decayTimes[i]);

      osc.connect(gain);
      gain.connect(masterGain);

      osc.start(now);
      osc.stop(now + decayTimes[i]);
    });
  } catch (err) {
    console.warn("Audio playback not permitted or supported yet:", err);
  }
}
