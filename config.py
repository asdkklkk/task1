#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
电报机器人配置文件
Telegram Bot Configuration
"""

# 电报机器人配置
TELEGRAM_CONFIG = {
    # Telegram Bot API Token (需要从 @BotFather 获取)
    # Get from @BotFather on Telegram
    'token': 'YOUR_BOT_TOKEN_HERE',
    
    # 机器人名称
    'bot_name': '电报机器人',
    
    # 欢迎消息
    'welcome_message': '欢迎使用电报机器人！\nWelcome to Telegram Bot!',
    
    # 帮助信息
    'help_message': '''
可用命令 Available Commands:
/start - 开始使用 Start
/help - 显示帮助 Show help
/info - 机器人信息 Bot info
''',
    
    # 机器人信息
    'info_message': '这是一个简单的电报机器人实现\nThis is a simple Telegram Bot implementation',
}
