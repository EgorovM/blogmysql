from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('edit_article/<int:id>', views.edit_article),
    path('add_article/', views.add_article),
    path('article_list/', views.article_list),
    path('article/<int:id>', views.article)
]
