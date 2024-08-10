import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Event that triggers when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Basic command example
@bot.command()
async def hello(ctx):
    await ctx.send('Hello! I am your RFD bot.')

# Run the bot with your token
