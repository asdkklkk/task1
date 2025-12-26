#!/usr/bin/env python3
"""
TelegramX Bot - Example Usage Script
This script demonstrates various ways to use the TelegramX bot.
"""

import os
from telegramx_bot import TelegramXBot


def example_basic_message():
    """Example: Send a basic text message."""
    print("Example 1: Basic message")
    bot = TelegramXBot()
    response = bot.send_message("Hello from TelegramX! This is a test message.")
    print(f"Response: {response}\n")


def example_notification():
    """Example: Send a formatted notification."""
    print("Example 2: Formatted notification")
    bot = TelegramXBot()
    response = bot.send_notification(
        title="System Alert",
        body="The backup process has completed successfully."
    )
    print(f"Response: {response}\n")


def example_custom_chat():
    """Example: Send message to a specific chat."""
    print("Example 3: Message to specific chat")
    bot = TelegramXBot()
    custom_chat_id = os.getenv('TELEGRAM_CUSTOM_CHAT_ID', bot.chat_id)
    response = bot.send_message(
        "This message is sent to a custom chat ID",
        chat_id=custom_chat_id
    )
    print(f"Response: {response}\n")


def example_config_file():
    """Example: Initialize bot from config file."""
    print("Example 4: Using config file")
    config = TelegramXBot.load_config('config.json')
    
    if config and 'telegram' in config:
        bot = TelegramXBot(
            token=config['telegram'].get('bot_token'),
            chat_id=config['telegram'].get('chat_id')
        )
        response = bot.send_message("Bot initialized from config file!")
        print(f"Response: {response}\n")
    else:
        print("Config file not found or invalid. Using environment variables.\n")


def main():
    """Run all examples."""
    print("=" * 60)
    print("TelegramX Bot - Usage Examples")
    print("=" * 60)
    print()
    
    try:
        # Example 1: Basic message
        example_basic_message()
        
        # Example 2: Notification
        example_notification()
        
        # Example 3: Custom chat
        example_custom_chat()
        
        # Example 4: Config file
        example_config_file()
        
        print("=" * 60)
        print("All examples completed successfully!")
        print("=" * 60)
        
    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("\nPlease ensure you have set the required environment variables:")
        print("  - TELEGRAM_BOT_TOKEN")
        print("  - TELEGRAM_CHAT_ID")
        print("\nOr create a config.json file with your bot credentials.")
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")


if __name__ == '__main__':
    main()
