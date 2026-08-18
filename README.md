<div align="center">

# 🛡️ AI Email Security & Phishing Analysis Agent

**🤖 AI-powered email threat detection • 🧠 Multi-agent SOC analysis • 🔎 Threat intelligence • 🚨 Automated alerting**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-FF4B4B.svg)](https://crewai.com/)
[![Google Gemini](https://img.shields.io/badge/LLM-Google_Gemini-8E75B2.svg?logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![VirusTotal](https://img.shields.io/badge/Threat_Intel-VirusTotal-001A70.svg?logo=virustotal&logoColor=white)](https://www.virustotal.com/)

An intelligent email-security prototype that continuously monitors Gmail, analyzes suspicious emails and attachments, enriches indicators with VirusTotal, and uses a CrewAI multi-agent system powered by Google Gemini to generate an explainable **SAFE / SUSPICIOUS / MALICIOUS** verdict.

<br>

</div>

## 🚀 What Is This?

**AI Email Security & Phishing Analysis Agent** is an AI-assisted SOC automation project designed to investigate potentially malicious emails with minimal manual intervention. Instead of relying on a single detection mechanism, the system combines:

*   📧 **Email analysis**
*   🔗 **URL extraction**
*   📎 **Attachment analysis**
*   #️⃣ **SHA-256 file hashing**
*   🦠 **VirusTotal threat intelligence**
*   🤖 **CrewAI multi-agent reasoning**
*   🧠 **Google Gemini LLM**
*   👨‍💻 **SOC Manager correlation**
*   🚨 **Automated security alerts**
*   📊 **Streamlit SOC dashboard**

The result is an end-to-end prototype for AI-powered phishing triage and email threat investigation.

---

## 🧠 Core Capabilities

| Capability | Description |
| :--- | :--- |
| **📧 Gmail Monitoring** | Continuously monitors unread emails using IMAP. |
| **🎣 Phishing Detection** | AI-assisted analysis of email content and social-engineering indicators. |
| **🔗 URL Intelligence** | Extracts URLs and checks them against VirusTotal. |
| **📎 Attachment Analysis** | Extracts attachments and calculates SHA-256 hashes locally. |
| **🦠 Malware Reputation** | Looks up attachment hashes through VirusTotal. |
| **🤖 Multi-Agent AI** | Uses specialized CrewAI agents for different investigation tasks. |
| **🧠 Gemini LLM** | Provides natural-language security reasoning. |
| **👨‍💻 SOC Correlation** | Combines multiple analysis streams into a final verdict. |
| **🚨 Automated Alerting** | Sends SMTP email alerts for suspicious/malicious results. |
| **📊 SOC Dashboard** | Provides a Streamlit interface for investigation history. |
| **📝 Audit Logging** | Stores analysis results locally in `logs.json`. |

---

## 🤖 Multi-Agent SOC Architecture

The project follows a specialized-agent architecture rather than asking one AI agent to perform the entire investigation.

### 🎣 1. Email Phishing Analyst
Analyzes the raw email text for indicators such as:
> *Social engineering • Urgency • Suspicious requests • Credential harvesting • Impersonation • Phishing intent • Suspicious wording • Malicious attachment references*

### 🔎 2. Threat Intelligence Analyst
Receives URL intelligence from VirusTotal and evaluates:
> *Malicious detections • Suspicious reputation • Threat indicators • URL-analysis statistics*

### 🦠 3. Malware Analyst
Analyzes attachment reputation using a hash-based lookup approach to maintain privacy (files are not uploaded):
> `Attachment` ➔ `SHA-256 Hash` ➔ `VirusTotal Lookup` ➔ `Malware Reputation`

### 👨‍💻 4. SOC Manager
Acts as the final correlation layer. It synthesizes insights from the Phishing, Threat Intel, and Malware analysts to produce a final, explainable classification:
*   🟢 **SAFE**
*   🟡 **SUSPICIOUS**
*   🔴 **MALICIOUS**

---

## 🏗️ System Architecture

```mermaid
graph TD
    A["📧 Gmail Inbox"] --> B["📥 Gmail Fetcher"]
    B --> C["📄 Email Body"]
    B --> D["🔗 URL Extraction"]
    B --> E["📎 Attachment Handler"]

    D --> F["🦠 VirusTotal URL Intel"]
    E --> G["#️⃣ SHA-256 Hashing"]
    G --> H["🦠 VirusTotal File Intel"]

    C --> I["🎣 Phishing Analyst"]
    F --> J["🔎 Threat Intel Analyst"]
    H --> K["🦠 Malware Analyst"]

    I --> L["👨‍💻 SOC Manager (Correlation)"]
    J --> L
    K --> L

    L --> M{"🚨 Final Verdict"}

    M -->|"🟢"| N["SAFE"]
    M -->|"🟡"| O["SUSPICIOUS"]
    M -->|"🔴"| P["MALICIOUS"]

    O --> Q["📧 Send Alert"]
    P --> Q

    L --> R["📝 logs.json"]
    R --> S["📊 Streamlit SOC Dashboard"]

```

🛠️ Technology Stack

| Layer | Technology |
|-------|------------|
| 🐍 Language | Python 3.10+|
| 🤖 Agent Framework | CrewAI |
| 🧠 LLM | Google Gemini (google-generativeai) |
| 📧 Email | Gmail IMAP |
| 🔎 Threat Intelligence | VirusTotal API |
| 📊 Dashboard | Streamlit |
| 🚨 Alerting | SMTP |
| 🔐 Hashing | SHA-256 (hashlib) |
