import os

# getting the .env VARS
BOT_ID = int(os.getenv("BOT_ID"))
AUTH_ID = int(os.getenv("AUTH_ID"))

ErrorUnknown = "ErrorUnknown: an Unknown Error occurred, :/"
ErrorAuthNeeded = "ErrorAuthNeeded: Authorization Required for ADMIN commands"
ErrorBotDetected = "ErrorBotDetected: Bot input detected, Bots/Apps are not allowed to run ADMIN commands"

async def adminTimeoutUser(MessageList, message):
    return
async def adminKickUser(MessageList, message):
    return
async def adminBanUser(MessageList, message):
    return
async def adminPurgeFunction(MessageList, message):
    return
async def adminModlog(MessageList, message):
    return
async def adminUserlog(MessageList, message):
    return
async def adminUserjoin(MessageList, message):
    return

# Separate from the rest because it has a lot of text and is generally annoying
async def adminHelpFunctions(MessageList, message):
    return

# main def for sorting commands and sending them to the proper def /\ :3
async def commandAdmin(MessageList, Message, message):
    if message.author.id == BOT_ID:     # check if the one sending the command is a bot or not
        await message.channel.send(ErrorBotDetected)
        return
    if message.author.id != AUTH_ID:    # checks for AUTH_ID for ERROR handling
        await message.channel.send(ErrorAuthNeeded)
        return
    if message.author.id == AUTH_ID:    # checks for AUTH_ID before proceeding
        if len(MessageList) >= 1 and "!" not in Message:
            await message.channel.send(
                "This command **REQUIRES** !flags"
                "\nUse `help !admin` for available flags"
            )
        if len(MessageList) >= 2 and MessageList[1] == ("!timeout"):
            await adminTimeoutUser(MessageList, message)
            return
        if len(MessageList) >= 2 and MessageList[1] == ("!kick"):
            await adminTimeoutUser(MessageList, message)
            return
        if len(MessageList) >= 2 and MessageList[1] == ("!ban"):
            await adminTimeoutUser(MessageList, message)
            return
        if len(MessageList) >= 2 and MessageList[1] == ("!purge"):
            await adminTimeoutUser(MessageList, message)
            return
        if len(MessageList) >= 2 and MessageList[1] == ("!modlog"):
            await adminTimeoutUser(MessageList, message)
            return
        if len(MessageList) >= 2 and MessageList[1] == ("!userlog"):
            await adminTimeoutUser(MessageList, message)
            return
        if len(MessageList) >= 2 and MessageList[1] == ("!userjoin"):
            await adminTimeoutUser(MessageList, message)
            return
    else:
        await message.channel.send(ErrorUnknown)