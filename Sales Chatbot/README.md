# KDK Sales Chatbot — Project Workspace

## Purpose
An AI-powered sales chatbot for KDK Software that can:
- Pitch Express GST, Express TDS, and Express ITR to prospects
- Handle queries from both DIY (Enterprise) and DIFM (CA) segments
- Compare KDK products against competitors intelligently
- Qualify leads using the built-in questionnaire
- Handle objections and guide prospects toward a demo or purchase

---

## Folder Structure

```
Sales Chatbot/
│
├── Knowledge Base Files/         ← Source documents fed to the AI
│   ├── KDK-Sales-Agent-KnowledgeBase.md   ← Primary: pitches, comparisons, objections, questionnaire
│   ├── Express-GST-KnowledgeBase.md       ← 96 support articles for GST
│   ├── Express-TDS-KnowledgeBase.md       ← 82 support articles for TDS
│   ├── Express-ITR-KnowledgeBase.md       ← 109 support articles for ITR
│   └── kb_all_articles.json               ← Combined JSON (287 articles) for AI training
│
├── Prompts/                      ← System prompts for the chatbot
│   └── system_prompt.md          ← Main system prompt defining the bot's persona and behavior
│
├── Conversation Flows/           ← Scripted flows for key scenarios
│   └── conversation_flows.md     ← Discovery, pitch, objection, closing flows
│
├── Config/                       ← Configuration and integration settings
│   └── chatbot_config.md         ← API settings, model config, tone, escalation rules
│
└── Scripts/                      ← Helper scripts
    └── (development scripts go here)
```

---

## Knowledge Base Summary

| File | Content | Size |
|---|---|---|
| KDK-Sales-Agent-KnowledgeBase.md | Pitches, USPs, competitor tables, questionnaire, objection handling | 40 KB |
| Express-GST-KnowledgeBase.md | 96 GST how-to articles | 268 KB |
| Express-TDS-KnowledgeBase.md | 82 TDS how-to articles | 193 KB |
| Express-ITR-KnowledgeBase.md | 109 ITR how-to articles | 221 KB |
| kb_all_articles.json | All 287 articles in JSON format | 822 KB |

---

## Target Segments

| Segment | Who | Key Need |
|---|---|---|
| **DIY** | Enterprises / Businesses | Automate compliance, reduce manual work |
| **DIFM** | CAs / Tax Professionals | Manage more clients, increase productivity |
| **Bundle** | Large firms / enterprises | All three products on one platform |

---

## Products Covered

| Product | What it does |
|---|---|
| **Express GST** | GST return filing, reconciliation, e-invoice, e-way bill |
| **Express TDS** | TDS return filing (24Q/26Q/27Q/27EQ), TRACES integration |
| **Express ITR** | Income tax return filing (ITR-1 to ITR-7), tax audit |

---

## Next Steps
1. Finalize the system prompt (`Prompts/system_prompt.md`)
2. Define conversation flows (`Conversation Flows/conversation_flows.md`)
3. Choose AI platform / API (Claude, OpenAI, Dialogflow, etc.)
4. Build and test the chatbot
5. Integrate with website / WhatsApp / CRM
