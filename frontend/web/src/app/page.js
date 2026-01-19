"use client";

import { useState } from "react";
import SentimentCard from "@/components/SentimentCard";

export default function Home() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  function handleAnalyze() {
    // backend integration will come later
    setResult("Positive");
  }

  return (
    <main className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-600 to-pink-600">
      <SentimentCard
        text={text}
        onTextChange={setText}
        result={result}
        onAnalyze={handleAnalyze}
      />
    </main>
  );
}
