from . import components

async def Atlas_commands(Message, message, CMD_PREFIX):
    Message = Message.lower().replace(CMD_PREFIX, "")
    
    if Message == ("commands"):
        await components.commandList(message)
        return

    elif Message == (""):
        return

    elif Message == (""):
        return
    
    elif Message == (""):
        return
    
    else:

        return