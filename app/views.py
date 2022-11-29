from django.shortcuts import render, redirect
from app.forms import AnimalsForm
from app.models import Animals
from django.core.paginator import Paginator


def home(request):
    #data = {}
    #data['database'] = Animals.objects.all()
    #return render(request, 'index.html', data)

    #Filtro procurar
    data = {}
    search = request.GET.get('search')
    if search:
        data['database'] = Animals.objects.filter(cpf__icontains=search)

    else:
        data['database'] = Animals.objects.all()

    return render(request, 'index.html', data)

# def home(request):
#     data = {}
#     all = Animals.objects.all()
#     paginator = Paginator(all, 2)
#     pages = request.GET.get('page')
#     data['database'] = paginator.get_page(pages)
#     return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = AnimalsForm()
    return render(request, 'form.html', data)

def create(request):
    form = AnimalsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def edit(request, pk):
    data = {}
    data['database'] = Animals.objects.get(pk=pk)
    data['form'] = AnimalsForm(instance=data['database'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['database'] = Animals.objects.get(pk=pk)
    form = AnimalsForm(request.POST or None, instance=data['database'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    database = Animals.objects.get(pk=pk)
    database.delete()
    return redirect('home')