import praw

reddit = praw.Reddit(
    client_id="5h4vo8TLnRRHkLlzUaMFKA",
    client_secret="J1vwyYuOEl3RQvsAKKhJdoS7ay9TWA",
    username="adityavshinde",
    password="reddit@aditya",
    user_agent="memeops-trends by u/adityavshinde"
)

try:
    print("✅ Logged in as:", reddit.user.me())
except Exception as e:
    print("❌ Error:", e)

