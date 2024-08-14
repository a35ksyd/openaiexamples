import os
import base64
from openai import OpenAI


image_files = [
    "./images/apple.jpg",
    "./images/orange.jpg",
    "./images/dog.jpg"
]

# Initialize the API client
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

# Read and ecncode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Read all images  and store them in a list
base64_images = [encode_image(image_file) for image_file in image_files]

# Dyanic generate image text content
image_content = [
    {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
        }
    }
    for base64_image in base64_images
]

# API request to identify the object and try to calate the price,
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "You are a cashier. Calculate the total price for the items in the image."
                },
                {
                    "type": "text",
                    "text": "Identify known/unknown items and sum the total."
                },
                *image_content  
            ]
        }
    ],
    max_tokens=100,
)

# Output the response from the API
print(response.choices[0])

