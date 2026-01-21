# 📄 Model Contract — Sentiment Analysis

**Status:** LOCKED (Phase 1)

This document defines the **authoritative contract** between:

- ML Training / Model Owners
- Inference Runtime (MLflow / ML Service)
- Backend API
- Frontend Consumers

Once locked, **this contract MUST NOT change** without a version bump.

---

## 1️⃣ Purpose of This Contract

The goal of this contract is to ensure:

- Models can be upgraded (TF‑IDF → BERT → RAG)
- Infrastructure can evolve (MLflow → HF → Vertex)
- Backend & frontend remain **unchanged**

As long as this contract is honored, the system is considered **compatible**.

---

## 2️⃣ Input Contract (IMMUTABLE)

### API Input Schema

```json
{
  "text": "string"
}
```

### Input Rules

- `text` MUST be:
  - Non-empty
  - UTF‑8 encoded string
- Leading/trailing whitespace is ignored
- Empty or invalid input MUST result in a **400 error**

### Backend Responsibility

- Validate input
- Reject empty text

### ML Responsibility

- Assume input is already validated

---

## 3️⃣ Output Contract (IMMUTABLE)

### API Output Schema

```json
{
  "sentiment": "positive | negative | neutral",
  "confidence": 0,
  "source": "inference"
}
```

### Field Semantics

#### `sentiment`

- Final predicted class
- MUST be one of:
  - `positive`
  - `negative`
  - `neutral`

#### `confidence`

- Integer range: **0 – 100**
- Represents **relative model confidence**, NOT absolute probability

Examples:
- 92 → model strongly favors this class
- 55 → weak preference
- 0 → confidence unavailable (fallback)

⚠️ Confidence meaning may differ internally across models, but output range and type MUST remain stable.

#### `source`

- Indicates prediction origin
- Allowed values (examples, NOT exhaustive):
  - `inference`
  - `bert`
  - `rag`

The value indicates the **inference system**, not the registry or artifact store.

Used for debugging & observability only.

---

## 4️⃣ Inference Behavior Contract

### Prediction Interface (Conceptual)

```text
Prediction predict(text: str)
```

Rules:
- Single input → single output
- Batch inference is OPTIONAL, not required

### Model Expectations

The loaded model MUST:

- Accept `List[str]` as input
- Return either:
  - List of labels, OR
  - Object convertible to labels

---

## 5️⃣ Lifecycle & Loading Rules

### Model Loading

- Model is loaded **lazily** on first inference request
- Singleton instance per backend process

### Cold Start

- First request may incur load latency
- Subsequent requests reuse the loaded model

### Failure Handling

| Scenario | Behavior |
|-------|---------|
| Model URI invalid | Backend returns 500 |
| MLflow unreachable | Backend returns 500 |
| Prediction exception | Backend returns 500 |

Backend MUST NOT crash the process.

---

## 6️⃣ Model Registry & Artifact Integration Rules

### Allowed Model References

```text
models:/<RegisteredModelName>/<Stage>
```

Example:
```text
models:/TwitterSentimentModel/Production
```

### Stage Policy

- Inference layer reads from:
  - `Production` (default)

Promotion to Production is an ML-only decision.

Backend NEVER selects versions or artifact locations manually.

---

## 7️⃣ Backend Guarantees

Backend guarantees:

- Stable API schema
- Stable error behavior
- No dependency on model internals

Backend does NOT guarantee:

- Specific accuracy
- Specific latency
- Specific algorithm

---

## 8️⃣ ML Guarantees

ML guarantees:

- Output adheres to this contract
- Model registered correctly
- Backward compatibility

ML does NOT guarantee:

- Model size
- Training method
- Framework (sklearn / torch / tf)

---

## 9️⃣ Change Policy

| Change Type | Allowed? |
|-----------|--------|
| Model algorithm change | ✅ |
| Model framework change | ✅ |
| Registry backend change | ✅ |
| Input schema change | ❌ |
| Output schema change | ❌ |
| Confidence range change | ❌ |

Breaking changes require:

- New contract version
- Parallel API

---

## 🔒 Contract Status

**This contract is LOCKED for Phase 1.**

Any model or infra change MUST comply with this document.

---

**Owner:** System Architecture
**Version:** v1.0
**Last Updated:** Phase 1 Inference Lock

