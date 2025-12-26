# task1
pan2025task

## 电报机器人 (Telegram Bot)

这个项目实现了一个简单的电报机器人。

This project implements a simple Telegram Bot.

### 功能特性 (Features)

- 消息接收和处理 (Message receiving and handling)
- 命令支持 (Command support)
- 配置管理 (Configuration management)
- 日志记录 (Logging)

### 使用方法 (Usage)

#### 1. 运行演示程序 (Run Demo)

```bash
python3 telegram_bot.py
```

#### 2. 配置机器人 (Configure Bot)

编辑 `config.py` 文件，填入您的 Telegram Bot Token：

Edit `config.py` and add your Telegram Bot Token:

```python
TELEGRAM_CONFIG = {
    'token': 'YOUR_BOT_TOKEN_HERE',
    ...
}
```

#### 3. 获取 Bot Token

1. 在 Telegram 中找到 @BotFather
2. 发送 `/newbot` 命令
3. 按照提示创建机器人
4. 获取 Token 并填入配置文件

#### 4. 支持的命令 (Supported Commands)

- `/start` - 开始使用机器人 (Start the bot)
- `/help` - 显示帮助信息 (Show help)
- `/info` - 显示机器人信息 (Show bot info)

### 文件说明 (File Description)

- `telegram_bot.py` - 主程序文件 (Main bot implementation)
- `config.py` - 配置文件 (Configuration file)
- `requirements.txt` - Python依赖 (Python dependencies)

### 依赖安装 (Install Dependencies)

```bash
pip install -r requirements.txt
```

### 示例输出 (Example Output)

```
==================================================
电报机器人演示程序
Telegram Bot Demo
==================================================

测试消息处理功能：
Testing message handling:

输入: /start
回复: 欢迎使用电报机器人！Welcome to Telegram Bot!

输入: /help
回复: 可用命令：/start, /help, /info

输入: /info
回复: 这是一个简单的电报机器人实现

输入: 你好
回复: 收到消息：你好
```
