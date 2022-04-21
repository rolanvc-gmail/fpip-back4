from django.http import JsonResponse


def hello (request):
    response = {"hello": "world"}
    return JsonResponse(response)
