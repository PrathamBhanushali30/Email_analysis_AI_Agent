import requests, os
from dotenv import load_dotenv

load_dotenv()
VT_API_KEY = os.getenv("VT_API_KEY")

def main():
    api = "https://www.virustotal.com/api/v3/urls"

    payload = { "url": "https://www.amazon.com" }
    headers = {
        "accept": "application/json",
        "x-apikey": VT_API_KEY,
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(api, data=payload, headers=headers)
    print(f"result of vt url:{response.json()}")

    url_analysis_id = response.json()["data"]["id"].split("-")[1]

    headers = {
    "accept": "application/json",
    "x-apikey": VT_API_KEY
    }
    url_id = requests.utils.quote(url_analysis_id, safe='')
    api2 = f"https://www.virustotal.com/api/v3/urls/{url_id}"

    r = requests.get(api2, headers=headers)
    print(f"result of vt url:{r.json()}")

if __name__ == "__main__":
    main()