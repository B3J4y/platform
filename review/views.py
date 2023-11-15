from django.shortcuts import render


# Create your views here.
def index(request):
    input_data = {'text': 'Hello, Viewer.'}
    return render(request, "review.html", {"data": input_data})
