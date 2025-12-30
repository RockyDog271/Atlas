import os
import discord
from dotenv import load_dotenv

# FROM IMPORTS
from commands.atlasAI import Atlas_commands
from commands.redirect import Atlas_commands as Redirect_commands

# Environment variable loading
load_dotenv()
BOT_TOKEN = os.getenv("DISCORD_TOKEN")
AUTH_ID = int(os.getenv("AUTH_ID"))

# Discord setup thingy
intents = discord.Intents.default()
intents.message_content = True
Client = discord.Client(intents = intents) 


@Client.event
async def on_ready():
    print(f"Logged in as {Client.user}")

@Client.event
async def on_message(message):
    content = message.content.strip().lower().replace("'", "")

    if message.author.bot:
        return
    
    if message.author.id == AUTH_ID:
        await Redirect_commands(message)
        return

    if content.startswith("atlas,"):
        await Atlas_commands(message)
        return
    
Client.run(BOT_TOKEN)