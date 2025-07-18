import os
from dotenv import load_dotenv
from openai import OpenAI

# Access environment variables
load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn."
        }
    ]
)

print(completion.choices[0].message.content)