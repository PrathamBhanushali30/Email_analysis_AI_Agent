from crewai import Task
from agents import email_agent, url_agent, malware_agent, coordinator_agent

def create_tasks(email_text, url_data, file_data):

    email_task = Task(
        description=f"Analyze this email:\n{email_text}",
        expected_output="A detailed assessment of the email's risk level with specific reasons.",
        agent=email_agent
    )

    url_task = Task(
        description=f"Analyze URL scan results:\n{url_data}",
        expected_output="A summary explaining if any URLs are flagged as malicious.",
        agent=url_agent
    )

    malware_task = Task(
        description=f"Analyze file scan results:\n{file_data}",
        expected_output="A breakdown of file safety based on the provided hashes.",
        agent=malware_agent
    )

    coordinator_task = Task(
        description="Combine all above results and give final verdict: SAFE / SUSPICIOUS / MALICIOUS with reason",
        expected_output="A final verdict: SAFE, SUSPICIOUS, or MALICIOUS, followed by a summary of the evidence.",
        agent=coordinator_agent
    )

    return [email_task, url_task, malware_task, coordinator_task]