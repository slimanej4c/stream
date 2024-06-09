
import openai
import requests
import time
import os
import openai
import base64
import requests
from IPython.display import display, Image, Audio
from openai import OpenAI
api_key = 'sk-proj-BCtNALBJdUhNjwA2XKPoT3BlbkFJ14y9f2uLvjfWYGvLCL2r'
os.environ["OPENAI_API_KEY"] = api_key
client = OpenAI()


speech_file_path = "tts_test.mp3"
audio_response = client.audio.speech.create(
  model="tts-1",
  voice="shimmer",
  input="Hey there! I am using TTS API :)"
)

audio_response.stream_to_file(speech_file_path)
Audio(speech_file_path, autoplay=True)