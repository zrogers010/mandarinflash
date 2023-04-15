from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.http import require_GET
from .models import Word, Vocab
import random


def home(request):
    return render(request, 'website/home.html', {})


@require_GET
def search(request):
    query = request.GET.get('q', '')
    results = Vocab.objects.filter(Q(pinyin3__icontains=query) | Q(english1__icontains=query)).values()#[:10]
    html = render(request, 'website/search_results.html', {'results': results}).content.decode('utf-8')

    return JsonResponse({'html': html})


def character(request, char):
    word = Vocab.objects.filter(simplified=char).first()
    context = {
        'character': char,
        'word': word
    }

    return render(request, 'website/character.html', context)


def character_search(request):
    return render(request, 'website/character_search.html')


def dictionary(request):
    return render(request, 'website/dictionary.html', {})


def flashcards(request, level):
    words = list(Vocab.objects.filter(hsk_level=level).values())
    # print("WORDS: ", words[:5])
    words = sorted(words, key=lambda k: random.random())
    
    for word in words[:5]:
        ans = generate_answers(level, word)
        ans = random.sample(ans, k=len(ans))
        word["answer1"] = ans[0]
        word["answer2"] = ans[1]
        word["answer3"] = ans[2]
        word["answer4"] = ans[3]

    context = {
        'words': words[:5],
        'english': [word["english1"], word["english2"], word["english3"]],
        'level': level
    }

    return render(request, 'website/hsk_flashcards.html', context)



# Shuffles flashcards for new quiz
def new_flashcard_words(request, level):
    words = list(Vocab.objects.filter(hsk_level=level).values())
    words = sorted(words, key=lambda k: random.random())

    for word in words[:5]:
        ans = generate_answers(level, word)
        ans = random.sample(ans, k=len(ans))
        word["answer1"] = ans[0]
        word["answer2"] = ans[1]
        word["answer3"] = ans[2]
        word["answer4"] = ans[3]

    response_data = {
        'words': words[:5],
    }

    return JsonResponse(response_data)

def wordslist(request, level):
    words = Vocab.objects.filter(hsk_level=level).order_by('id').values()
    context = {
        'words': words,
        'level': level
    }
    
    return render(request, 'website/hsk_wordlist.html', context)


def generate_answers(level, word):
    word_list = Vocab.objects.filter(~Q(simplified=word) & Q(hsk_level=level)).values()
    word_list = sorted(word_list, key=lambda k: random.random())

    answer_list = []
    answer_list.append((word['simplified'], word['english1']))
    answer_list.append((word_list[0]['simplified'], word_list[0]['english1']))
    answer_list.append((word_list[1]['simplified'], word_list[1]['english1']))
    answer_list.append((word_list[2]['simplified'], word_list[2]['english1']))

    return(answer_list)
