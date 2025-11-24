# Ultimate Account Plan Agent 2025

**One file. Zero setup pain. 60–90 seconds from company name to battle-ready account plan.**  
Works with your voice or keyboard. Fixes conflicting data automatically. Speaks the full plan into your ear.

Built, battle-tested, and used daily by **B Prem Kumar**  
GitHub → https://github.com/Premkumar-2004/account-plan-agent  

---

## Why This Exists

I was sick of:
- 47 tabs open
- Crunchbase saying $450M, TechCrunch saying $620M
- Manually writing the same account plan format every week
- Tools that “research” but still leave me doing 80% of the work

So I built the agent I actually use every single day — before standup, on walks, on flights.

Now I just say “Anthropic” and come back with a full plan being spoken into my AirPods.

---

## What You Actually Get

- Correct official website (never wrong)
- Latest funding, revenue, valuation, headcount
- Real customers + competitors
- Current initiatives & 2025–2026 buying triggers
- Top 3 pain points with proof from their own site/news
- Decision-makers (when public)
- 3 messaging angles that actually land
- Full 90-day outreach sequence
- Every objection you’ll hear + how to crush it

All in under 90 seconds. Spoken or printed.

---

## Who This Is For (Real People, Real Jobs)

- **Enterprise AEs** who hate research but love closing
- **SDR/BDRs** building target account lists at scale
- **Founders** doing cold outreach (this is pure gold)
- **RevOps / SalesOps** building territory plans
- **VPs of Sales** who want their team 5x faster
- **Students / bootcamp grads** who want to look like senior AEs on day 1

If you sell B2B software — this is your new superpower.

---

## Architecture – Simple, But Does the Hard Work

```mermaid
graph TD
    A[You] -->|Voice or Text| B(Choose Mode)
    B --> C[Company Name]
    C --> D[GPT-4o → Official URL]
    D --> E[Scrape Homepage]
    E --> F[Deep Research + Auto Fix Conflicts]
    F --> G[Clean Data]
    G --> H{Say "correct"?}
    H -->|Yes| I[Live Editing]
    H -->|No| J[Generate Account Plan]
    I --> J
    J --> K[Print + Speak Full Plan]
    
    style A fill:#ef4444,color:white
    style K fill:#0d9488,color:white
    style J fill:#10b981,color:white


## Installation – Takes Exactly 2 Minutes

```bash
# 1. Clone the project
git clone https://github.com/Premkumar-2004/account-plan-agent.git
cd account-plan-agent

# 2. Install everything it needs
pip install openai beautifulsoup4 requests pyttsx4 speechrecognition pyaudio

# ← Windows users: if pyaudio fails, run these two lines first →
# pip install pipwin
# pipwin install pyaudio

# 3. Run it
python final-agent.py
