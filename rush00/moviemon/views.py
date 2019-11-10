from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html', {
        'title': 'Home Page Title'
        }
    )

def worldmap(request):
    return render(request, 'worldmap.html', {
        'title': 'Worldmap Page Title'
        }
    )

def battle(request):
    return render(request, 'battle.html', {
        'title': 'Battle Page Title'
        }
    )


def moviedex(request):
    return render(request, 'moviedex.html', {
        'title': 'Moviedex Page Title'
        }
    )


def details(request):
    return render(request, 'details.html', {
        'title': 'Details Page Title'
        }
    )

def options(request):
    return render(request, 'options.html', {
        'title': 'Options Page Title'
        }
    )


def save_game(request):
    return render(request, 'save_game.html', {
        'title': 'Save Game Page Title'
        }
    )

def load_game(request):
    return render(request, 'load_game.html', {
        'title': 'Load Game Page Title'
        }
    )

def move(request):
    print(request)
