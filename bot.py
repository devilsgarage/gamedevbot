from atproto import Client
import os
import time

# Get login details from GitHub Secrets
USERNAME = os.getenv("BSKY_USERNAME")
APP_PASSWORD = os.getenv("BSKY_APP_PASSWORD")

# Debugging: Check if secrets are properly received
print(f"🔍 Debug: BSKY_USERNAME = {USERNAME}")
print(f"🔍 Debug: BSKY_APP_PASSWORD exists: {'Yes' if APP_PASSWORD else 'No'}")

# Validate login details before running
if not USERNAME or not APP_PASSWORD:
    print("❌ ERROR: Bluesky username or app password is missing.")
    exit(1)  # Exit with an error code

HASHTAGS = ["#gamedevjobs", "#gamejobs"]
TARGET_USER = "did:plc:q2bt6nvwkwt5thhr36zrdm7s"  # Work With Indies DID

# Login to Bluesky
try:
    print("🔄 Attempting to log in to Bluesky...")
    client = Client()
    client.login(USERNAME, APP_PASSWORD)
    print("✅ Successfully logged into Bluesky!")
except Exception as e:
    print(f"❌ Login failed: {e}")
    exit(1)  # Exit with an error code

def search_and_retweet():
    print("🔎 Searching for posts...")
    try:
        feed = client.app.bsky.feed.get_timeline()  # Fetch recent posts
        for post in feed.feed:
            post_text = post.post.record.text
            post_uri = post.post.uri
            post_author = post.post.author.did  # Unique ID of the post author

            # Debugging: Print out the posts found
            print(f"📌 Found post from {post_author}: {post_text[:50]}...")

            # Check if the post has any of the target hashtags or is from Work With Indies
            if any(hashtag.lower() in post_text.lower() for hashtag in HASHTAGS) or post_author == TARGET_USER:
                print(f"🔁 Retweeting: {post_text}")
                client.app.bsky.feed.repost.create(client.me.did, post_uri)
            else:
                print("❌ No matching posts found.")
    except Exception as e:
        print(f"❌ Error while searching for posts: {e}")

# Run once (instead of infinite loop) for debugging
search_and_retweet()
