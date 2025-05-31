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

1. Your child can start a screen time session by typing "i have started watching"
2. The bot will confirm and start the timer
3. When time is up, the bot will send a message
4. If your child doesn't respond, the bot will send three warnings
5. Your child can end the session early by typing `!stop`

## Getting a Discord Bot Token

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Go to the "Bot" section
4. Click "Add Bot"
5. Copy the token and add it to your `.env` file

## Note

Make sure to invite the bot to your Discord server with the necessary permissions (Send Messages, Read Messages, etc.). 