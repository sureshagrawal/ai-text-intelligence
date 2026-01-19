"use client";

export default function SentimentCard({
  text,
  onTextChange,
  result,
  onAnalyze,
}) {
  return (
    <div className="w-full max-w-lg bg-white/90 backdrop-blur-xl rounded-3xl shadow-2xl p-8">
      <h1 className="text-3xl font-extrabold text-center">
        Sentiment Analyzer
      </h1>

      <p className="text-center text-sm text-gray-500 mt-1">
        Feel the emotion behind words ✨
      </p>

      <div className="mt-8">
        <label className="block text-sm font-semibold mb-2">
          Your text
        </label>

        <textarea
          value={text}
          onChange={(e) => onTextChange(e.target.value)}
          placeholder="Example: I absolutely loved the experience!"
          className="w-full h-32 p-4 rounded-xl border resize-none"
        />
      </div>

      <button
        onClick={onAnalyze}
        className="w-full mt-6 py-3 rounded-xl text-white font-semibold
                   bg-gradient-to-r from-purple-600 to-pink-600"
      >
        Analyze Sentiment 🚀
      </button>

      <div className="mt-6 text-center">
        <div className="inline-block px-6 py-2 rounded-full font-bold">
          {result || "—"}
        </div>
      </div>
    </div>
  );
}
