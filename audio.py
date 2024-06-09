
import openai
import requests
import time
import os
import openai

from openai import OpenAI
api_key = 'sk-proj-BCtNALBJdUhNjwA2XKPoT3BlbkFJ14y9f2uLvjfWYGvLCL2r'
os.environ["OPENAI_API_KEY"] = api_key
client = OpenAI()


audio_file = open("./audio/audio_file_whisper.mp3", "rb")

'''transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file,
  response_format='vtt'
)'''
#print(transcript)
transcript_translated = client.audio.translations.create(
  model="whisper-1",
  file=audio_file
)
print(transcript_translated.text )
target_language = "francais"
messages = [{"role": "system", "content": """I want you to act as an algorithm for translation to language {}. Systep will provide you with a text, and your only task is to translate it to {}. Never break character.""".format(target_language, target_language)}]
messages.append({"role": "user", "content": transcript_translated.text})

# NOTE: This model might be changed or depreicated in the future, use the most updated one :)
chat_response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0.9,
    max_tokens=2000,
)
print("Assistant:", chat_response.choices[0].message.content)