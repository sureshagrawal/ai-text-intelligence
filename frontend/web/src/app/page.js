"use client";

import { useState } from "react";
import { analyzeSentiment } from "@/services/sentimentService";
import SentimentCard from "@/components/SentimentCard";

export default function HomePage() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    setError(null);
    setResult(null);

    if (!text.trim()) {
      setError("Type something first 😅");
      return;
    }

    try {
      setLoading(true);
      const data = await analyzeSentiment(text);
      setResult(data);
    } catch {
      setError("AI got confused 🤯");
    } finally {
      setLoading(false);
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
        <textarea
          rows={4}
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="I absolutely love this product..."
          className="w-full rounded-xl bg-white/10 border border-white/20 p-4 text-white placeholder-white/50 focus:outline-none focus:ring-2 focus:ring-purple-500 backdrop-blur"
        />

        <button
          onClick={handleAnalyze}
          disabled={loading}
          className="mt-4 w-full rounded-xl bg-gradient-to-r from-pink-500 to-purple-600 py-3 font-bold tracking-wide hover:scale-[1.02] transition-transform disabled:opacity-60"
        >
          {loading ? "Analyzing vibes..." : "Analyze Sentiment 🚀"}
        </button>

        {error && (
          <p className="mt-3 text-red-400 text-sm">
            {error}
          </p>
        )}

        <SentimentCard result={result} />
      </div>
    </main>
  );
}
