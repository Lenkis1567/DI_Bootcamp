from django.shortcuts import render
from .forms import CategoryForm, GifForm
from .models import Category, Gif
from django.http import HttpResponse

def add_gif_view(request):
    if request.method =='POST':
        gif_filled_form = GifForm(request.POST)

        if gif_filled_form.is_valid():
            new_gif = gif_filled_form.save()
            category=gif_filled_form.cleaned_data('categories')
            category_obj=Category.objects.get(name=category)
            new_gif.categories.add(category_obj)
            return HttpResponse('Success')
    
    if request.method =='GET':
        gif_form=GifForm()
        context={'form':gif_form}   

    return render(request, 'add_gif.html', context)

def add_category_view(request):
    if request.method =='POST':
        category_filled_form = CategoryForm(request.POST)
        if category_filled_form.is_valid():
            category_filled_form.save()
            return HttpResponse('Success')

    if request.method == 'GET':
        category_form=CategoryForm()
        context={'form': category_form}

    return render(request, 'add_category.html', context)

def gifs_view(request):
    gifs_all=Gif.objects.all()
    like_dislike_forms = [LikeForm(initial={'gif':gif_instance}) for gif_instance in gifs_all]
    