from atproto import Client
import os
import time

# Get login details from GitHub Secrets
USERNAME = os.getenv("BSKY_USERNAME")
APP_PASSWORD = os.getenv("BSKY_APP_PASSWORD")
HASHTAGS = ["#gamedevjobs", "#gamejobs"]
TARGET_USER = "did:plc:q2bt6nvwkwt5thhr36zrdm7s"  # workwithindies.com DID

# Login to Bluesky
client = Client()
client.login(USERNAME, APP_PASSWORD)

def search_and_retweet():
    print("Searching for posts...")
    feed = client.app.bsky.feed.get_timeline()  # Fetch recent posts

    for post in feed.feed:
        post_text = post.post.record.text
        post_uri = post.post.uri
        post_author = post.post.author.did  # Unique ID of the post author

        # Check if the post has any of the target hashtags or is from Work With Indies
        if any(hashtag.lower() in post_text.lower() for hashtag in HASHTAGS) or post_author == TARGET_USER:
            print(f"Retweeting: {post_text}")
            client.app.bsky.feed.repost.create(client.me.did, post_uri)
        else:
            print("No matching posts found.")

# Run every 10 minutes
while True:
    search_and_retweet()
    time.sleep(600)  # 10 minutes
