import discord
from discord.ext import commands
from decouple import config

from datetime import datetime
import os

extdir = "extensions" # Name of the directory in which all the extensions files go

prefix = ['?', '? '] # Prefix(s) of the bot
intents = discord.Intents.all() # Intents of the bot
client = commands.Bot(
    command_prefix=prefix, 
    intents=intents,
    case_insensitive=True
)

# Loads all extensions at start
for filename in os.listdir(extdir):
    if filename.endswith(".py"):
        try: 
            extname = f"extensions.{filename[:-3]}"                            
            client.load_extension(extname)
            print(f" * '{extname}'  has been loaded")
        except Exception as e: print(e)
        
@client.event
async def on_ready():
    # Displays once the bot has successfully been started
    print(f'\n * Logged in as {client.user.name}#{client.user.discriminator} \n * Time: {datetime.now()}')
    
# Starts the bot
client.run(config("token"))