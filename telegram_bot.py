#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的Telegram机器人实现
A Simple Telegram Bot Implementation
"""

import logging
from typing import Optional
from config import TELEGRAM_CONFIG

# 配置日志
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class TelegramBot:
    """电报机器人类 - Telegram Bot Class"""
    
    def __init__(self, token: Optional[str] = None):
        """
        初始化电报机器人
        Initialize Telegram Bot
        
        Args:
            token: Telegram Bot API Token
        """
        self.token = token
        self.running = False
        logger.info("电报机器人已初始化 - Telegram Bot initialized")
    
    def start(self):
        """启动机器人 - Start the bot
        
        Returns:
            bool: True if started successfully, False otherwise
        """
        if not self.token:
            logger.warning("警告：未设置Token - Warning: No token set")
            return False
        
        self.running = True
        logger.info("电报机器人已启动 - Telegram Bot started")
        return True
    
    def stop(self):
        """停止机器人 - Stop the bot"""
        self.running = False
        logger.info("电报机器人已停止 - Telegram Bot stopped")
    
    def send_message(self, chat_id: int, text: str):
        """
        发送消息 - Send a message
        
        Args:
            chat_id: 聊天ID - Chat ID
            text: 消息内容 - Message text
        """
        if not self.running:
            logger.warning("机器人未运行 - Bot is not running")
            return
        
        logger.info(f"发送消息到/Sending message to {chat_id}: {text}")
    
    def handle_message(self, message: str) -> str:
        """
        处理接收的消息 - Handle received message
        
        Args:
            message: 接收的消息 - Received message
            
        Returns:
            回复内容 - Reply text
        """
        if message == "/start":
            return TELEGRAM_CONFIG['welcome_message']
        elif message == "/help":
            return TELEGRAM_CONFIG['help_message'].strip()
        elif message == "/info":
            return TELEGRAM_CONFIG['info_message']
        else:
            return f"收到消息：{message}"


def main():
    """主函数 - Main function"""
    print("=" * 50)
    print("电报机器人演示程序")
    print("Telegram Bot Demo")
    print("=" * 50)
    
    # 创建机器人实例
    bot = TelegramBot()
    
    # 演示功能
    print("\n测试消息处理功能：")
    print("Testing message handling:")
    
    test_messages = ["/start", "/help", "/info", "你好"]
    for msg in test_messages:
        response = bot.handle_message(msg)
        print(f"\n输入: {msg}")
        print(f"回复: {response}")


if __name__ == "__main__":
    main()
