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
    
    # 允许的命令
    'allowed_commands': [
        '/start',
        '/help',
        '/info',
    ],
    
    # 欢迎消息
    'welcome_message': '欢迎使用电报机器人！\nWelcome to Telegram Bot!',
    
    # 帮助信息
    'help_message': '''
可用命令 Available Commands:
/start - 开始使用 Start
/help - 显示帮助 Show help
/info - 机器人信息 Bot info
''',
}

# 日志配置
LOG_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
}
