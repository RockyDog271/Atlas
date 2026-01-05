import os
import discord
from dotenv import load_dotenv

# Importing all of the sub-folders in order to call functions
from .commands.atlasAI import Atlas_AIcommands
from .redirect.handler import Redirect_commands
from .commands.core import Atlas_commands

# Modifiable variables are here \/
MAX_MSG_LEN = 1000  # Determines max message length to process responses
CMD_PREFIX = ">> "  # This is the command prefix for 
DEBUG = 0           # 0 for OFF, 1 for ON

# Modifiable variables are here \/
ErrorSomethingWentWrong = "No idea what went from with this one, 403/500 ERROR "
ErrorMessageToLong = "Message send is too long to process\nPlease shorten message message and retry :3"

# Environment variable loading
load_dotenv()
BOT_TOKEN = os.getenv("DISCORD_TOKEN")
AUTH_ID = int(os.getenv("AUTH_ID"))
BOT_ID = int(os.getenv("BOT_ID"))

# Discord setup thingy
intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
intents.members = True
intents.guilds = True

# This connects to the Discord API and is REQUIRED
Client = discord.Client(intents = intents) 

# I honestly don't know what this does but it's important
@Client.event
async def on_ready():
    print(f"INFO: Logged in as: {Client.user}")

#This is the main loop, // the part you edit
@Client.event
async def on_message(message):
    ContentCheck = message.content.strip().lower().replace("'", "")   # Used for all checks in this loop
    if len(message.content) >= MAX_MSG_LEN:
        if not (message.author.id == AUTH_ID or ContentCheck.endswith("!override")):
            print(f"ERROR: ErrorMessageToLong: Message exceeded {MAX_MSG_LEN} chars")
            if message.author.id == BOT_ID:
                return
            await message.channel.send(ErrorMessageToLong)
            return
    Message = message.content.strip("'")

    # If message is the AUTH_ID it sends the content to Redirect_commands
    if message.author.id == AUTH_ID:
        await Redirect_commands(Message, message)
        return

    # If command starts with {STR} prefix, sends to Atlas_commands (in core.py)
    elif ContentCheck.startswith(CMD_PREFIX):
        await Atlas_commands(Message, message, CMD_PREFIX)

    # Checks for either the AI command "Atlas" or for the Atlas discord bot ID
    elif ContentCheck.startswith("atlas,") or message.author.id == BOT_ID:
        await Atlas_AIcommands(Message, message)
        return

    # If the message is coming from a bot it simply returns :3
    elif message.author.bot:
        return

    else:
        return

Client.run(BOT_TOKEN)