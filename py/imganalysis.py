from openai import OpenAI
import base64
import requests
import sys

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')



# image_path = "../test_imgs/ex2.png"
# base64_image = encode_image(image_path)

def extracttext(img_url):
  client = OpenAI(api_key="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")
  response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
          {
      "role": "system",
      "content": "You will be provided with an image. The goal is to extract the text data from it, keep spaces and newlines but DO NOT KEEP the code block symbol ```. Do not include any explanations or any other irrelavant data. If the image does not contain text, return the word \"ERROR\""
    },
      {
        "role": "user",
        "content": [
          # {"type": "text", "text": "Do not include any explanation or any other irrelevant data. Convert the text in this image into syntactically correct "  + prog_lang + " as well as plaintext, separate these two forms with a newline of 6 hashtag symbols. For example if the text in an image is int i = 0; while i < 10; display(i) then you should output public class Example { public static void main(String[] args) { int i = 0; while (i <= 10) { display(i); i++; } } static void display(int value) { System.out.println(value); } }"},
          {
            "type": "image_url",
            "image_url": {
              "url": img_url,
            },
          },
        ],
      }
    ],
    max_tokens=600,
  )
  return response.choices[0].message.content

def checktext(text):
  client = OpenAI(api_key="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")
  response = client.chat.completions.create(
  model="gpt-4-turbo-preview",
  messages=[
    {
      "role": "system",
      "content": "You are checking a text input to see if it is pseudocode. Be lenient. If it is pseudocode then return \"true\" and only \"true\" otherwise return \"false\"."
    },
    {
      "role": "user",
      "content": text
    }
  ]
  # ,
  # temperature=1,
  # max_tokens=256,
  # top_p=1,
  # frequency_penalty=0,
  # presence_penalty=0
)
  return response.choices[0].message.content

def converttext(lang, text):
  client = OpenAI(api_key="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")
  response = client.chat.completions.create(
  model="gpt-4-turbo-preview",
  messages=[
    {
      "role": "system",
      "content": "You are converting the given text into "+lang+" make sure the code is functional and correct. DO NOT KEEP the code block symbol ```.For example if the text in an image is int i = 0; while i < 10; display(i) then you should output public class Example { public static void main(String[] args) { int i = 0; while (i <= 10) { display(i); i++; } } static void display(int value) { System.out.println(value); } }"
    },
    {
      "role": "user",
      "content": text
    }
  ]
)
  return response.choices[0].message.content

def main():
  method = sys.argv[1];
  if method == "extracttext":
    print(extracttext(sys.argv[2]))
  if method == "checktext":
    print(checktext(sys.argv[2]))
  if method == "x":
    print(checktext(extracttext(sys.argv[2])))
  if method == "y":
    print(converttext("java",extracttext(sys.argv[2])))
  sys.stdout.flush()

if __name__ == '__main__':
    main()
# response = client.chat.completions.create(
#   model="gpt-4-vision-preview",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {"type": "text", "text": "Do not include any explanation or any other irrelevant data. Convert the text in this image into syntactically correct "  + prog_lang + " as well as plaintext, separate these two forms with a newline of 6 hashtag symbols. For example if the text in an image is int i = 0; while i < 10; display(i) then you should output public class Example { public static void main(String[] args) { int i = 0; while (i <= 10) { display(i); i++; } } static void display(int value) { System.out.println(value); } }"},
#         {
#           "type": "image_url",
#           "image_url": {
#             "url": image_path,
#           },
#         },
#       ],
#     }
#   ],
#   max_tokens=600,
# )

