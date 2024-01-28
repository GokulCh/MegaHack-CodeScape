from openai import OpenAI
import base64
import requests
import sys
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


client = OpenAI()

# image_path = "../test_imgs/ex2.png"
prog_lang = sys.argv[1];
image_path = sys.argv[2];
# base64_image = encode_image(image_path)


response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Do not include any explanation or any other irrelevant data. Convert the text in this image into syntactically correct "  + prog_lang + " as well as plaintext, separate these two forms with a newline of 6 hashtag symbols. For example if the text in an image is int i = 0; while i < 10; display(i) then you should output public class Example { public static void main(String[] args) { int i = 0; while (i <= 10) { display(i); i++; } } static void display(int value) { System.out.println(value); } }"},
        {
          "type": "image_url",
          "image_url": {
            "url": image_path,
          },
        },
      ],
    }
  ],
  max_tokens=600,
)

print(response.choices[0].message.content)
sys.stdout.flush()