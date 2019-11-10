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

def battle(request):
    return render(request, 'home.html', {
        'title': 'Battle Page Title'
        }
    )


def moviedex(request):
    return render(request, 'home.html', {
        'title': 'Moviedex Page Title'
        }
    )


def details(request):
    return render(request, 'home.html', {
        'title': 'Details Page Title'
        }
    )

def options(request):
    return render(request, 'home.html', {
        'title': 'Options Page Title'
        }
    )


def save_game(request):
    return render(request, 'home.html', {
        'title': 'Save Game Page Title'
        }
    )

def load_game(request):
    return render(request, 'home.html', {
        'title': 'Load Game Page Title'
        }
    )
