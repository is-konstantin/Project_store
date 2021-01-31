from django.contrib import admin

# Register your models here.
from . models import Author
from . models import Series
from . models import Genre
from . models import Publishing_house

admin.site.register(Author)

admin.site.register(Series)

admin.site.register(Genre)

admin.site.register(Publishing_house)



