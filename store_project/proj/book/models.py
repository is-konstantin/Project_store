from django.db import models

# Create your models here.

class Author(models.Model):
    author_name = models.CharField("Name", max_length = 100)
    author_description = models.CharField("Description", max_length = 400)
    def __str__(self):
        return self.author_name

class Series(models.Model):
    series_name = models.CharField("Name", max_length = 100)
    series_description = models.CharField("Description", max_length = 400)
    def __str__(self):
        return self.series_name

class Genre(models.Model):
    genre_name = models.CharField("Name", max_length = 100)
    genre_description = models.CharField("Description", max_length = 400)
    def __str__(self):
        return self.genre_name

class Publishing_house(models.Model):
    publishing_house_name = models.CharField("Name", max_length = 100)
    publishing_house_description = models.CharField("Description", max_length = 400)
    def __str__(self):
        return self.publishing_house_name

class Book(models.Model):
    book_name = models.CharField("Name", max_length = 100)
    #book_picture = models.CharField("Picture", max_length = 100)
    book_price = models.DecimalField(
        "Price",
        max_digits = 5,
        decimal_places = 2
    )
    book_author = models.ForeignKey(Author,
        verbose_name = "Author",
        on_delete = models.CASCADE)

    book_series = models.ForeignKey(Series,
        verbose_name = "Series",
        on_delete = models.CASCADE
    )

    book_genre = models.ForeignKey(Genre,
        verbose_name = "Genre",
        on_delete = models.CASCADE
    )

    book_year_published = models.IntegerField("Year of publishing")
    book_pages = models.IntegerField("Numb of pages")
    book_binding = models.CharField("Binding", max_length = 50)
    book_format = models.CharField("Format", max_length = 50)
    book_isbn = models.CharField("ISBN", max_length = 50)
    book_weight = models.IntegerField("Weight")
    book_age_limit = models.CharField("Age limits", max_length = 30)

    book_publishing_house = models.ForeignKey(Publishing_house,
        verbose_name = "Publishing house",
        on_delete = models.CASCADE
    )
    book_quantity = models.IntegerField("Quantity")
    book_activity = models.CharField("Activity", max_length = 10)
    book_rating = models.IntegerField("Rating")
    book_entry = models.DateTimeField(auto_now_add=True)#, default = timezone.now)
    book_changes = models.DateField(auto_now=True)#, default = timezone.now)






    def __str__(self):
        return self.book_name



