"""
TrelegramX - A simple messaging application module

This module provides basic messaging functionality similar to Telegram.
"""

import time


class TrelegramX:
    """Main TrelegramX application class for managing messages and users."""
    
    def __init__(self):
        """Initialize TrelegramX with empty message and user storage."""
        self.messages = []
        self.users = {}
        
    def add_user(self, user_id, username):
        """
        Add a new user to TrelegramX.
        
        Args:
            user_id (str): Unique identifier for the user
            username (str): Display name for the user
            
        Returns:
            bool: True if user was added successfully, False if user already exists
        """
        if user_id in self.users:
            return False
        self.users[user_id] = {
            'username': username,
            'messages': []
        }
        return True
    
    def send_message(self, from_user_id, to_user_id, content):
        """
        Send a message from one user to another.
        
        Args:
            from_user_id (str): ID of the sender
            to_user_id (str): ID of the recipient
            content (str): Message content
            
        Returns:
            dict: Message object if successful, None if user doesn't exist
        """
        if from_user_id not in self.users or to_user_id not in self.users:
            return None
            
        message = {
            'from': from_user_id,
            'to': to_user_id,
            'content': content,
            'timestamp': time.time()
        }
        
        self.messages.append(message)
        self.users[to_user_id]['messages'].append(message)
        
        return message
    
    def get_user_messages(self, user_id):
        """
        Get all messages for a specific user.
        
        Args:
            user_id (str): ID of the user
            
        Returns:
            list: List of messages for the user, empty list if user doesn't exist
        """
        if user_id not in self.users:
            return []
        return self.users[user_id]['messages']
    
    def get_all_messages(self):
        """
        Get all messages in the system.
        
        Returns:
            list: List of all messages
        """
        return self.messages


def main():
    """Demo usage of TrelegramX."""
    app = TrelegramX()
    
    # Add users
    app.add_user('user1', 'Alice')
    app.add_user('user2', 'Bob')
    
    # Send messages
    app.send_message('user1', 'user2', 'Hello, Bob!')
    app.send_message('user2', 'user1', 'Hi Alice, how are you?')
    
    # Get messages
    bob_messages = app.get_user_messages('user2')
    print(f"Bob has {len(bob_messages)} message(s)")
    
    for msg in bob_messages:
        sender = app.users[msg['from']]['username']
        print(f"  From {sender}: {msg['content']}")


if __name__ == '__main__':
    main()
