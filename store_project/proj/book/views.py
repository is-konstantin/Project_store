from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView, DeleteView, CreateView, UpdateView   

from book.models import Author

from . import forms

# Create your views here.
def authors_list(request):
    authors = Author.objects.all()
    contxt = {"authors" : authors}
    return render(request, template_name = "home.html", context = contxt)
    #html = "Authors: <br>"
    #for auth in authors:
    #    html += f"{auth.author_name} <br>"
    #return HttpResponse(html)

class AuthorsList(ListView):
    model = Author


def authors_detail(request, pk):
    author = Author.objects.get(pk=pk)
    contxt = {"object" : author}
    return render(request, template_name = "detail.html", context = contxt)

class AuthorDetail( DetailView ):
    model = Author


def authors_delete(request, pk):
    author = Author.objects.get(pk=pk)
    message = f'Author {author.author_name} has been deleted!'
    author.delete()
    contxt = {"message" : message}
    return render(request, template_name = "delete.html", context = contxt)

class AuthorDelete(DeleteView):
    success_url = '/authors-cbv/'
    model = Author

class AuthorCrate(CreateView):
    success_url = '/authors-cbv/'
    model = Author
    fields = ('author_name', 'author_description')

class AuthorUpdate(UpdateView):
    model = Author
    success_url = '/authors-cbv/'
    fields = ('author_name', 'author_description')  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            



