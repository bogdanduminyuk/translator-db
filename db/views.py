from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
