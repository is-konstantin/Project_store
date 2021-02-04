from django.shortcuts import render
from django.http import HttpResponse

from book.models import Author

# Create your views here.
def home_page(request):
    author = Author.objects.first()
    contxt = {"author" : author}
    return render(request, template_name = "home.html", context = contxt)
    #html = "Authors: <br>"
    #for auth in authors:
    #    html += f"{auth.author_name} <br>"
    #return HttpResponse(html)