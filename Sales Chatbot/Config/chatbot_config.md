# KDK Sales Chatbot — Configuration Reference

---

## AI Model Settings (Recommended)

| Setting | Recommended Value | Notes |
|---|---|---|
| Model | Claude Sonnet / GPT-4o | High reasoning for complex sales conversations |
| Temperature | 0.4 – 0.6 | Confident and natural, not robotic |
| Max tokens (response) | 300 – 500 | Keep chat responses concise |
| Context window | 32K+ tokens | Needed to hold KB + conversation history |
| Top-p | 0.9 | Standard |
| Frequency penalty | 0.3 | Avoid repetitive phrasing |

---

## Knowledge Base Loading Strategy

### Option A — Full Context (Simpler)
Load the full `KDK-Sales-Agent-KnowledgeBase.md` as the system context.
- Pros: Simple, fast to implement
- Cons: Uses large context window; may hit token limits with long conversations
- Best for: Claude API, GPT-4o API with 128K context

### Option B — RAG (Retrieval-Augmented Generation)
Chunk and embed all 287 articles from `kb_all_articles.json`, then retrieve relevant chunks based on user query.
- Pros: Scalable, handles large KB efficiently
- Cons: Requires embedding infrastructure (Pinecone, Weaviate, pgvector, etc.)
- Best for: Production deployments with high query volume
- Recommended chunk size: 500–800 tokens per article
- Embedding model: text-embedding-3-small (OpenAI) or Cohere embed

### Option C — Hybrid (Best)
- System prompt: `system_prompt.md` (always in context)
- Static knowledge: `KDK-Sales-Agent-KnowledgeBase.md` (always in context — pitches, comparisons, objections)
- Dynamic retrieval: Individual KB articles from `kb_all_articles.json` (retrieved only when user asks how-to questions)

---

## Deployment Platforms (Options)

| Platform | Best For | Notes |
|---|---|---|
| **Website widget** | Lead generation from website visitors | Embed as chat bubble |
| **WhatsApp Business API** | Existing customers + new leads via WhatsApp | Requires WhatsApp Business API approval |
| **Dialogflow CX** | Multi-channel (web + WhatsApp + voice) | Good for structured flows |
| **Claude API (Anthropic)** | Custom implementation | Most flexible, best reasoning |
| **OpenAI Assistants API** | File-based knowledge base | Supports file uploads natively |
| **Botpress / Voiceflow** | No-code / low-code | Faster to deploy, less flexible |

---

## Languages

| Language | Priority | Notes |
|---|---|---|
| English | Primary | All KB content is in English |
| Hindi | Secondary | Agent should respond in Hindi if user writes in Hindi |
| Hinglish | Supported | Common in Indian B2B conversations |

---

## Escalation Rules

Trigger human handoff when:
1. User explicitly asks for a human / agent / callback
2. User is ready to purchase (says "buy", "pricing", "quote", "demo")
3. Bot fails to answer 2 consecutive questions confidently
4. User expresses frustration (words like "not helpful", "useless", "wrong")
5. Conversation exceeds 15 turns without resolution

Handoff options:
- Live chat (if available during business hours)
- Lead capture form (name + mobile + email + requirement)
- Scheduled callback

---

## Tone Guidelines

| Situation | Tone |
|---|---|
| Greeting / Opening | Warm, welcoming |
| Product pitch | Confident, benefit-focused |
| Competitor comparison | Factual, respectful (never dismissive) |
| Objection handling | Empathetic, reassuring, solution-oriented |
| Closing / Demo ask | Enthusiastic but not pushy |
| Technical how-to | Clear, step-by-step, concise |

---

## Do Not Say List

- Do not say specific prices (route to sales team)
- Do not say "I don't know" — say "Let me connect you with our team for that"
- Do not say negative things about competitors by name aggressively
- Do not make promises about features not in the knowledge base
- Do not give tax advice or legal opinions
- Do not say "As an AI..." — maintain the persona of KDK Sales Assistant

---

## Analytics to Track

| Metric | Purpose |
|---|---|
| Most asked product (GST / TDS / ITR) | Focus product training |
| Most common segment (DIY / DIFM) | Refine pitch content |
| Top competitor mentions | Update comparison data |
| Top objections raised | Improve objection responses |
| Conversion rate (chat → demo request) | Measure chatbot effectiveness |
| Escalation rate | Identify knowledge gaps |
| Drop-off point in conversation | Fix broken flows |
