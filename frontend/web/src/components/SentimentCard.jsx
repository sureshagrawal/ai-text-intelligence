export default function SentimentCard({ result }) {
  if (!result) return null;

  const { sentiment, confidence, source } = result;

  // ✅ Normalize backend sentiment (positive → Positive)
  const normalizedSentiment =
    sentiment.charAt(0).toUpperCase() + sentiment.slice(1);

  const configMap = {
    Positive: {
      gradient: "from-green-400 to-emerald-600",
      glow: "shadow-green-400/50",
      emoji: "😍",
      label: "Feeling Great!",
    },
    Neutral: {
      gradient: "from-yellow-300 to-orange-400",
      glow: "shadow-yellow-300/50",
      emoji: "😐",
      label: "Meh, it’s okay",
    },
    Negative: {
      gradient: "from-red-400 to-rose-600",
      glow: "shadow-red-400/50",
      emoji: "😡",
      label: "Not Good!",
    },
  };

  // ✅ Use normalized sentiment for UI mapping
  const cfg = configMap[normalizedSentiment] || configMap.Neutral;

  return (
    <div className="mt-8 w-full max-w-xl rounded-2xl border border-white/20 bg-white/10 backdrop-blur-xl p-6 shadow-xl transition-all">
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <span className="text-4xl animate-bounce">{cfg.emoji}</span>
          <div>
            <div className="text-xl font-bold text-white">
              {normalizedSentiment}
            </div>
            <div className="text-sm text-white/70">
              {cfg.label}
            </div>
          </div>
        </div>


      </div>

      {/* Confidence Bar */}
      <div className="relative h-5 w-full rounded-full bg-white/20 overflow-hidden">
        <div
          className={`absolute left-0 top-0 h-5 rounded-full bg-gradient-to-r ${cfg.gradient} ${cfg.glow} transition-all duration-700`}
          style={{ width: `${confidence}%` }}
        />
      </div>

      <div className="mt-3 text-right text-sm text-white">
        🔥 Confidence: <span className="font-bold">{confidence}%</span>
      </div>
    </div>
  );
}
