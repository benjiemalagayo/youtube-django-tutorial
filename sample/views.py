from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Sample

def sample(request):
    data = Sample.objects.all()
    return render(request, 'sample/sample.html', {'sample' : data})

def home(request):
    return HttpResponse('Home')

def detail(request, id):
    data = Sample.objects.get(pk=id)
    return render(request, 'sample/detail.html', {'sample' : data})

def add(request):
    title = request.POST.get('title')
    year = request.POST.get('year')
    
    if title and year:
        sample = Sample(title=title, year=year)
        sample.save()
        return HttpResponseRedirect('/sample')
    
    return render(request, 'sample/add.html')


def delete(request, id):
    try:
        sample = Sample.objects.get(pk=id)
    except:
        raise Http404('Sample does not exist')
    sample.delete()
    return HttpResponseRedirect('/sample')