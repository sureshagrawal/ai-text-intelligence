const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL;

export async function analyzeSentiment(text) {
  if (!text || !text.trim()) {
    throw new Error("Text is required");
  }

  const response = await fetch(`${API_BASE_URL}/sentiment/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text }),
  });

  if (!response.ok) {
    const err = await response.text();
    throw new Error(err || "Failed to analyze sentiment");
  }

  return response.json();
}
