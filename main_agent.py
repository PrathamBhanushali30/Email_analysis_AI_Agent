from crewai import Crew
from tasks import create_tasks
from threat_intel import scan_url, scan_hash
from email_utils import extract_urls


def analyze_email(email_obj):
    email_text = email_obj["body"]
    hashes = email_obj["hashes"]

    urls = extract_urls(email_text)

    url_results = {u: scan_url(u) for u in urls}
    file_results = {h: scan_hash(h) for h in hashes}

    tasks = create_tasks(email_text, url_results, file_results)

    crew = Crew(
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()

    return {
        "email": email_text,
        "url_analysis": url_results,
        "file_analysis": file_results,
        "final": str(result)
    }