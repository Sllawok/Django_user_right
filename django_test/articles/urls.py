"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from articles import views


app_name = 'articles'

urlpatterns = [
    path('', views.main_page, name = 'index'),
    path('<int:id>/', views.article_description, name = 'article'),
    path('add/', views.article_add, name='article_add'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('tag-one/<int:pk>/', views.TagDetailView.as_view(), name='tag_one'),
    path('tag-update/<int:pk>/', views.TagUpdateView.as_view(), name='tag_update'),
    path('tag-delete/<int:pk>/', views.TagDeleteView.as_view(), name='tag_delete'),
    path('tag-create/', views.TagCreateView.as_view(), name='tag_create'),

]
