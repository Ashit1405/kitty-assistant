
import requests
from datetime import datetime, timedelta
import os

BOT_TOKEN = os.getenv("KITTY_BOT_TOKEN")
CHAT_ID = os.getenv("KITTY_CHAT_ID")
NEWS_API_KEY = "016b7d7f889e45cbbaa035d8c18f3edd"

def get_news():
    categories = {
        "India Politics": "narendra modi OR indian government OR indian elections",
        "Startup India": "indian startup OR unicorns OR funding",
        "Global Tech": "openai OR google ai OR elon musk OR apple",
        "Indian Stock Market": "nifty OR sensex OR indian stock market",
        "Global Economy": "inflation OR interest rates OR global economy"
    }

    headlines = []
    from_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    base_url = "https://newsapi.org/v2/everything"

    for cat, query in categories.items():
        params = {
            "q": query,
            "from": from_date,
            "sortBy": "relevancy",
            "language": "en",
            "pageSize": 3,
            "apiKey": NEWS_API_KEY
        }
                try:
            res = requests.get(base_url, params=params, timeout=10)
            articles = res.json().get("articles", [])
            entries = [f"• {a['title']}" for a in articles]
            if entries:
                section = f"🗂️ {cat}:\n" + "\n".join(entries)
            else:
                section = f"🗂️ {cat}:\n• No news found."
            headlines.append(section)
        except Exception:
            headlines.append(f"🗂️ {cat}:\n• Failed to fetch news.")


    return "\n\n".join(headlines)

# Compose Kitty's morning message
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

# Send message via Telegram
send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(send_url, data={
    "chat_id": CHAT_ID,
    "text": message
})

# Log result
if response.status_code == 200:
    print("✅ Kitty message sent with news!")
else:
    print("❌ Telegram error:", response.text)
