from crewai import Agent, LLM
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

# os.environ["GEMINI_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# gemini_model = "gemini/gemini-1.5-flash"

llm = LLM(
    model="gemini-2.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

email_agent = Agent(
    role="Email Phishing Analyst",
    goal="Detect phishing or malicious intent in emails",
    backstory="Expert in phishing detection",
    llm=llm,
    verbose=True
)

url_agent = Agent(
    role="Threat Intelligence Analyst",
    goal="Analyze URLs using VirusTotal results",
    backstory="Expert in malicious URL detection",
    llm=llm,
    verbose=True
)

malware_agent = Agent(
    role="Malware Analyst",
    goal="Analyze file hashes using VirusTotal",
    backstory="Expert in malware detection",
    llm=llm,
    verbose=True
)

coordinator_agent = Agent(
    role="SOC Manager",
    goal="Combine all analysis and give final verdict",
    backstory="Senior SOC decision maker",
    llm=llm,
    verbose=True
)