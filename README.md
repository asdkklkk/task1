# task1
pan2025task

## TrelegramX

TrelegramX is a simple messaging application module that provides basic messaging functionality.

### Features

- User management (add users with unique IDs and usernames)
- Message sending between users
- Message retrieval for individual users
- Message history tracking

### Usage

```python
from trelegramx import TrelegramX

# Create a new TrelegramX instance
app = TrelegramX()

# Add users
app.add_user('user1', 'Alice')
app.add_user('user2', 'Bob')

# Send a message
app.send_message('user1', 'user2', 'Hello, Bob!')

# Get user messages
messages = app.get_user_messages('user2')
```

### Running the Demo

```bash
python3 trelegramx.py
```
