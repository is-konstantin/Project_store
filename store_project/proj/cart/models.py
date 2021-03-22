from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete = models.PROTECT,
        blank = False,
        null = True

    )
    @property
    def total_summ(self):
        all_books = self.books.all()
        total = 0
        for book in all_books:
            total += book.total_price
        return total

    def __str__(self):
        return f"cart #{self.pk} "

class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name = "Cart",
        related_name = "books",
        on_delete = models.CASCADE
    )
    book = models.ForeignKey(
        "book.Book",
        verbose_name = "Book in a cart",
        on_delete = models.PROTECT
    )

    quantity = models.IntegerField(
        "Quantity",
        default = 1
    )
    price = models.DecimalField(
        "Price",
        max_digits = 5,
        decimal_places = 2
    )

    def __str__(self):
        return f"BookInCart #{self.pk} {self.book.book_name} quantity {self.quantity}  price {self.price}" 

    @property
    def total_price(self):
        return self.book.book_price * self.quantity