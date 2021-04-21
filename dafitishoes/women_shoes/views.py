from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import WomenShoes
from .serializers import WomenShoesSerializer

@csrf_exempt
def women_shoes_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = WomenShoes.objects.all()
        serializer = WomenShoesSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = WomenShoesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def women_shoes_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = WomenShoes.objects.get(pk=pk)
    except WomenShoes.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = WomenShoesSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = WomenShoesSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
