import openai
from config import telegram_token, openai_api_key
#from bot import messages

openai.api_key = "***"

prompt = "lego"


# Generate an image
def get_Image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        model="image-alpha-001",
        size="1024x1024",
        response_format="url")
    return response["data"][0]["url"]


#print(get_Image(prompt))
# Print the URL of the generated image
# print(response["data"][0]["url"])
