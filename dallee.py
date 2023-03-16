import openai
from config import openai_api_key
#from bot import prompt

openai.api_key = openai_api_key

prompt = []


# Generate an image
def get_Image(prompt):
    response = openai.Image.create(
        prompt=str(prompt),
        model="image-alpha-001",
        size="1024x1024",
        response_format="url")
    return response["data"][0]["url"]

