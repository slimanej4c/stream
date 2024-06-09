import openai
import requests
import time
import os
import openai

from openai import OpenAI
# Remplacez 'YOUR_OPENAI_API_KEY' par votre clé API
api_key = 'sk-proj-BCtNALBJdUhNjwA2XKPoT3BlbkFJ14y9f2uLvjfWYGvLCL2r'
os.environ["OPENAI_API_KEY"] = api_key
client = OpenAI()
print(client.models.list())
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Generate a blog about GTA 5",
    temperature=1,
    max_tokens=700,
)
print(response.choices[0].text)

#https://colab.research.google.com/drive/1OLWCEg-H6ID-sKgBPcn6Gy-NfwyQvCLP?usp=sharing
messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("You: ")
    if user_input == "quit":
        break

    messages.append({"role": "user", "content": user_input})
    chat_response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        temperature=0.9,
        max_tokens=150,
    )
    messages.append({"role": "assistant", "content": chat_response.choices[0].message.content})
    print("Assistant:", chat_response.choices[0].message.content)