from django.http import HttpResponse
from django.shortcuts import render

data = {
    'sample' : [
        {
            'id' : 5, 
            'title' : 'Jaws',
            'year' : 1969
        },
        {
            'id' : 6, 
            'title' : 'Shaknado',
            'year' : 1600
        },
        {
            'id' : 7, 
            'title' : 'The Meg',
            'year' : 2000
        },
    ]
}

def sample(request):
    return render(request, 'sample/sample.html', data)

def home(request):
    return HttpResponse('Home')