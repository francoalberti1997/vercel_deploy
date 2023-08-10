from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Este es mi deploy en Vercel")