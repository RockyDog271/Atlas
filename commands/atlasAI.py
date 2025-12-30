import os
from urllib import response
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

debug = 1   # 0 for OFF, 1 for ON

ChatGPT = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# LLM flow control
# GPT-5 nano    //can call GPT-5-mini if warranted 

SystemPromptNano = (
    'You are a discord chatbot named "Atlas", Your job is to sound like a human when responding.'
    'If you feel incapable of accurately responding respond with "upgrade-model"'
    'Do not respond with reasoning only. Keep responses concise and to the point.'
    'If you cannot answer, respond exactly with: upgrade-model'
    'I repeat, if you cannot answer, respond exactly with: upgrade-model'
)
SystemPromptMini = (
    'You are a discord chatbot named "Atlas", Your job is to sound like a human when responding.'
)

async def Atlas_commands(message):
    content = message.content.strip()            # message striping
    UserPrompt = content[len("atlas,"):].strip()     # more message striping / removing "atlas"
    if debug == 1:
        print(f"UserPrompt REPR:   {repr(UserPrompt)}")
    response = ChatGPT.responses.create(         # ChatGPT response creation
        model = "gpt-5-nano",
        #max_output_tokens = 350,
        input=[
        {"role": "system", "content": SystemPromptNano},
        {"role": "user", "content": UserPrompt},
        ]
    )
    if ("upgrade-model" in response.output_text) or (response.output_text == ""): # Checks for model self-upgrade thingy
        if debug == 1:
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