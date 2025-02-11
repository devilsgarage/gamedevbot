name: Bluesky Retweet Bot

on:
  schedule:
    - cron: "*/10 * * * *"  # Runs every 10 minutes
  workflow_dispatch:  # Allows manual runs

jobs:
  run-bot:
    runs-on: ubuntu-latest
    env:
      BSKY_USERNAME: ${{ secrets.BSKY_USERNAME }}
      BSKY_APP_PASSWORD: ${{ secrets.BSKY_APP_PASSWORD }}
    steps:
      - name: Checkout repo
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: pip install atproto

      - name: Run bot
        run: python bot.py
