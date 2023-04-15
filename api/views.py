import json
import re
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
    response = generation_pipeline(input_text, max_length=25, num_return_sequences=3, temperature=0.8, do_sample=True, top_k=50)
    best_response = choose_best_response(input_text, response)

    trimmed_response = trim_response(best_response["generated_text"])
    
    return trimmed_response

def trim_response(response_text):
    # Split the response text into sentences using a regular expression
    sentences = re.split('(?<=[。！？])', response_text)
    
    # Remove any empty sentences
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    # Reconstruct the response text with only complete sentences
    trimmed_text = ''.join(sentences)
    return trimmed_text
def choose_best_response(input_text, response_list):
    best_response = min(response_list, key=lambda x: len(x["generated_text"]))
    
    return best_response

    