import discord
from discord.ext import commands, tasks
import asyncio
import os
from dotenv import load_dotenv
import datetime

# Load environment variables
load_dotenv()

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Store active timers
active_timers = {}

class ScreenTimeTimer:
    def __init__(self, user_id, channel_id, duration_minutes=30):
        self.user_id = user_id
        self.channel_id = channel_id
        self.duration = duration_minutes
        self.start_time = datetime.datetime.now()
        self.warning_count = 0
        self.is_active = True

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    check_timers.start()

@bot.event
async def on_message(message):
    # Don't respond to our own messages
    if message.author == bot.user:
        return

    # Check if the message contains the trigger phrase (case insensitive)
    if "i have started watching" in message.content.lower():
        user_id = message.author.id
        if user_id in active_timers:
            await message.channel.send("You already have an active timer! Please stop the current session first.")
            return

        # Create new timer (default 30 minutes)
        active_timers[user_id] = ScreenTimeTimer(user_id, message.channel.id)
        await message.channel.send("Ok sunshine! Since you've started watching, I will start the timer. I'll let you know when time's up!")

    # Process commands
    await bot.process_commands(message)

@bot.command(name='stop')
async def stop_watching(ctx):
    user_id = ctx.author.id
    if user_id in active_timers:
        del active_timers[user_id]
        await ctx.send("Great job stopping on time! Your screen time session has ended.")
    else:
        await ctx.send("You don't have any active screen time sessions.")

@tasks.loop(seconds=30)
async def check_timers():
    current_time = datetime.datetime.now()
    for user_id, timer in list(active_timers.items()):
        if not timer.is_active:
            continue

        elapsed_time = (current_time - timer.start_time).total_seconds() / 60
        
        if elapsed_time >= timer.duration:
            channel = bot.get_channel(timer.channel_id)
            if channel:
                if timer.warning_count == 0:
                    await channel.send(f"<@{user_id}> Time's up! Have you stopped?")
                    timer.warning_count += 1
                elif timer.warning_count < 3:
                    await channel.send(f"<@{user_id}> Warning {timer.warning_count + 1}/3: Please stop watching! If you don't respond, I'll have to tell your dad to enable screen time restrictions!")
                    timer.warning_count += 1
                else:
                    await channel.send(f"<@{user_id}> Final warning! I'm notifying your dad about the screen time violation.")
                    timer.is_active = False
                    # Here you could add code to notify the parent (e.g., through a specific channel or DM)

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN')) 