from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView, TemplateView   

from book.models import Author
from book.models import Series
from book.models import Genre
from book.models import Publishing_house
from book.models import Book

from . import forms

class HomePage(TemplateView):
    template_name = 'book/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.all().order_by("-pk")[:5]
        #context["authors"] = Author.objects.all().order_by("pk")[:3]
        return context


# Create your views here.
def authors_list(request):
    authors = Author.objects.all()
    contxt = {"authors" : authors}
    return render(request, template_name = "home.html", context = contxt)
    #html = "Authors: <br>"
    #for auth in authors:
    #    html += f"{auth.author_name} <br>"
    #return HttpResponse(html)
    


def authors_detail(request, pk):
    author = Author.objects.get(pk=pk)
    contxt = {"object" : author}
    return render(request, template_name = "detail.html", context = contxt)




def authors_delete(request, pk):
    author = Author.objects.get(pk=pk)
    message = f'Author {author.author_name} has been deleted!'
    author.delete()
    contxt = {"message" : message}
    return render(request, template_name = "delete.html", context = contxt)

### Authors

class AuthorsList(ListView):
    model = Author

class AuthorDetail( DetailView ):
    model = Author

class AuthorDelete(DeleteView):
    success_url = '/authors/'
    model = Author

class AuthorCreate(CreateView):
    success_url = '/authors/'
    model = Author
    fields = ('author_name', 'author_description')

class AuthorUpdate(UpdateView):
    model = Author
    success_url = '/authors/'
    fields = ('author_name', 'author_description') 

#### Series

class SeriesList(ListView):
    model = Series

class SeriesDetail( DetailView ):
    model = Series

class SeriesDelete(DeleteView):
    success_url = '/series/'
    model = Series

class SeriesCreate(CreateView):
    success_url = '/series/'
    model = Series
    fields = ('series_name', 'series_description')

class SeriesUpdate(UpdateView):
    model = Series
    success_url = '/series/'
    fields = ('series_name', 'series_description')  

### Genres

class GenreList(ListView):
    model = Genre

class GenreDetail( DetailView ):
    model = Genre

class GenreDelete(DeleteView):
    success_url = '/genre/'
    model = Genre

class GenreCreate(CreateView):
    success_url = '/genre/'
    model = Genre
    fields = ('genre_name', 'genre_description')

class GenreUpdate(UpdateView):
    model = Genre
    success_url = '/genre/'
    fields = ('genre_name', 'genre_description')

### Publishing_house

class Publishing_houseList(ListView):
    model = Publishing_house

class Publishing_houseDetail( DetailView ):
    model = Publishing_house

class Publishing_houseDelete(DeleteView):
    success_url = '/publishing_house/'
    model = Publishing_house

class Publishing_houseCreate(CreateView):
    success_url = '/publishing_house/'
    model = Publishing_house
    fields = ('publishing_house_name', 'publishing_house_description')

class Publishing_houseUpdate(UpdateView):
    model = Publishing_house
    success_url = '/publishing_house/'
    fields = ('publishing_house_name', 'publishing_house_description')








