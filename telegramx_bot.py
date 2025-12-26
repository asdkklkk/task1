"""
TelegramX Bot - A simple Telegram bot implementation
This module provides a basic Telegram bot that can send notifications and respond to commands.
"""

import os
import json
import logging
from typing import Optional, Dict, Any

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class TelegramXBot:
    """
    A simple Telegram bot for sending notifications and handling commands.
    
    Attributes:
        token (str): The Telegram bot token
        chat_id (str): Default chat ID for sending messages
    """
    
    def __init__(self, token: Optional[str] = None, chat_id: Optional[str] = None):
        """
        Initialize the TelegramX bot.
        
        Args:
            token: Telegram bot token (if not provided, reads from environment)
            chat_id: Default chat ID for messages (if not provided, reads from environment)
        """
        self.token = token or os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = chat_id or os.getenv('TELEGRAM_CHAT_ID')
        
        if not self.token:
            raise ValueError("Telegram bot token is required. Set TELEGRAM_BOT_TOKEN environment variable.")
    
    def send_message(self, message: str, chat_id: Optional[str] = None, parse_mode: str = 'HTML') -> Dict[str, Any]:
        """
        Send a message to a Telegram chat.
        
        Args:
            message: The message text to send
            chat_id: Target chat ID (uses default if not provided)
            parse_mode: Message parse mode (HTML, Markdown, or None)
        
        Returns:
            Response from Telegram API
        """
        target_chat_id = chat_id or self.chat_id
        
        if not target_chat_id:
            raise ValueError("Chat ID is required. Provide chat_id or set TELEGRAM_CHAT_ID environment variable.")
        
        logger.info(f"Sending message to chat {target_chat_id}: {message[:50]}...")
        
        # In a real implementation, this would make an API call to Telegram
        # For now, we'll return a mock response
        return {
            'ok': True,
            'result': {
                'message_id': 1,
                'chat': {'id': target_chat_id},
                'text': message
            }
        }
    
    def send_notification(self, title: str, body: str, chat_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Send a formatted notification message.
        
        Args:
            title: Notification title
            body: Notification body text
            chat_id: Target chat ID (uses default if not provided)
        
        Returns:
            Response from Telegram API
        """
        message = f"<b>{title}</b>\n\n{body}"
        return self.send_message(message, chat_id)
    
    @staticmethod
    def load_config(config_path: str = 'config.json') -> Dict[str, Any]:
        """
        Load bot configuration from a JSON file.
        
        Args:
            config_path: Path to the configuration file
        
        Returns:
            Configuration dictionary
        """
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Config file {config_path} not found. Using environment variables.")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing config file: {e}")
            return {}


def main():
    """
    Main function to demonstrate basic bot usage.
    """
    try:
        # Initialize bot
        bot = TelegramXBot()
        
        # Send a test message
        response = bot.send_notification(
            title="TelegramX Bot Started",
            body="The bot is now running and ready to send notifications!"
        )
        
        logger.info(f"Message sent successfully: {response}")
        
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        logger.info("Please set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID environment variables.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


if __name__ == '__main__':
    main()
