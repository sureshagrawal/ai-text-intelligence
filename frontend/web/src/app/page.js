"use client";

import { useState } from "react";
import SentimentCard from "@/components/SentimentCard";
import { analyzeSentiment } from "@/services/sentimentService";

export default function Home() {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  async function handleAnalyze() {
    if (!text.trim()) return;

    setLoading(true);
    setResult(null);

    try {
      const data = await analyzeSentiment(text);
      setResult(data.sentiment);
    } catch (err) {
      setResult("Error");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-600 to-pink-600 px-4">
      <SentimentCard
        text={text}
        onTextChange={setText}
        result={result}
        onAnalyze={handleAnalyze}
        loading={loading}
      />
    </main>
  );
}
