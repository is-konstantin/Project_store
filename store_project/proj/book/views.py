from django.shortcuts import render
from django.http import HttpResponse

from book.models import Author

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

