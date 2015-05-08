from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def index(request):
    # return HttpResponse("Welcome to Caregiver Response.")
    context_dict = {'boldmessage': "Connecting hearts and minds."}

    return render(request, 'care/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': ""}
    return render(request, 'care/about.html', context_dict)