from openai import OpenAI
from django.conf import settings
from django.http import JsonResponse
import json
import logging
import os
 
logger = logging.getLogger('opai')

API_KEY=settings.OPEN_AI_KEY
client = OpenAI(api_key=API_KEY)
DUMMY_JOKES= os.getenv("DUMMY_JOKES") in ["True", "true", True]

JOKE_DATA={"title": "Math Joke", "joke": "5 + 5 = 10"}
def send_generation_request_to_gpt():
    try:
        logger.info(f"Sending request to GPT: {str(API_KEY)}")
        if(not DUMMY_JOKES):
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
        else:
            return JOKE_DATA
    except Exception as e:
        logger.error(f"Error sending request to GPT: {str(e)}")