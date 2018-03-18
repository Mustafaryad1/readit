"""readit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from books.views import (list_books, AuthorList, AuthorDetail, CreateAuthor,
                         BookDetail, review_book, ReviewList)

urlpatterns = [
    # auth
    url(r'^logout/$', auth_views.logout, {'next_page': 'books'}, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
    # readit
    url(r'^authors/$', AuthorList.as_view(), name='authors'),
    url(r'^$', list_books, name='books'),
    url(r'^books/(?P<pk>[-\w]+)', BookDetail.as_view(), name='book-details'),
    url(r'^authors/add/$', login_required(CreateAuthor.as_view()), name='add-author'),
    url(r'^authors/(?P<pk>[-\w]+)', AuthorDetail.as_view(), name='author-details'),
    url(r'^review/(?P<pk>[-\w]+)/$', review_book, name='review-book'),
    url(r'^review/$', login_required(ReviewList.as_view()), name='review-books'),

]