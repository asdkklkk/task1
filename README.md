# task1
pan2025task

## TelegramX Bot

A simple and lightweight Telegram bot implementation for sending notifications and messages.

### Features

- Send text messages to Telegram chats
- Send formatted notifications with titles and body text
- Configuration via environment variables or JSON file
- Logging support for debugging and monitoring

### Setup

1. **Get a Telegram Bot Token:**
   - Talk to [@BotFather](https://t.me/botfather) on Telegram
   - Create a new bot using `/newbot` command
   - Copy the bot token provided

2. **Get your Chat ID:**
   - Start a chat with your bot
   - Send any message to the bot
   - Visit `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Find your chat ID in the response

3. **Configure the bot:**
   
   Option A - Using environment variables:
   ```bash
   export TELEGRAM_BOT_TOKEN="your_bot_token_here"
   export TELEGRAM_CHAT_ID="your_chat_id_here"
   ```
   
   Option B - Using configuration file:
   ```bash
   cp config.json.example config.json
   # Edit config.json with your bot token and chat ID
   ```

### Usage

**Basic usage:**

```python
from telegramx_bot import TelegramXBot

# Initialize the bot
bot = TelegramXBot()

# Send a simple message
bot.send_message("Hello from TelegramX!")

# Send a notification
bot.send_notification(
    title="Alert",
    body="This is an important notification"
)
```

**Running the demo:**

```bash
python telegramx_bot.py
```

### Requirements

- Python 3.6 or higher
- No external dependencies for basic functionality

For production use with full Telegram API features, install:
```bash
pip install -r requirements.txt
```

### Configuration Options

The bot can be configured using:
- Environment variables (recommended for production)
- JSON configuration file (config.json)
- Direct parameter passing to the TelegramXBot class

### License

This project is provided as-is for educational and notification purposes.
