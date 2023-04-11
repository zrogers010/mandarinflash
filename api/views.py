import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import GPT2LMHeadModel, BertTokenizer, TextGenerationPipeline

# Load pre-trained model and tokenizer
model_name = "uer/gpt2-chinese-cluecorpussmall"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Initialize the text generation pipeline
generation_pipeline = TextGenerationPipeline(model, tokenizer)

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get('input', '')

        # Process user input and generate chatbot response
        bot_response = generate_response(user_input)

        return JsonResponse({'response': bot_response})

    return JsonResponse({'error': 'Invalid request'}, status=400)

def generate_response(input_text):
    response = generation_pipeline(input_text, max_length=100, num_return_sequences=1)
    response_text = response[0]["generated_text"]
    return response_text