from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Word


@csrf_exempt
def get_word(request):
    if request.method == "GET":
        word = request.GET.get("word", False)

        if not word:
            return HttpResponseNotFound()

        word_object = list(Word.objects.filter(word=word).values())
        print(len(Word.objects.all()))

        if not word_object:
            return HttpResponseNotFound()

        return JsonResponse(word_object, safe=False,
                            json_dumps_params={'ensure_ascii': False})

    else:
        return HttpResponseNotFound()


@csrf_exempt
def set_word(request):
    if request.method == "POST":
        try:
            word = request.POST["word"]
            translation = request.POST["translation"]
            api = request.POST["api"]
        except KeyError:
            return HttpResponseNotFound()

        word_object = Word(word=word, translation=translation, api=api)
        word_object.save()

        return HttpResponse()


def count(request):
    if request.method == "GET":
        count = len(Word.objects.all())
        return JsonResponse({"count": count})


def show(request):
    answer = []
    for i, (id, word, translation, api) in enumerate(Word.objects.values_list(), 1):
        answer.append((i, word, translation[:10], api[:10]))

    return render(request, "db/show.html", {
            "objects": answer
        })
