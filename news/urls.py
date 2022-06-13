from django.urls import path
from .views import NewsPieceListView
from . import views

urlpatterns = [
    path('', NewsPieceListView.as_view(), name='news-home')
]