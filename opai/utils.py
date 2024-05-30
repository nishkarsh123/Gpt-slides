from openai import OpenAI
from django.conf import settings
from django.http import JsonResponse
import json

API_KEY=settings.OPEN_AI_KEY
client = OpenAI(api_key=API_KEY)


def send_generation_request_to_gpt():
    if(API_KEY is not None):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
        {"role": "system", "content": "You are a helpful assistant that generates random jokes in JSON format with a title and the joke itself."},
        {"role": "user", "content": "Generate a random joke in JSON format with a title and joke."}
    ]
        )
        joke_response = response.choices[0].message.content
        joke_data = json.loads(joke_response)
        return joke_data