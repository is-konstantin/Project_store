"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from book import views
from cart import urls as cart_urls
from order import urls as order_urls
from cart import views as cart_views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('main/')
    #path('authors/', views.authors_list, name = "authors-list"),
    path('authors/', views.AuthorsList.as_view() , name = "authors-list_cbv"),
    #path('authors/<int:pk>/', views.authors_detail, name = "author-detail"),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name = "author-detail_cbv"),
    #path('authors-delete/<int:pk>/', views.authors_delete, name = "author-delete"),
    path('authors-delete/<int:pk>/', views.AuthorDelete.as_view() , name = "author-delete_cbv"),
    path('author-create/', views.AuthorCreate.as_view(), name = "author-create_cbv"),
    path('author-update/<int:pk>/', views.AuthorUpdate.as_view(), name = "author-update_cbv"),
### Series
    path('series/', views.SeriesList.as_view() , name = "series-list"),
    path('series/<int:pk>/', views.SeriesDetail.as_view(), name = "series-detail"),
    path('series_delete/<int:pk>/', views.SeriesDelete.as_view() , name = "series-delete"),
    path('series-create/', views.SeriesCreate.as_view(), name = "series-create"),
    path('series-update/<int:pk>/', views.SeriesUpdate.as_view(), name = "series-update"),

### Genre
    path('genre/', views.GenreList.as_view() , name = "genre-list"),
    path('genre/<int:pk>/', views.GenreDetail.as_view(), name = "genre-detail"),
    path('genre_delete/<int:pk>/', views.GenreDelete.as_view() , name = "genre-delete"),
    path('genre-create/', views.GenreCreate.as_view(), name = "genre-create"),
    path('genre-update/<int:pk>/', views.GenreUpdate.as_view(), name = "genre-update"),

### Publishing_house
    path('publishing_house/', views.Publishing_houseList.as_view() , name = "publishing_house-list"),
    path('publishing_house/<int:pk>/', views.Publishing_houseDetail.as_view(), name = "publishing_house-detail"),
    path('publishing_house_delete/<int:pk>/', views.Publishing_houseDelete.as_view() , name = "publishing_house-delete"),
    path('publishing_house-create/', views.Publishing_houseCreate.as_view(), name = "publishing_house-create"),
    path('publishing_house-update/<int:pk>/', views.Publishing_houseUpdate.as_view(), name = "publishing_house-update"),

### Book
    #path('book/', views.Publishing_houseList.as_view() , name = "book-list"),
    #path('book/<int:pk>/', views.Publishing_houseDetail.as_view(), name = "book-detail"),
    
    #path('order/', include(order_urls, namespace="order")),
    path('order/', include(order_urls, namespace='order')),
    path('cart/', include(cart_urls, namespace="cart")),
    path('', views.HomePage.as_view(), name = "Home-page"),

]


