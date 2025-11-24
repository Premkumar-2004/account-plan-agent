# Ultimate Account Plan Agent 2025

**One file. One command. One minute.**  
Say any company name → get a complete, accurate, spoken enterprise account plan.  
No tabs. No copy-paste. No conflicting data. No excuses.

Built and used every single day by **B Prem Kumar**  
GitHub → https://github.com/Premkumar-2004/account-plan-agent

---

## Why I Built This

I was tired of spending 2–4 hours researching one account.  
Crunchbase says one number, LinkedIn another, news says something else.  
Then I still had to write the damn plan myself.

So I built the tool I actually wanted:  
→ Say “Vercel” while walking to lunch → come back with a full account plan in my AirPods.

It’s now the most valuable piece of software I own.

---

## What You Get in 60–90 Seconds

- Correct company website (never guesses)
- Up-to-date funding, revenue, valuation, headcount
- Real customers & competitors
- Current initiatives and 2025–2026 triggers
- Top 3 pain points with proof
- Decision-makers (when public)
- 3 messaging angles that actually cut through
- 90-day outreach sequence you can start tomorrow
- Objections you’ll hear and exactly how to handle them

And in **voice mode** → the entire plan is read aloud to you.

---

## Live Demo Flow (What You’ll See)

1. Run the script  
2. Choose **voice** or **text** mode  
3. Say or type any company  
4. Watch it research in real time  
5. Optionally say “correct” and fix anything instantly  
6. Receive a battle-ready account plan — printed + spoken

Works perfectly with startups, unicorns, and Fortune 500 companies.

---

## Architecture – Simple but Powerful

```mermaid
graph TD
    A[You] -->|Voice or Text| B(Choose Mode)
    B --> C[Company Name]
    C --> D[GPT-4o → Official Website]
    D --> E[Scrape Real Homepage]
    E --> F[Deep Multi-Source Research<br/>+ Auto Conflict Resolution]
    F --> G[Clean Structured Data]
    G --> H{Correct Anything?}
    H -->|Yes| I[Live Voice/Text Editing]
    H -->|No| J[Generate Full Account Plan]
    I --> J
    J --> K[Print + Speak Complete Plan]
    
    style A fill:#ff6b6b,color:white
    style K fill:#1a535c,color:white
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

