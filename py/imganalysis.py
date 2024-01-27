secret_key = "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"
secret_key = "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"
from openai import OpenAI
import base64
import requests

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


client = OpenAI(api_key = secret_key)

image_path = "../test_imgs/ex.png"
base64_image = encode_image(image_path)


response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Do not include any explanation. Only extract the text in this image in latex format."},
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])