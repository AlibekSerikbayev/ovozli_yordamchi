import openai
from settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_gpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return response['choices'][0]['message']['content']
