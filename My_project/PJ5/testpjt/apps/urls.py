from django.urls import path
from . import views

urlpatterns = [
    path('crawling/', views.crawling),
]
