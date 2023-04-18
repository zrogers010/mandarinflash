import os
import json
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Set up OpenAI API credentials
openai.api_key = str(os.getenv('OPENAI_KEY'))

# Define function to generate chatbot response using OpenAI API
def generate_response(input_text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Conversation\nUser: 你好吗? I'm learning chinese, can you please help me practice some basic vocabulary words? I may say something in english, but you can response in english and chinese. Just keep the reponse short and fun, but try to help me learn. \nAI:早上好，今天我们将复习基本的汉语词汇 \nUser: {input_text}\nAI:",
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    bot_response = response.choices[0].text.strip()

    return bot_response

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('input', '')

        # Process user input and generate chatbot response
        bot_response = generate_response(user_input)

        return JsonResponse({'response': bot_response})

    return JsonResponse({'error': 'Invalid request'}, status=400)

