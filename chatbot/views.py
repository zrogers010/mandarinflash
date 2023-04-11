from django.shortcuts import render

def chatbot(request):
    print("CHATBOT!!")
    return render(request, 'chatbot/chat.html', {})
