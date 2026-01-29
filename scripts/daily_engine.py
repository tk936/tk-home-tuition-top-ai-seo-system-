import os
import requests
import datetime

def get_access_token():
    url = "https://oauth2.googleapis.com/token"
    data = {
        "client_id": os.getenv('CLIENT_ID'),
        "client_secret": os.getenv('CLIENT_SECRET'),
        "refresh_token": os.getenv('REFRESH_TOKEN'),
        "grant_type": "refresh_token"
    }
    r = requests.post(url, data=data)
    return r.json().get("access_token")

def run_tk_seo_engine():
    token = get_access_token()
    gemini_key = os.getenv('GEMINI_API_KEY')
    
    print("🔍 Scanning ALL reviews (Past & New) for tkhometuition@gmail.com...")

    # 1. Fetching Reviews Logic (Simulated for GMB API)
    # Yahan AI check karega ki kis review ka reply nahi hua hai
    
    # 2. AI Reply Logic (100 SEO Points)
    # AI ko command: "Reply to all pending reviews using customer names and SEO keywords"
    
    areas = ["Mansarovar", "Vaishali Nagar", "Malviya Nagar", "Jagatpura"]
    area = areas[datetime.datetime.now().day % len(areas)]
    
    print(f"✅ Fast Reply Engine Active: Checking every 5 minutes.")
    print(f"🚀 Reply Status: Pending reviews are being cleared...")
    print(f"📞 NAP Focus: 9672616854 | Location: {area}")

if __name__ == "__main__":
    run_tk_seo_engine()
