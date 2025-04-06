
import requests
from datetime import datetime
import os

BOT_TOKEN = os.getenv("KITTY_BOT_TOKEN")
CHAT_ID = os.getenv("KITTY_CHAT_ID")
NEWS_API_KEY = "016b7d7f889e45cbbaa035d8c18f3edd"

def get_news():
    categories = {
        "India Politics": "indian politics",
        "Startup India": "startup india",
        "Global Tech": "technology AND global",
        "Indian Stock Market": "nifty sensex stock",
        "Global Economy": "global economy markets"
    }

    headlines = []
    today = datetime.now().strftime("%Y-%m-%d")
    base_url = "https://newsapi.org/v2/everything"

    for cat, query in categories.items():
        params = {
            "q": query,
            "from": today,
            "sortBy": "relevancy",
            "language": "en",
            "pageSize": 3,
            "apiKey": NEWS_API_KEY
        }
        try:
            res = requests.get(base_url, params=params, timeout=10)
            articles = res.json().get("articles", [])
            entries = [f"• {a['title']}" for a in articles]
            headlines.append(f"🗂️ {cat}:
" + "\n".join(entries))
        except Exception as e:
            headlines.append(f"🗂️ {cat}:
• Failed to fetch news.")

    return "\n\n".join(headlines)

# Build the message
today = datetime.now().strftime("%A, %d %B %Y")
news = get_news()

message = f'''
🐾 Good Morning, Ashit!  
Here’s your daily Kitty briefing for {today} 🗞️

📰 Top News:
{news}

📈 Market Update: (Coming Soon)
🏏 Sports Highlights: (Coming Soon)
☁️ Weather: (Coming Soon)
💡 Quote of the Day: "Keep moving forward." – Walt Disney
🍽️ Date Tip: Try something new in Gurgaon this week!
🎟️ Event: Explore something exciting nearby!
💰 Finance Tip: Avoid lifestyle inflation – upgrade your savings before your lifestyle.
🎯 Reflection Prompt: What’s one thing you’re grateful for this week?

Stay awesome 😸
'''

# Send message
send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(send_url, data={
    "chat_id": CHAT_ID,
    "text": message
})

if response.status_code == 200:
    print("✅ Kitty news message sent!")
else:
    print("❌ Failed to send message:", response.text)
