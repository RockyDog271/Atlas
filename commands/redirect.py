import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

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