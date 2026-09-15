#!/usr/bin/env python3
import subprocess
import sys

# Install required packages
print("Installing dependencies...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "python-telegram-bot==20.3", "requests==2.31.0", "python-dotenv==1.0.0", "aiohttp==3.9.1"])

print("Dependencies installed!")
print("Starting bot...")

# Run the bot
subprocess.run([sys.executable, "bot.py"])
