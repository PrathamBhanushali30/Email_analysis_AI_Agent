🛡️ AI Email Security & Phishing Analysis Agent

<p align="center">
  <strong>🤖 AI-powered email threat detection • 🧠 Multi-agent SOC analysis • 🔎 Threat intelligence • 🚨 Automated alerting</strong>
</p>

<p align="center">
  An intelligent email-security prototype that continuously monitors Gmail, analyzes suspicious emails and attachments, enriches indicators with VirusTotal, and uses a CrewAI multi-agent system powered by Google Gemini to generate an explainable <strong>SAFE / SUSPICIOUS / MALICIOUS</strong> verdict.
</p>

<p align="center">








</p>

🚀 What Is This?

AI Email Security & Phishing Analysis Agent is an AI-assisted SOC automation project designed to investigate potentially malicious emails with minimal manual intervention.

Instead of relying on a single detection mechanism, the system combines:

📧 Email analysis

🔗 URL extraction

📎 Attachment analysis

#️⃣ SHA-256 file hashing

🦠 VirusTotal threat intelligence

🤖 CrewAI multi-agent reasoning

🧠 Google Gemini

👨‍💻 SOC Manager correlation

🚨 Automated security alerts

📊 Streamlit SOC dashboard

The result is an end-to-end prototype for AI-powered phishing triage and email threat investigation.

✨ Why This Project?

Traditional email-security workflows can require analysts to manually inspect:

Email
 ├── Sender
 ├── Body
 ├── URLs
 ├── Attachments
 ├── File hashes
 └── Threat intelligence

This project attempts to automate that investigation:

                 📧 Incoming Email
                        │
                        ▼
              🔍 Automated Extraction
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       📄 Body        🔗 URLs       📎 Files
          │             │             │
          │             ▼             ▼
          │        VirusTotal      SHA-256
          │             │             │
          └─────────────┼─────────────┘
                        ▼
              🤖 Multi-Agent AI
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
   🎣 Phishing      🔎 Threat         🦠 Malware
     Analyst        Intel Agent        Analyst
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                 👨‍💻 SOC Manager
                        │
                        ▼
             ┌─────────────────────┐
             │  FINAL VERDICT      │
             │                     │
             │ 🟢 SAFE             │
             │ 🟡 SUSPICIOUS       │
             │ 🔴 MALICIOUS        │
             └──────────┬──────────┘
                        │
                 ┌──────┴──────┐
                 ▼             ▼
             📊 Dashboard    🚨 Alert

🧠 Core Capabilities

Capability

Description

📧 Gmail Monitoring

Continuously monitors unread emails using IMAP

🎣 Phishing Detection

AI-assisted analysis of email content and social-engineering indicators

🔗 URL Intelligence

Extracts URLs and checks them against VirusTotal

📎 Attachment Analysis

Extracts attachments and calculates SHA-256 hashes

🦠 Malware Reputation

Looks up attachment hashes through VirusTotal

🤖 Multi-Agent AI

Uses specialized CrewAI agents for different investigation tasks

🧠 Gemini LLM

Provides natural-language security reasoning

👨‍💻 SOC Correlation

Combines multiple analysis streams into a final verdict

🚨 Automated Alerting

Sends email alerts for suspicious/malicious results

📊 SOC Dashboard

Provides a Streamlit interface for investigation history

📝 Audit Logging

Stores analysis results in logs.json

🤖 Multi-Agent SOC Architecture

The project follows a specialized-agent architecture rather than asking one AI agent to perform the entire investigation.

🎣 1. Email Phishing Analyst

Analyzes the email itself for indicators such as:

Social engineering

Urgency

Suspicious requests

Credential harvesting

Impersonation

Phishing intent

Suspicious wording

Malicious attachment references

🔎 2. Threat Intelligence Analyst

Receives URL intelligence from VirusTotal and evaluates:

Malicious detections

Suspicious reputation

Threat indicators

URL-analysis statistics

🦠 3. Malware Analyst

Analyzes attachment reputation using:

Attachment
     ↓
SHA-256
     ↓
VirusTotal Hash Lookup
     ↓
Malware Reputation

The current implementation performs hash-based reputation checks rather than directly uploading attachments to VirusTotal.

👨‍💻 4. SOC Manager

Acts as the final correlation layer.

It combines:

Email Analysis
      +
URL Intelligence
      +
File Intelligence
      ↓
SOC Correlation
      ↓
Final Verdict

Final classifications:

🟢 SAFE
🟡 SUSPICIOUS
🔴 MALICIOUS

🏗️ System Architecture

flowchart TD
    A["📧 Gmail Inbox"] --> B["📥 Gmail Fetcher"]
    B --> C["📄 Email Body"]
    B --> D["🔗 URL Extraction"]
    B --> E["📎 Attachment Handler"]

    D --> F["🦠 VirusTotal URL Intelligence"]
    E --> G["#️⃣ SHA-256 Hashing"]
    G --> H["🦠 VirusTotal File Intelligence"]

    C --> I["🎣 Phishing Analyst"]
    F --> J["🔎 Threat Intelligence Analyst"]
    H --> K["🦠 Malware Analyst"]

    I --> L["👨‍💻 SOC Manager"]
    J --> L
    K --> L

    L --> M{"🚨 Final Verdict"}

    M --> N["🟢 SAFE"]
    M --> O["🟡 SUSPICIOUS"]
    M --> P["🔴 MALICIOUS"]

    O --> Q["📧 Alert"]
    P --> Q

    L --> R["📝 logs.json"]
    R --> S["📊 Streamlit SOC Dashboard"]

🔄 End-to-End Investigation Pipeline

┌──────────────────────────────────────────────────────┐
│                 1. EMAIL COLLECTION                  │
│                    Gmail / IMAP                      │
└──────────────────────────┬───────────────────────────┘
                           ▼
┌──────────────────────────────────────────────────────┐
│                  2. EMAIL PARSING                    │
│          Body • URLs • Attachments                   │
└──────────────────────────┬───────────────────────────┘
                           ▼
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        📄 Email       🔗 URL          📎 File
          Body       Extraction       Extraction
             │             │             │
             │             ▼             ▼
             │       VirusTotal      SHA-256
             │             │             │
             └─────────────┼─────────────┘
                           ▼
┌──────────────────────────────────────────────────────┐
│                   3. AI ANALYSIS                     │
│              CrewAI + Google Gemini                  │
└──────────────────────────┬───────────────────────────┘
                           ▼
┌──────────────────────────────────────────────────────┐
│                   4. CORRELATION                     │
│                    SOC Manager                       │
└──────────────────────────┬───────────────────────────┘
                           ▼
                    ┌──────────────┐
                    │ FINAL RESULT │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           🟢 SAFE     🟡 SUSPICIOUS  🔴 MALICIOUS
                           │            │
                           └─────┬──────┘
                                 ▼
                           🚨 Alerting

🛠️ Technology Stack

Layer

Technology

🐍 Language

Python 3.10+

🤖 Agent Framework

CrewAI

🧠 LLM

Google Gemini

📧 Email

Gmail IMAP

🔎 Threat Intelligence

VirusTotal API

📊 Dashboard

Streamlit

🚨 Alerting

SMTP

🌐 HTTP

Requests

🔐 Hashing

SHA-256

⚙️ Configuration

python-dotenv

📝 Logging

JSON

📁 Project Structure

Email_analysis_AI_Agent/
│
├── 🤖 agents.py
│   └── CrewAI agent definitions
│
├── 🚨 alert.py
│   └── SMTP alerting
│
├── 📎 attachment_handler.py
│   └── Attachment extraction + SHA-256 hashing
│
├── 📊 dashboard.py
│   └── Streamlit SOC dashboard
│
├── 🔗 email_utils.py
│   └── URL extraction utilities
│
├── 📧 gmail_fetcher.py
│   └── Gmail IMAP collection
│
├── 🧠 llm_wrapper.py
│   └── Google Gemini integration
│
├── 🎯 main_agent.py
│   └── Main AI analysis orchestration
│
├── ▶️ run.py
│   └── Continuous monitoring loop
│
├── 📋 tasks.py
│   └── CrewAI task definitions
│
├── 🔎 threat_intel.py
│   └── VirusTotal integration
│
├── 🧪 vt_test.py
│   └── VirusTotal testing utility
│
├── 📎 attachments/
│   └── Locally extracted attachments
│
├── 📝 logs.json
│   └── Analysis history
│
├── 🔐 .env
│   └── Local secrets/configuration
│
└── 📖 README.md

⚡ Quick Start

1️⃣ Clone the Repository

git clone <your-repository-url>
cd Email_analysis_AI_Agent

2️⃣ Create a Virtual Environment

Windows

python -m venv .venv
.venv\Scripts\activate

Linux / macOS

python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install Dependencies

The supplied project does not currently include a requirements.txt.

Install the primary dependencies:

pip install crewai
pip install langchain-google-genai
pip install google-generativeai
pip install python-dotenv
pip install requests
pip install streamlit

🔐 Configuration

Create a .env file in the project root:

GOOGLE_API_KEY=<your-google-gemini-api-key>
VT_API_KEY=<your-virustotal-api-key>

EMAIL_USER=<your-gmail-address>
EMAIL_PASS=<your-gmail-app-password>

ALERT_EMAIL=<security-alert-recipient>

⚠️ NEVER Commit Secrets

Add this to .gitignore:

.env
.venv/
__pycache__/
*.pyc
attachments/

Create an .env.example instead:

GOOGLE_API_KEY=
VT_API_KEY=
HA_API_KEY=

EMAIL_USER=
EMAIL_PASS=
ALERT_EMAIL=

Security warning: If credentials were previously committed or shared publicly, rotate them immediately.

▶️ Running the Agent

Start the continuous email-monitoring system:

python run.py

The agent continuously:

📧 Checks Gmail
      ↓
🔍 Finds unread messages
      ↓
🧠 Analyzes email
      ↓
🔗 Scans URLs
      ↓
📎 Hashes attachments
      ↓
🦠 Queries VirusTotal
      ↓
🤖 Runs CrewAI agents
      ↓
👨‍💻 Generates SOC verdict
      ↓
📝 Saves result
      ↓
🚨 Sends alert if required
      ↓
⏳ Waits and repeats

The current monitoring interval is approximately 60 seconds.

📊 Launch the SOC Dashboard

Open another terminal:

streamlit run dashboard.py

The dashboard reads the analysis history from:

logs.json

and presents information such as:

📧 Analyzed emails

🔗 URL intelligence

📎 File intelligence

🤖 AI analysis

🚨 Final SOC verdict

🔎 Threat Intelligence Workflow

URL Analysis

Email
  ↓
URL Extraction
  ↓
VirusTotal Submission
  ↓
Analysis ID
  ↓
VirusTotal Result
  ↓
Threat Intelligence Agent

The URL intelligence layer can provide security-relevant reputation information that is then supplied to the AI analysis workflow.

Attachment Analysis

Email Attachment
       ↓
Extract File
       ↓
SHA-256
       ↓
VirusTotal Hash Lookup
       ↓
Malware Analyst

This design allows the current implementation to perform reputation checks without directly uploading the attachment itself to VirusTotal.

🧩 Example Security Decision

The final SOC decision can conceptually combine:

┌──────────────────────────────┐
│ Email Content                │
│                              │
│ • Urgency                    │
│ • Social Engineering         │
│ • Credential Request         │
│ • Impersonation              │
└──────────────┬───────────────┘
               │
               +
┌──────────────▼───────────────┐
│ URL Intelligence             │
│                              │
│ • Reputation                 │
│ • Detection Count            │
│ • Suspicious Indicators      │
└──────────────┬───────────────┘
               │
               +
┌──────────────▼───────────────┐
│ File Intelligence            │
│                              │
│ • SHA-256                    │
│ • VirusTotal Reputation      │
│ • Malware Detections         │
└──────────────┬───────────────┘
               │
               ▼
       👨‍💻 SOC Manager
               │
               ▼
      ┌─────────────────┐
      │ FINAL VERDICT   │
      ├─────────────────┤
      │ 🟢 SAFE         │
      │ 🟡 SUSPICIOUS   │
      │ 🔴 MALICIOUS    │
      └─────────────────┘

🚨 Automated Alerting

If the final analysis contains:

SUSPICIOUS

or:

MALICIOUS

the system triggers the alerting mechanism.

AI Verdict
    │
    ├── SAFE ────────────────► No Alert
    │
    ├── SUSPICIOUS ──────────► 🚨 Email Alert
    │
    └── MALICIOUS ───────────► 🚨 Email Alert

The current implementation uses Gmail SMTP over SSL.

📈 Security Engineering Concepts Demonstrated

This project brings together several real-world cybersecurity concepts:

🔐 Email Security

Phishing detection

Social engineering analysis

Malicious URL detection

Attachment analysis

Email automation

🦠 Threat Intelligence

VirusTotal API

IOC reputation

File-hash intelligence

URL intelligence

🤖 AI for Cybersecurity

LLM-based analysis

Multi-agent architecture

Specialized security agents

AI-assisted SOC triage

🧑‍💻 SOC Automation

Alert generation

Automated investigation

Evidence correlation

Security verdict generation

Investigation dashboard

🗺️ Roadmap

🟢 Phase 1 — Core Engine

Gmail monitoring

Unread email detection

Email extraction

URL extraction

Attachment extraction

SHA-256 hashing

VirusTotal URL lookup

VirusTotal hash lookup

CrewAI agents

Gemini integration

SOC verdict

JSON logging

Streamlit dashboard

SMTP alerting

🟡 Phase 2 — Advanced Email Security

HTML email parsing

Email-header analysis

SPF validation

DKIM validation

DMARC validation

Sender reputation

Domain reputation

Brand impersonation detection

Business Email Compromise detection

🟠 Phase 3 — Advanced Threat Intelligence

Hybrid Analysis

YARA

URLhaus

OpenPhish

AbuseIPDB

WHOIS intelligence

IOC enrichment

🔴 Phase 4 — Malware Analysis

Static file analysis

File-type verification

Entropy analysis

Macro detection

PE analysis

Sandbox integration

Malware family classification

🔵 Phase 5 — AI Security

Structured LLM outputs

Confidence scoring

Prompt-injection detection

Rule + AI hybrid detection

Explainable evidence scoring

Analyst feedback loop

Detection evaluation dataset

🟣 Phase 6 — Full SOC Platform

PostgreSQL event storage

User authentication

RBAC

Incident management

IOC management

SIEM integration

MITRE ATT&CK mapping

Real-time dashboard

Multi-analyst workflow

🔒 Production Security Considerations

This repository is currently a prototype/research implementation.

Before production deployment, consider implementing:

🔐 Strong secrets management

🔑 OAuth2 / secure Gmail authentication

👥 RBAC

🧱 API authentication

🛡️ Rate limiting

📦 Attachment size limits

🧹 Safe filename normalization

🔬 File-type verification

🦠 Antivirus/sandbox scanning

🧬 YARA analysis

🌐 HTML/URL sandboxing

📜 Structured audit logging

🗄️ Database-backed event storage

🔒 TLS

🧠 Prompt-injection defenses

📋 Structured LLM output validation

👨‍💻 Human-in-the-loop approval for high-impact actions

⚠️ Important Limitations

The current project should not be treated as a standalone enterprise email-security gateway.

Current limitations include:

Basic URL extraction

Limited HTML-email handling

Local attachment storage

Hash-based attachment reputation

Dependence on VirusTotal availability/API limits

LLM-generated verdicts are probabilistic

No automatic email quarantine

No sender blocking

JSON-based logging

No complete authentication/RBAC layer

No production-grade secret-management system

The AI verdict should therefore be treated as analyst assistance, not an unquestionable security decision.

🎯 Project Goals

The long-term goal is to evolve this prototype into an AI-assisted SOC email investigation platform capable of:

          📧 Email
             │
             ▼
      🔍 Automated Triage
             │
             ▼
       🧠 AI Investigation
             │
             ▼
      🔎 Threat Intelligence
             │
             ▼
      🦠 Malware Analysis
             │
             ▼
       👨‍💻 SOC Correlation
             │
             ▼
       🚨 Risk Decision
             │
       ┌─────┴─────┐
       ▼           ▼
   📊 Dashboard   🚨 Alert

👨‍💻 Author

<p align="center">

Pratham Bhanushali

M.Tech — Artificial Intelligence & Data Science
Specialization: Cybersecurity

</p>

Areas of Interest

Cybersecurity • SOC Automation • AI/ML Security • Threat Intelligence • Phishing Detection • Malware Analysis • Security Automation

⭐ Why This Project Matters

Modern phishing campaigns increasingly combine:

Social engineering + malicious infrastructure + weaponized files + human targeting

A modern SOC therefore needs more than a simple keyword-based filter.

This project explores how AI agents + threat intelligence + automated investigation can work together to reduce the manual effort required for initial email triage.

🤝 Contributing

Contributions, improvements, detection ideas, and security research are welcome.

git checkout -b feature/<your-feature>

Run your tests and security checks before opening a pull request.

Please never submit API keys, passwords, email credentials, or other secrets.

📜 License

Add an appropriate open-source license before publishing the repository.

<p align="center">

🛡️ Built for Cybersecurity Research & AI-Powered SOC Automation

Detect • Investigate • Correlate • Respond

</p>
