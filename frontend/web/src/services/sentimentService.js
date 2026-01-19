const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL;

export async function analyzeSentiment(text) {
  const res = await fetch(`${API_BASE_URL}/sentiment`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });

  if (!res.ok) {
    throw new Error("Sentiment API failed");
  }

  return res.json();
}
