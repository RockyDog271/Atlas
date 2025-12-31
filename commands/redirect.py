import os
from dotenv import load_dotenv
from openai import OpenAI
#from collections import deque
load_dotenv()

# Modifiable variables are here \/
DEBUG = 0           # 0 for OFF, 1 for ON
MAX_HISTORY = 10    # The max history that can be stored (default is 10)

# Grabbing the API key for ChatGPT from the environment
ChatGPT = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))





async def Atlas_commands(message):
    content = message.content.strip()
    prompt = content

    print(f"PROMPT REPR: {repr(prompt)}")

    response = ChatGPT.responses.create(
        model = "gpt-5.2-chat-latest",
        input = prompt
    )
    response_text = f"Hello Rocky^^\n\n{response.output_text}"
    await message.channel.send(response_text)

