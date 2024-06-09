import openai
import requests
import time
import os
import openai
import base64
import requests
from openai import OpenAI
api_key = 'sk-proj-BCtNALBJdUhNjwA2XKPoT3BlbkFJ14y9f2uLvjfWYGvLCL2r'
os.environ["OPENAI_API_KEY"] = api_key
client = OpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
base64_image = encode_image("./img/img_animal.jpg")
'''response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Whats in the image?"},
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}"
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0].message.content)
target_language = "arabe"
messages = [{"role": "system", "content": """I want you to act as an algorithm for translation to language {}. Systep will provide you with a text, and your only task is to translate it to {}. Never break character.""".format(target_language, target_language)}]
messages.append({"role": "user", "content": response.choices[0].message.content})

# NOTE: This model might be changed or depreicated in the future, use the most updated one :)
chat_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.9,
    max_tokens=2000,
)
print("Assistant:", chat_response.choices[0].message.content)'''


response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Act as a image classification algorithm. Your task is to classify this image witch animals, and nothing else"},
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{base64_image}"
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0].message.content)