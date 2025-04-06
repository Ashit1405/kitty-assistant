
import requests
from datetime import datetime
import os

# Load credentials from environment
BOT_TOKEN = os.getenv("KITTY_BOT_TOKEN")
CHAT_ID = os.getenv("KITTY_CHAT_ID")

# Construct Kitty's daily message
today = datetime.now().strftime("%A, %d %B %Y")

message = f"""🐾 Good Morning, Ashit!  
Here’s your daily Kitty briefing for {today} 🗞️

📰 Top News: (Coming Soon)
📈 Market Update: (Coming Soon)
🏏 Sports Highlights: (Coming Soon)
☁️ Weather: (Coming Soon)
💡 Quote of the Day: "Keep moving forward." – Walt Disney
🍽️ Date Tip: Try something new in Gurgaon this week!
🎟️ Event: Explore something exciting nearby!
💰 Finance Tip: Avoid lifestyle inflation – upgrade your savings before your lifestyle.
🎯 Reflection Prompt: What’s one thing you’re grateful for this week?

Stay awesome 😸
"""

# Send the message via Telegram
send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
response = requests.post(send_url, data={
    "chat_id": CHAT_ID,
    "text": message
})

# Check response
if response.status_code == 200:
    print("✅ Kitty message sent successfully!")
else:
    print("❌ Failed to send message:", response.text)
