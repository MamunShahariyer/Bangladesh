
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello WOrld !!")

def aboutUs(request):
    return HttpResponse("Shahariya Mamun !!")

def blogs(request,blogsid):
    return HttpResponse(blogsid)