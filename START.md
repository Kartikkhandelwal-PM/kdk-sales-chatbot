# KDK Sales Chatbot — Quick Start Guide

## What you need
- **Node.js** installed on your computer → [Download here](https://nodejs.org) (choose "LTS")
- **OpenAI API key** → Get it at [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

---

## Setup (one-time, takes ~3 minutes)

**Step 1 — Open this folder in Command Prompt / Terminal**
- In Windows Explorer, navigate to this `App` folder
- Click the address bar, type `cmd`, press Enter

**Step 2 — Install dependencies**
```
npm install
```

**Step 3 — Add your API key**
- Copy the file `.env.example` and rename the copy to `.env`
- Open `.env` in Notepad
- Replace `sk-xxxxxxxxx...` with your actual OpenAI API key
- Save and close

---

## Run the chatbot

```
npm start
```

Then open your browser and go to: **http://localhost:3000**

To stop it: press `Ctrl + C` in the terminal

---

## What the chatbot does

- Aria (the bot) helps prospects explore Express GST, TDS, and ITR
- **Never reveals pricing** — always redirects to demo booking
- Identifies whether the user is a CA (DIFM) or enterprise (DIY)
- Pushes demo booking after every meaningful answer
- Shows a booking form when user agrees to a demo
- Saves all demo requests to `demo_requests.json` in this folder
- Sidebar counter shows total demos booked

---

## Demo requests

All booked demos are saved in `App/demo_requests.json`.
You can also view them at: http://localhost:3000/api/demos

---

## Recommended model
Default is `gpt-4o-mini` (fast and cost-efficient).
To use GPT-4o, edit `.env` and set: `OPENAI_MODEL=gpt-4o`
