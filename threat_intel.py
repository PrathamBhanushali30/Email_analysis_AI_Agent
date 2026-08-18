import requests, os
from dotenv import load_dotenv

load_dotenv()
VT_API_KEY = os.getenv("VT_API_KEY")

def scan_url(url):

    url_scanning_api = "https://www.virustotal.com/api/v3/urls"

    payload = { "url": url }
    headers = {
        "accept": "application/json",
        "x-apikey": VT_API_KEY,
        "content-type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url_scanning_api, data=payload, headers=headers)

    url_analysis_id = response.json()["data"]["id"].split("-")[1]

    headers = {
            "accept": "application/json",
            "x-apikey": VT_API_KEY
            }

    api = f"https://www.virustotal.com/api/v3/urls/{url_analysis_id}"

    r = requests.get(api, headers=headers)
    if r.json()["data"]["id"] == url_analysis_id:
        return r.json() #["data"]["attributes"]["last_analysis_stats"]
    return {}

def scan_hash(file_hash):
    headers = {"x-apikey": VT_API_KEY}
    api = f"https://www.virustotal.com/api/v3/files/{file_hash}"

    r = requests.get(api, headers=headers)
    if r.status_code == 200:
        return r.json()["data"]["attributes"]["last_analysis_stats"]
    return {}