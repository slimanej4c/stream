
import openai
import requests
import time
import cv2
import base64
import time
import openai
import os
import requests
from IPython.display import display, Image, Audio
from openai import OpenAI
api_key = 'sk-proj-BCtNALBJdUhNjwA2XKPoT3BlbkFJ14y9f2uLvjfWYGvLCL2r'
os.environ["OPENAI_API_KEY"] = api_key
client = OpenAI()

video = cv2.VideoCapture("./video/experiment_video_desc.mp4")

base64Frames = []
while video.isOpened():
    success, frame = video.read()
    if not success:
        break
    _, buffer = cv2.imencode(".jpg", frame)
    base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

video.release()
print(len(base64Frames), "frames read.")

PROMPT_MESSAGES = [
    {
        "role": "user",
        "content": [
            "These are frames of a video. Create a short voiceover script in the style of David Attenborough. Only include the narration.",
            *map(lambda x: {"image": x, "resize": 768}, base64Frames[0::400]),
        ],
    },
]

response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=PROMPT_MESSAGES,
    max_tokens=500,
)

print(response.choices[0].message.content)
speech_file_path = "speech.mp3"
audio_response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=response.choices[0].message.content
)

audio_response.stream_to_file(speech_file_path)
Audio(speech_file_path, autoplay=True)