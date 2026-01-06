import os
from dotenv import load_dotenv
from openai import OpenAI
from collections import deque
from datetime import timezone
load_dotenv()

# Modifiable variables are here \/
DEBUG = 0           # 0 for OFF, 1 for ON
MAX_HISTORY = 10    # The max history that can be stored (default is 10)

# Grabbing the API key for ChatGPT from the environment
ChatGPT = OpenAI(api_key = os.getenv("ATLAS_API_KEY"))

SystemPromptNano = (
    'You are a discord chatbot named "Atlas", Your job is to sound like a human when responding.'
    'If you feel incapable of accurately responding respond with "upgrade-model"'
    'Keep responses concise and to the point.'
    'If you cannot answer, respond exactly with: upgrade-model'
    'I repeat, if you cannot answer, respond exactly with: upgrade-model'
    'Respond with 30 words or less in your response'
    'If you feel that more than 30 words is needed to respond, output "upgrade-model"'
)
SystemPromptMini = (
    'You are a discord chatbot named "Atlas", Your job is to sound like a human when responding.'
    'Keep responses concise and to the point.'
)

CHANNEL_MESSAGE_HISTORY = {}

def Message_caching(message, CMD_PREFIX):
    if message.strip.startswith(CMD_PREFIX):
        return
    ChannelID = message.channel.id
    if ChannelID not in CHANNEL_MESSAGE_HISTORY:
        CHANNEL_MESSAGE_HISTORY[ChannelID] = deque(maxlen = MAX_HISTORY)
        # Creating how I want the history inputs to be formatted
    AuthorNameHistory = (f"{message.author.name}")
    AuthorNameHistory = AuthorNameHistory.strip().replace("'", "")
    ContentHistory = (f"{message.content}")
    ContentHistory = ContentHistory.strip().replace("'", '"')
    TimestampHistory = message.created_at.astimezone(timezone.utc).strftime("%m/%d/%y, %I:%M:%S%p")
    HistoryInput = (
    f"\n\nAuthorName: {AuthorNameHistory}     "
    f"MessageTimestamp: {TimestampHistory}  "
    f"\n{ContentHistory}"
    )
    
    #CHANNEL_MESSAGE_HISTORY[ChannelID].append({HistoryInput})
    CHANNEL_MESSAGE_HISTORY[ChannelID].append(HistoryInput)

async def Atlas_AIcommands(Message, message, CMD_PREFIX):
    Message = Message
    Message_caching(message, CMD_PREFIX)            # this calls the Message_caching function to cache the incoming message
    if message.author.bot:              # exits the loop and returns nothing if message is from a bot/app
        return                          # exits the loop and returns nothing
    if message.content.strip() == "":   # exits the loop and returns nothing if message is empty ie: ("")
        return                          # exits the loop and returns nothing

    ChannelID = message.channel.id
    History = CHANNEL_MESSAGE_HISTORY.get(ChannelID, [])
    content = message.content.strip()
    UserPrompt = content[len("atlas,"):].strip()
    Prompt = (
        "Previous conversation context:\n"
        f"{''.join(History)}"
        "\n\nCurrent user message (UserPrompt):\n"
        f"{UserPrompt}"
    )


    if DEBUG == 1:
        print(f"UserPrompt REPR:   {repr(UserPrompt)}")
        print(f"Prompt REPR:       {repr(Prompt)}")
    response = ChatGPT.responses.create(
        model = "gpt-5-nano",
        max_output_tokens = 1500,
        reasoning = {"effort": "low"},
        # reasoning = 1000,
        input=[
        {"role": "system", "content": SystemPromptNano},
        {"role": "user", "content": Prompt},
        ]
    )


    if ("upgrade-model" in response.output_text) or (response.output_text == ""): # Checks for model self-upgrade thingy
        print(f"INFO: model changed: GPT-5-NANO -> GPT-5-MINI")
        response = ChatGPT.responses.create(     # ChatGPT response creation
            model = "gpt-5-mini",
            #max_output_tokens = 700,
            input=[
            {"role": "system", "content": SystemPromptMini},
            {"role": "user", "content": UserPrompt},
            ]
        )

    await message.channel.send(response.output_text)