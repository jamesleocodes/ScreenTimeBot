# Screen Time Bot

A Discord bot that helps manage screen time for children. The bot tracks when a child starts watching content and reminds them when their time is up.



## Features

- Start screen time tracking by typing "i have started watching"
- Stop screen time tracking with `!stop`
- Automatic warnings when time is up
- Three-level warning system
- Parent notification system

## Known Limitations and Issues

⚠️ **Important Note**: This is a beta version with some limitations:
- The bot currently doesn't persist data between restarts (all active timers will be reset)
- Parent notifications are not fully implemented yet
- The bot doesn't track daily screen time limits
- No user authentication system is in place
- The bot might not handle multiple users in the same channel optimally

These features are planned for future updates.

## Important Notes

1. **Bot Token Security**:
   - Never share your bot token with anyone
   - Don't commit the `.env` file to version control
   - If your token is compromised, reset it immediately in the Discord Developer Portal

2. **Server Requirements**:
   - The bot needs to be in a server where it has permission to read and send messages
   - Make sure the bot has the necessary permissions when inviting it to your server

3. **Running the Bot**:
   - The bot needs to be running continuously to track screen time
   - If the bot goes offline, all active timers will be reset
   - Consider using a hosting service for 24/7 operation

4. **Parental Control**:
   - This bot is a tool to help manage screen time, not a complete solution
   - Regular monitoring and communication with your child is still important
   - The bot's warnings should be used as a guide, not a replacement for parental supervision

## Setup

1. Install Python 3.8 or higher
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with your Discord bot token:
   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

## How to Use

### For Parents:
1. **Initial Setup**:
   - Create a dedicated channel for the bot in your Discord server
   - Make sure only your child and the bot have access to this channel
   - Explain to your child how the bot works and its purpose

2. **Monitoring**:
   - Check the channel regularly to see if your child is following the screen time rules
   - Look for warning messages that indicate your child might be exceeding their time
   - Use the bot's warnings as conversation starters about responsible screen time use

### For Children:
1. **Starting Screen Time**:
   - When you want to start watching something, go to the bot's channel
   - Type exactly: "i have started watching"
   - The bot will respond with a confirmation message
   - Your screen time session has begun!

2. **During Screen Time**:
   - The bot will automatically track your time
   - You can continue watching until the time is up
   - If you finish early, you can stop the timer

3. **When Time is Up**:
   - The bot will send you a message saying "Time's up!"
   - You should respond by typing `!stop`
   - If you don't stop, the bot will send three warnings
   - After three warnings, it will notify your parent

4. **Stopping Early**:
   - If you want to stop before time is up, type `!stop`
   - The bot will confirm that your session has ended
   - This is good practice and shows responsible screen time management!

### Example Conversation:
```
Child: i have started watching
Bot: Ok sunshine! Since you've started watching, I will start the timer. I'll let you know when time's up!

[30 minutes later]
Bot: @Child Time's up! Have you stopped?

[If no response]
Bot: @Child Warning 1/3: Please stop watching! If you don't respond, I'll have to tell your dad to enable screen time restrictions!

Child: !stop
Bot: Great job stopping on time! Your screen time session has ended.
```

## Getting a Discord Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section
4. Click "Add Bot"
5. Copy the token and add it to your `.env` file

## Note

Make sure to invite the bot to your Discord server with the necessary permissions (Send Messages, Read Messages, etc.). 