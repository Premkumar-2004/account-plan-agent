# final-agent.py — VOICE MODE = SPEAK ONLY | TEXT MODE = TEXT ONLY (PERFECT)
import os
import json
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
from openai import OpenAI

client = OpenAI("api_key")

# === VOICE SETUP ===
try:
    import speech_recognition as sr
    import pyttsx4
    r = sr.Recognizer()
    mic = sr.Microphone()
    engine = pyttsx4.init()
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1.0)
    VOICE_READY = True
except Exception as e:
    VOICE_READY = False
    print("Voice not available → forced text mode")

# === SPEAK ONLY IN VOICE MODE ===
def speak(text):
    if VOICE_MODE:
        print(f"AI: {text}")
        try:
            engine.say(text)
            engine.runAndWait()
        except:
            pass

# === INPUT: Voice or Text ===
def get_input(prompt=""):
    if VOICE_MODE:
        if prompt:
            speak(prompt)
        try:
            with mic as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=10, phrase_time_limit=10)
            text = r.recognize_google(audio).lower()
            print(f"You: {text}")
            return text
        except:
            speak("I didn't hear you. Please try again.")
            return get_input(prompt)  # retry
    else:
        return input(f"{prompt}You: ").strip().lower()

# === CORE FUNCTIONS ===
def clean_url(url):
    if not url.startswith("http"): url = "https://" + url
    try: url = requests.head(url, allow_redirects=True, timeout=10).url
    except: pass
    p = urlparse(url)
    return urlunparse(p._replace(query="", fragment="", scheme="https")).rstrip("/").replace("www.", "")

def scrape(url):
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
        soup = BeautifulSoup(r.text, "lxml")
        for tag in soup(["script","style","nav","footer","header"]): tag.decompose()
        title = soup.title.string.strip() if soup.title else "Unknown"
        text = " ".join(soup.get_text(separator=" ").split())[:30000]
        return {"title": title, "text": text}
    except: return {"title": "Unknown", "text": ""}

def get_official_url(company):
    prompt = f"Return ONLY the official homepage URL for {company}. Example: https://about.amazon.com"
    try:
        resp = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}], temperature=0, max_tokens=50)
        url = resp.choices[0].message.content.strip().strip(' "\'')
        match = re.search(r"https?://[^\s<>'\"]+", url)
        return match.group(0) if match else f"https://www.{company.lower().replace(' ', '')}.com"
    except:
        return f"https://www.{company.lower().replace(' ', '')}.com"

def deep_research(company, url, content):
    speak("Running deep research...")
    prompt = f"""
Research {company} using all sources. Resolve conflicts automatically.
Return ONLY valid JSON:
{{
  "Company Name": "", "Description": "", "Founded": "", "HQ": "", "CEO": "",
  "Employees": "", "Revenue (Latest ARR)": "", "Total Funding": "", "Valuation": "",
  "Key Customers (5-10)": "", "Main Competitors (5-8)": "", "Tech Stack (top 8)": "",
  "Biggest Pain Points": "", "Current Initiatives": "", "Buying Triggers (2025-2026)": ""
}}
"""
    raw = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}], response_format={"type": "json_object"}, temperature=0.2).choices[0].message.content.strip()
    try:
        data = json.loads(raw)
    except:
        data = {"Company Name": company.title()}

    speak("Research complete.")
    for k, v in data.items():
        if v:
            speak(f"{k.replace('_', ' ')}: {v}")

    if "correct" in get_input("Say 'correct' to edit anything: "):
        while True:
            field = get_input("Which field?")
            if "done" in field or not field: break
            value = get_input("New value?")
            if value:
                data[field.title().replace(" ", "")] = value
            speak("Updated.")
    return data

# === START ===
print("Welcome to the Ultimate Account Plan Agent 2025")
print("Do you want TEXT or VOICE mode?")

mode_choice = input("You: ").strip().lower()

VOICE_MODE = ("voice" in mode_choice) and VOICE_READY

if VOICE_MODE:
    speak("Voice mode activated. I'm ready. Say a company name.")
else:
    print("Text mode activated.")
    if not VOICE_READY:
        print("Voice libraries missing → install with: pip install pyttsx4 speechrecognition pyaudio")

# === MAIN LOOP ===
while True:
    company = get_input("Company name: " if not VOICE_MODE else "")
    if not company or "quit" in company or "exit" in company:
        speak("Goodbye!") if VOICE_MODE else print("Goodbye!")
        break

    speak(f"Researching {company}...")
    url = get_official_url(company)
    speak(f"Website: {url.split('//')[1].split('/')[0]}")
    content = scrape(url)
    data = deep_research(company, url, content)

    speak("Generating your account plan...")
    plan_prompt = f"""
Create a sharp Account Plan for {data.get('Company Name', company)} ({data.get('Description', '')}).

Include:
• Strategic Importance & TAM
• Top 3 Pain Points (with proof)
• Key Decision Makers
• 3 Killer Messaging Angles
• 90-Day Next Steps
• Objections & Counters

Be direct and ruthless.
"""
    plan = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": plan_prompt}], temperature=0.4).choices[0].message.content.strip()

    # Final output
    print("\n" + "="*80)
    print(f"ACCOUNT PLAN: {data.get('Company Name','').upper()}")
    print("="*80)
    for k, v in data.items():
        if v and k != "Company Name":
            print(f"{k}: {v}")
    print("\nACCOUNT PLAN:")
    print(plan)
    print("="*80 + "\n")

    # SPEAK ONLY IN VOICE MODE
    if VOICE_MODE:
        for chunk in [plan[i:i+500] for i in range(0, len(plan), 500)]:
            speak(chunk)
        speak("Done. Say next company or quit.")
    else:
        input("Press Enter for next company...")
