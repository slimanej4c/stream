import openai
import requests
import time
import os
import openai

from openai import OpenAI
api_key = 'sk-proj-BCtNALBJdUhNjwA2XKPoT3BlbkFJ14y9f2uLvjfWYGvLCL2r'
os.environ["OPENAI_API_KEY"] = api_key
client = OpenAI()
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

# Function to display image from a given URL
def show_image_from_url(url):
    response = requests.get(url)                # Send a GET request to the image URL
    img = Image.open(BytesIO(response.content)) # Open the image from the bytes in the response
    plt.imshow(img)                             # Use Matplotlib to display the image
    plt.axis('off')                             # Hide the axis to only show the image
    plt.show()
# Function to display image from a given URL
def save_image_from_url(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:  # Check if the request was successful
        with open(file_path, 'wb') as f:  # Open a file in binary write mode
            f.write(response.content)  # Write the content of the response to the file
        print(f"Image saved at {file_path}")
    else:
        print(f"Error: Unable to retrieve image. Status code: {response.status_code}")
'''response = client.images.generate(
  prompt="man with simpson filtre carton",
  size="1024x1024",
  n=1,
)

image_url = response.data[0].url
show_image_from_url(image_url)'''

from PIL import Image

# Load the mask image


# Resize it to the required dimensions


# Save the resized mask

print('The mask has been resized and saved as "resized_mask.png"')

### ABOVE THIS LINE IS OPTIONAL CODE IN CASE YOUR MASK IS A DIFFERENT SIZE
res = client.images.edit(
  image=open("./img/img.png", "rb"),
  
 prompt="Convert this image to a cartoon style",
  n=1,
  size="1024x1024"
)
for image in res.data:
    show_image_from_url(image.url)