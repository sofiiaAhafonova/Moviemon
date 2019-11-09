from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {
        'title': 'Home Page Title'
        }
    )

def worldmap(request):
    return render(request, 'home.html', {
        'title': 'Worldmap Page Title'
        }
    )
