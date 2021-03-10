from django.http import HttpResponse

def stocks(request):
    return HttpResponse("Hello, world. You're at the stocks index.")
