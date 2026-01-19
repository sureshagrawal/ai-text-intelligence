"use client";

export default function SentimentCard({
  text,
  onTextChange,
  result,
  onAnalyze,
  loading,
}) {
  return (
    <div className="w-full max-w-lg bg-white/90 backdrop-blur-xl rounded-3xl shadow-2xl p-8">
      <h1 className="text-3xl font-extrabold text-center mb-2">
        Sentiment Analyzer
      </h1>

      <textarea
        value={text}
        onChange={(e) => onTextChange(e.target.value)}
        placeholder="Type something..."
        className="w-full h-32 p-4 rounded-xl border focus:outline-none"
      />

      <button
        onClick={onAnalyze}
        disabled={loading}
        className="w-full mt-6 py-3 rounded-xl text-white font-semibold
                   bg-gradient-to-r from-purple-600 to-pink-600
                   disabled:opacity-60"
      >
        {loading ? "Analyzing..." : "Analyze Sentiment"}
      </button>

      <div className="mt-6 text-center">
        <div className="inline-flex items-center gap-2 px-6 py-3 rounded-full font-bold">
          {result || "—"}
        </div>
      </div>
    </div>
  );
}
