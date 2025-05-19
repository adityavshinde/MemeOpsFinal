from flask import Flask, render_template, url_for
import praw
import os
from meme_gen import generate_drake_meme

app = Flask(__name__)

# ✅ Reddit API Setup
reddit = praw.Reddit(
    client_id="5h4vo8TLnRRHkLlzUaMFKA",
    client_secret="J1vwyYuOEl3RQvsAKKhJdoS7ay9TWA",
    username="adityavshinde",
    password="reddit@aditya",
    user_agent="memeops-trends by u/adityavshinde"
)

# ✅ Smart contrast checker
def is_meme_friendly(title):
    title = title.lower()
    contrast_keywords = [
        " vs ", " instead of ", " but ", " not ", " rather than ",
        " don't ", " when ", " only to ", " and then ", " although ", " though "
    ]
    for kw in contrast_keywords:
        if kw in title:
            parts = title.split(kw)
            if len(parts) == 2:
                left, right = parts[0].strip(), parts[1].strip()
                if len(left.split()) >= 3 and len(right.split()) >= 3:
                    total_words = len(title.split())
                    if 6 <= total_words <= 20:
                        return True
    return False

# ✅ Filter only titles with good meme format
def filter_contrast_memes(titles):
    return [title for title in titles if is_meme_friendly(title)]

# ✅ Fetch Reddit Titles from multiple subreddits
def fetch_multiple_subreddits(subreddits=["memes", "dankmemes", "ProgrammerHumor", "AdviceAnimals", "funny", "me_irl", "wholesomememes", "technicallythetruth"], count=50):
    titles = []
    for sub in subreddits:
        try:
            subreddit = reddit.subreddit(sub)
            titles.extend([post.title for post in subreddit.hot(limit=count)])
        except Exception as e:
            print(f"Error fetching from subreddit {sub}: {e}")
    return titles

# ✅ Home route - Show trending titles with button
def clean_generated_memes():
    meme_dir = os.path.join("static", "memes")
    if not os.path.exists(meme_dir):
        os.makedirs(meme_dir)
    else:
        for f in os.listdir(meme_dir):
            os.remove(os.path.join(meme_dir, f))

@app.route('/')
def home():
    titles = fetch_multiple_subreddits()
    filtered = filter_contrast_memes(titles)
    return render_template("index.html", titles=filtered)

# ✅ Drake Meme Generator Route
@app.route('/generate-memes')
def generate_memes():
    titles = fetch_multiple_subreddits()
    contrast_titles = filter_contrast_memes(titles)

    clean_generated_memes()
    saved_memes = []
    for i, title in enumerate(contrast_titles):
        clean_title = title.strip().replace("\n", " ")
        filename = f"meme_{i + 1}.jpg"
        path = os.path.join("static", filename)

        try:
            generate_drake_meme(clean_title, path)
            saved_memes.append({"title": clean_title, "file": filename})
        except Exception as e:
            saved_memes.append({"title": clean_title, "error": str(e)})

    return render_template("gallery.html", memes=saved_memes)

if __name__ == '__main__':
    app.run(debug=True)
