from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'intro/index.html')

def team(request):
    return render(request, 'intro/team.html')

def publication(request):
    return render(request, 'intro/publication.html')

def caro(request):
    return render(request, 'intro/carousel.html')

def sect(request):
    return render(request, 'intro/section.html')

def test(request):
    return render(request, 'intro/test.html')

def research(request):
    return render(request, 'intro/research.html')


def team2(request):
    return render(request, 'intro/team2.html')

def gallery(request):
    return render(request, 'intro/gallery.html')

def error404(request):
    return render(request, 'intro/page-404.html')
