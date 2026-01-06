# Imports all of the wonderful commands in .components
from .components.commandAvatar import commandAvatar
from .components.commandGithub import commandGithub
from .components.commandRoast import commandRoast
from .components.commandWants import commandWants
from .components.commandTools import commandTools
from .components.commandAdmin import commandAdmin
from .components.commandHelp import commandHelp
from .components.commandInfo import commandInfo
from .components.commandEcho import commandEcho
from .components.commandRand import commandRand
from .components.commandJoke import commandJoke

# Importing os to get .env VAR
import os

AUTH_ID = int(os.getenv("AUTH_ID"))

ErrorNoCommandFound = "ErrorNoCommandFound"
DEBUG = 0 # 1 for on, 0 for off

async def Atlas_commands(Message, message, CMD_PREFIX):
    if DEBUG == 1:
        print(f"\033[35mDEBUG\033[0m: message == {Message}")
    Message = Message.lower().replace(CMD_PREFIX, "")
    MessageList = Message.split(maxsplit = 10)
    if DEBUG == 1:
        print(f"\033[35mDEBUG\033[0m: message REPR == {repr(Message)}")

    if len(MessageList) >= 1 and MessageList[0] == ("help"):
        await commandHelp(CMD_PREFIX, MessageList, Message, message)
        return

    elif len(MessageList) >= 1 and MessageList[0] == ("info"):        
        await commandInfo(MessageList, Message, message)
        return

    elif len(MessageList) >= 1 and MessageList[0] == ("echo"): 
        Message == Message.strip("echo", "")
        await commandEcho(MessageList, Message, message)
        return
    
    elif len(MessageList) >= 1 and MessageList[0] == ("rand"): 
        Message == Message.strip("rand", "")
        await commandRand(MessageList, Message, message)
        return
    
    elif len(MessageList) >= 1 and MessageList[0] == ("avatar"): 
        Message == Message.strip("avatar", "")
        await commandAvatar(MessageList, Message, message)
        return
    
    elif len(MessageList) >= 1 and MessageList[0] == ("roast"): 
        Message == Message.strip("roast", "")
        await commandRoast(MessageList, Message, message)
        return

    elif len(MessageList) >= 1 and MessageList[0] == ("joke"): 
        Message == Message.strip("joke", "")
        await commandJoke(MessageList, Message, message)
        return
    
    elif len(MessageList) >= 1 and MessageList[0] == ("wants"): 
        Message == Message.strip("wants", "")
        await commandWants(MessageList, Message, message)
        return

    elif len(MessageList) >= 1 and MessageList[0] == ("tools"): 
        Message == Message.strip("tools", "")
        await commandTools(MessageList, Message, message)
        return
    
    elif len(MessageList) >= 1 and MessageList[0] == ("github"): 
        Message == Message.strip("github", "")
        await commandGithub(MessageList, Message, message)
        return

    elif len(MessageList) >= 1 and MessageList[0] == ("admin"): 
        if message.author.id != AUTH_ID:
            return
        Message == Message.strip("admin", "")
        await commandAdmin(MessageList, Message, message)
        return
    else:
        await message.channel.send(ErrorNoCommandFound)
        return