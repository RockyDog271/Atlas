import os
#from urllib import response
from dotenv import load_dotenv
from openai import OpenAI
from collections import deque
load_dotenv()

# Modifiable variables are here \/
DEBUG = 0           # 0 for OFF, 1 for ON
MAX_HISTORY = 10    # The max history that can be stored (default is 10)

# Grabbing the API key for ChatGPT from the environment
ChatGPT = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

SystemPromptNano = (
    'You are a discord chatbot named "Atlas", Your job is to sound like a human when responding.'
    'If you feel incapable of accurately responding respond with "upgrade-model"'
    'Keep responses concise and to the point.'
    'If you cannot answer, respond exactly with: upgrade-model'
    'I repeat, if you cannot answer, respond exactly with: upgrade-model'
)
SystemPromptMini = (
    'You are a discord chatbot named "Atlas", Your job is to sound like a human when responding.'
    'Keep responses concise and to the point.'
)

CHANNEL_MESSAGE_HISTORY = {}

def Message_caching(message):
    ChannelID = message.channel.id
    if ChannelID not in CHANNEL_MESSAGE_HISTORY:
        CHANNEL_MESSAGE_HISTORY[ChannelID] = deque(maxlen = MAX_HISTORY)
    
    CHANNEL_MESSAGE_HISTORY[ChannelID].append({
        "Author": message.author.id,
        "AuthorName": message.author.name,
        "Content": message.content,
        "Timestamp": message.created_at,
    })

# VAR = CHANNEL_MESSAGE_HISTORY.get(ChannelID, [])





async def Atlas_commands(message):
    Message_caching(message)          # this calls the Message_caching function to cache the incoming message
    if message.author.bot:            # exits the loop and returns nothing if message is from a bot/app
        return                        # exits the loop and returns nothing

    ChannelID = message.channel.id
    History = CHANNEL_MESSAGE_HISTORY.get(ChannelID, [])
    content = message.content.strip()
    UserPrompt = content[len("atlas,"):].strip()
    Prompt = (
        "Previous conversation context:\n"
        f"{History}\n\n"
        "Current user message (UserPrompt):\n"
        f"{UserPrompt}"
    )

    if DEBUG == 1:
        print(f"UserPrompt REPR:   {repr(UserPrompt)}")
        print(f"Prompt REPR:       {repr(Prompt)}")
    response = ChatGPT.responses.create(
        model = "gpt-5-nano",
        max_output_tokens = 3000,
        input=[
        {"role": "system", "content": SystemPromptNano},
        {"role": "user", "content": Prompt},
        ]
    )


    if ("upgrade-model" in response.output_text) or (response.output_text == ""): # Checks for model self-upgrade thingy
        if DEBUG == 1:
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