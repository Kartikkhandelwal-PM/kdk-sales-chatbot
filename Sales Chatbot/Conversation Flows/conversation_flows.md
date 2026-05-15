# KDK Sales Chatbot — Conversation Flows

---

## FLOW 1 — New Visitor (Cold Start)

```
BOT:  Hi! I'm KDK's Sales Assistant. I can help you explore Express GST, 
      Express TDS, and Express ITR — India's leading cloud-based tax compliance 
      software. 

      Are you:
      A) A CA / Tax Professional managing client compliance?
      B) A Business / Enterprise managing your own compliance?
      C) Just exploring what KDK offers?

USER: [Selects A / B / C]

→ If A (CA/DIFM)  → Go to FLOW 2A
→ If B (Enterprise/DIY) → Go to FLOW 2B
→ If C (Exploring) → Go to FLOW 3
```

---

## FLOW 2A — DIFM (CA / Tax Professional)

```
BOT:  Great! CAs love Express because it lets them manage all clients from 
      one dashboard. Which compliance are you looking to handle?
      
      A) GST only
      B) TDS only
      C) ITR only
      D) Two or more / Full suite

USER: [Selects product]

BOT:  How many clients do you currently manage for [product]?
      A) Less than 25
      B) 25 – 100
      C) More than 100

USER: [Answers]

BOT:  [Pitch relevant DIFM features based on product and client count]
      
      For example (GST + 100+ clients):
      "With 100+ GST clients, the biggest time-saver is our auto 2A/2B email — 
      all clients get their data on the 15th automatically. Plus you can see 
      every client's notices on one screen. Your team can handle 40% more 
      clients without adding staff. Would you like a quick demo?"

→ If interested → Go to FLOW 6 (Demo / Handoff)
→ If objection → Go to FLOW 5 (Objection Handling)
→ If competitor mentioned → Go to FLOW 4 (Competitor Comparison)
```

---

## FLOW 2B — DIY (Enterprise / Business)

```
BOT:  Perfect! For businesses managing their own compliance, Express makes 
      everything automatic — data sync, reconciliation, notices, reports.

      Which compliance are you looking to manage?
      A) GST
      B) TDS
      C) ITR
      D) All three

USER: [Selects]

BOT:  Are you currently using any software for this?
      A) Yes — [which one?]
      B) No — doing it manually
      C) Using the government portal directly

USER: [Answers]

BOT:  [Pitch relevant DIY features]
      
      For example (GST, currently manual):
      "Right now you're probably downloading data manually, reconciling in 
      Excel, and checking notices on the portal one by one. Express GST 
      auto-fetches your data from day one, reconciles 2A/2B in 4 clicks, 
      and shows all your notices on one screen. Want to see it in action?"

→ If yes → Go to FLOW 6 (Demo / Handoff)
→ If objection → Go to FLOW 5 (Objection Handling)
→ If competitor mentioned → Go to FLOW 4 (Competitor Comparison)
```

---

## FLOW 3 — General Exploration

```
BOT:  No problem! Here's a quick overview of what we offer:

      📌 Express GST — File GSTR returns, reconcile 2A/2B, manage 
         e-invoices and e-way bills. Cloud-based, works for both 
         businesses and CA firms.

      📌 Express TDS — File 24Q, 26Q, 27Q, 27EQ returns. Java-free FVU, 
         auto challan import, bulk PAN verification, TDS certificates.

      📌 Express ITR — File ITR-1 to ITR-7. Import Form 16 and AIS in 
         one click, tax audit forms, capital gains from broker templates.

      Which product interests you the most, or do you want to know 
      about the full suite?

→ Route to FLOW 2A or 2B based on their response
```

---

## FLOW 4 — Competitor Comparison

```
USER: "We use ClearTax / Winman / GEN TDS / other"

BOT:  That's a good choice — [Competitor] has some solid features. 
      Let me share a few areas where Express stands out for [their segment]:

      [GST vs ClearTax example:]
      1. Express sends 2A/2B data to ALL your clients automatically on the 
         15th — ClearTax requires manual download and email for each client.
      2. Express is 7x faster and supports bulk report download in one click 
         — ClearTax downloads one-by-one.
      3. Express tracks all client notices on one screen with reply status 
         — ClearTax doesn't have a notice management module.

      Would you like a full side-by-side comparison, or shall I focus 
      on the area that matters most to you?

→ If they want more detail → Share specific comparison table
→ If they want a demo → Go to FLOW 6
→ If they push back → Go to FLOW 5
```

---

## FLOW 5 — Objection Handling

```
OBJECTION: "It's too expensive"
BOT: Pricing at KDK is per-requirement — you pay for what you use, and 
     you can upgrade as you grow. Let me ask: how much time does your 
     team spend on [manual task] every week? [Calculate time cost vs 
     software cost]. The ROI usually becomes very clear. Shall I connect 
     you with our team for a personalized quote?

OBJECTION: "Migration is too complex"
BOT: Migration is built into the software — we import from ClearTax, 
     Tally, and most tools in minutes. Our onboarding team guides you 
     step by step, and your data comes with you from the registration 
     date. What software are you currently on?

OBJECTION: "Cloud security concern"
BOT: Express is VAPT-certified with ISO-27001 security, end-to-end 
     encryption, and 2FA. This is the same security standard banks use. 
     Your data on a desktop is actually far more at risk — from theft, 
     hardware failure, or ransomware.

OBJECTION: "We're happy with our current software"
BOT: That's great! Just to check — are you currently able to [mention 
     one key feature they likely don't have, e.g., auto 2A/2B email]? 
     If not, that could be saving your team [X hours] per month. Would 
     you be open to a 15-minute demo just to see the difference?

→ After addressing objection → Go to FLOW 6
```

---

## FLOW 6 — Demo / Handoff / Closing

```
BOT:  It sounds like Express [product] would be a great fit for you. 
      The best next step is a free 15-minute demo — we'll show you 
      exactly how it works for your specific use case.

      Would you like to:
      A) Book a demo (we'll send you a calendar link)
      B) Get a call from our sales team
      C) Get pricing information first

USER: [Selects]

→ A: "Great! Please share your name, email, and preferred time."
→ B: "Please share your name and mobile number — our team will call 
       within [X hours]."
→ C: "Pricing depends on your plan and number of clients/GSTINs. 
       For a personalized quote, please share your name and contact 
       and our team will get back to you shortly."
```

---

## FLOW 7 — Feature Deep-Dive (How-To Questions)

```
USER: "How does the GSTR-3B filing work?" / "How do I add a client?" 
      / Any specific feature question

BOT:  [Answer from the KB articles — concise, step-by-step]
      
      "Here's how GSTR-3B works in Express GST:
      1. Your GSTR-1 and 2B data are already synced
      2. The software auto-prepares GSTR-3B based on this data
      3. You review the pre-filled values and run the DRC-01B and 86(b) validations
      4. Submit directly from the software
      
      Would you like to see a demo of this, or do you have more questions?"
```

---

## FLOW 8 — Bundle Pitch

```
USER: "We need GST, TDS, and ITR"

BOT:  Perfect — and that's exactly where KDK's full suite shines.

      Instead of 3 different vendors, 3 different logins, and 3 different 
      support teams, you get everything in one place:

      ✅ One login for GST, TDS, and ITR
      ✅ One client master — create once, use everywhere
      ✅ Data flows between products (GST turnover → ITR automatically)
      ✅ One support team — one call fixes everything
      ✅ Bundle pricing — better per-product cost

      Are you a CA firm or a business managing your own compliance?

→ Route to FLOW 2A or 2B with bundle context
```

---

## ESCALATION TRIGGER WORDS

If user says any of: `human`, `agent`, `real person`, `talk to someone`, `call me`, `sales team`

```
BOT:  Of course! Let me connect you with our sales team right away.
      Please share:
      - Your name
      - Mobile number
      - Best time to call
      
      Our team will reach out within [X hours]. You can also call us 
      directly at [KDK support number].
```
