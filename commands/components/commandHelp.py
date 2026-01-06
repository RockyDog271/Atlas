ErrorInvalidCommand = ""
GithubLink = "https://github.com/RockyDog271/Atlas"
DEBUG = 1 #1 for on, 0 for off

async def commandHelp(CMD_PREFIX, MessageList, Message, message):
    if DEBUG == 1:
        print(f"\033[35mDEBUG\033[0m: message == {Message}")
    if len(MessageList) >= 1 and "!" not in Message:
        await message.channel.send(
            f"Here is a list of all commands and functions:"
            f"\n**Functions**"
            f'\n"Atlas, <text>" to talk with AtlasAI'
            f"\nEXAMPLE: Atlas, what is a cheeseburger composed of?"
            f"\n**Commands**"
            f"\n{CMD_PREFIX}help"
            f"\n{CMD_PREFIX}info"
            f"\n{CMD_PREFIX}echo"
            f"\n{CMD_PREFIX}rand"
            f"\n{CMD_PREFIX}avatar"
            f"\n{CMD_PREFIX}roast"
            f"\n{CMD_PREFIX}joke"
            f"\n{CMD_PREFIX}wants"
            f"\n{CMD_PREFIX}tools"
            f"\n{CMD_PREFIX}github"
            f"\n{CMD_PREFIX}admin"
            f"\n\n{CMD_PREFIX}help !<**Command**> for specific help pages"
            f"\n\nEXAMPLE:"
            f"\n`{CMD_PREFIX}help !help`"
        )
    else:
        if len(MessageList) >= 2 and MessageList[1] in ("!help", "!?"):
            await message.channel.send(
                f"I just feel..."
                f"\nI feel like you should know this one?"
                f"\n-IVORY"
                f"\n\n{CMD_PREFIX}help for help page"
                f"\n{CMD_PREFIX} help !**<command name>** for more detail"\
            )
        elif len(MessageList) >= 2 and MessageList[1] == "!info":
            await message.channel.send(
                f"Here is a list of all available commands:"
                f"\n{CMD_PREFIX}info !ping"
                f"\n{CMD_PREFIX}info !whoami"
                f"\n{CMD_PREFIX}info !server"
                f"\n{CMD_PREFIX}info !bot"
                f'\n\nFor more specific help, use `info !<**command**> !help'
                f"\n EXAMPLE:"
                f"\n`{CMD_PREFIX}info !whoami !help`"
            )
        elif len(MessageList) >= 2 and MessageList[1] == "!echo":
            await message.channel.send(
                f"Here is a list of all available commands:"
                f"\n{CMD_PREFIX}echo <text>"
                f'\n{CMD_PREFIX}echo <text> !""'
                f'\n\nFor more specific help, use `info !<**command**> !help'
                f"\n EXAMPLE:"
                f"\n`{CMD_PREFIX}echo !help`"
            )
        elif len(MessageList) >= 2 and MessageList[1] == "!rand":
            await message.channel.send(
                f"Here is a list of all available commands:"
                f"\n{CMD_PREFIX}rand"
                f"\n{CMD_PREFIX}rand !min<num> !max<num>"
                f"\n{CMD_PREFIX}rand !8ball"
                f"\n{CMD_PREFIX}rand !<dice>"
                f"\n{CMD_PREFIX}rand !coinflip"
                f"\n{CMD_PREFIX}rand !<rps>"
                f"\n{CMD_PREFIX}rand !<RockPaperScissors>"
                f"\n{CMD_PREFIX}rand !rate"
                f"\n{CMD_PREFIX}rand !yes/no"
                f'\n\nFor more specific help, use `info !<**command**> !help'
                f"\n EXAMPLE:"
                f"\n`{CMD_PREFIX}rand !dice !help`"
            )
        elif len(MessageList) >= 2 and MessageList[1] == "!avatar":
            await message.channel.send(
                f"Here is a list of all available commands:"
                f"\n{CMD_PREFIX}avatar"
                f"\n{CMD_PREFIX}avatar !@user"
                f'\n\nFor more specific help, use `info !<**command**> !help'
                f"\n EXAMPLE:"
                f"\n`{CMD_PREFIX}avatar !help`"
            )
        elif len(MessageList) >= 2 and MessageList[1] == "!roast":
            await message.channel.send(
                f"Here is a list of all available commands:"
                f"\n{CMD_PREFIX}roast !me"
                f"\n{CMD_PREFIX}roast !@user"
                f'\n\nFor more specific help, use `info !<**command**> !help'
                f"\n EXAMPLE:"
                f"\n`{CMD_PREFIX}roast !@user !nomercy`"
            )
        elif len(MessageList) >= 2 and MessageList[1] == "!joke":
            await message.channel.send(
                f"Here is a list of all available commands:"
                f"\n{CMD_PREFIX}joke"
                f"\n{CMD_PREFIX}joke !<text>"
                f'\n\nFor more specific help, use `info !<**command**> !help'
                f"\n EXAMPLE:"
                f"\n`{CMD_PREFIX}joke help`"
            )
        elif len(MessageList) >= 2 and MessageList[1] == "!wants":
            await message.channel.send(
                f"Here is a list of all available commands:"
                f"\n{CMD_PREFIX}wants"
                f"\n{CMD_PREFIX}wants !suggestion"
                f'\n\nFor more specific help, use `info !<**command**> !help'
                f"\n EXAMPLE:"
                f"\n`{CMD_PREFIX}wants !help`"
            )
        elif len(MessageList) >= 2 and MessageList[1] == "!tools":
            await message.channel.send(
                f"Here is a list of all available commands:"
                f"\n{CMD_PREFIX}tools !time"
                f'\n\nFor more specific help, use `info !<**command**> !help'
                f"\n EXAMPLE:tools !time !help"
                f"\n`{CMD_PREFIX}`"
            )
        elif len(MessageList) >= 2 and MessageList[1] == "!github":
            await message.channel.send(
                f"yk what . . . ?"
                f"\nI'm going to save us both some time"
                f"\nhere ya go:"
                f"\n{GithubLink}"
                f"\n-IVORY :3"
            )
        elif len(MessageList) >= 2 and MessageList[1] == "!admin":
            await message.channel.send(
                f"Here is a list of all available commands:"
                f"\n{CMD_PREFIX}admin !timeout !@user"
                f"\n{CMD_PREFIX}admin !kick !@user"
                f"\n{CMD_PREFIX}admin !ban !@user"
                f"\n{CMD_PREFIX}admin !purge"
                f"\n{CMD_PREFIX}admin !modlog"
                f"\n{CMD_PREFIX}admin !userlog"
                f"\n{CMD_PREFIX}admin !userjoin"
                f'\n\nFor more specific help, use `info !<**command**> !help'
                f"\n EXAMPLE:"
                f"\n`{CMD_PREFIX}admin !timeout !@user !help`"
            )
        else:
            await message.channel.send(f"Unknown command {Message}")