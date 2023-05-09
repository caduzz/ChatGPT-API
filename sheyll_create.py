import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.organization = os.getenv("ORGANIZATION") 
openai.api_key = os.getenv("API_KEY")

def shell_command (prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{prompt}",
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None
    )
    return response['choices'][0]['text'].strip()


commmands_create = input('Prompt: ')

command = shell_command(commmands_create)

print(command)