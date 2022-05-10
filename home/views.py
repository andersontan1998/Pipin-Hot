from django.shortcuts import render

# Create your views here.
def defaultHome(request):
    return render(request, 'index.html')