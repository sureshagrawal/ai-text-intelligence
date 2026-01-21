"use client";

import { useState, useRef, useEffect } from "react";
import { analyzeSentiment } from "@/services/sentimentService";
import SentimentCard from "@/components/SentimentCard";

export default function HomePage() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [pulse, setPulse] = useState(false);

  const textareaRef = useRef(null);

  // ✅ Auto-focus on page load
  useEffect(() => {
    textareaRef.current?.focus();
  }, []);

  const forceFocus = () => {
    requestAnimationFrame(() => {
      textareaRef.current?.focus();
    });
  };

  const handleAnalyze = async () => {
    setError(null);
    setResult(null);

    if (!text.trim()) {
      setError("Type something first 😅");
      forceFocus();
      return;
    }

    try {
      setLoading(true);
      const data = await analyzeSentiment(text);
      setResult(data);

      // ✅ Clear input + success pulse
      setText("");
      setPulse(true);
      setTimeout(() => setPulse(false), 300);

      forceFocus();
    } catch {
      setError("AI got confused 🤯");
      forceFocus();
    } finally {
      setLoading(false);
    }
  };

  // ✅ Enter = Analyze | Shift+Enter = New line
  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      if (!loading) handleAnalyze();
    }
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-indigo-900 via-purple-900 to-black flex flex-col items-center px-4 py-14 text-white">
      <h1 className="text-4xl font-extrabold tracking-tight mb-2">
        AI Text Sentiment
      </h1>
      <p className="text-white/70 mb-8">
        Type something and feel the AI vibes ✨
      </p>

      <div className="w-full max-w-xl">
        {/* Textarea */}
        <div
          className={`rounded-xl transition-all ${
            pulse ? "ring-2 ring-pink-400/60" : ""
          }`}
        >
          <textarea
            ref={textareaRef}
            rows={4}
            value={text}
            onChange={(e) => setText(e.target.value)}
            onKeyDown={handleKeyDown}
            readOnly={loading} // ✅ NOT disabled (important)
            placeholder="Type here… press Enter to analyze"
            className="w-full rounded-xl bg-white/10 border border-white/20 p-4 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-purple-500 backdrop-blur transition-all"
          />
        </div>

        {/* Hint */}
        <div className="mt-2 text-xs text-white/50">
          ⏎ Enter to analyze • ⇧ Shift + Enter for new line
        </div>

        {/* Button */}
        <button
          onClick={handleAnalyze}
          disabled={loading}
          className="mt-4 w-full rounded-xl bg-gradient-to-r from-pink-500 to-purple-600 py-3 font-bold tracking-wide hover:scale-[1.03] transition-transform disabled:opacity-60 disabled:hover:scale-100"
        >
          {loading ? "Analyzing vibes..." : "Analyze Sentiment 🚀"}
        </button>

        {error && (
          <p className="mt-3 text-red-400 text-sm animate-pulse">
            {error}
          </p>
        )}

        {/* Result */}
        <div className="animate-fade-in">
          <SentimentCard result={result} />
        </div>
      </div>
    </main>
  );
}
