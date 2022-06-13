from django.shortcuts import render
from django.views.generic import ListView
from .models import NewsPiece
import json, requests
from newsapi.newsapi_client import NewsApiClient

class NewsPieceListView(ListView):
    newsapi = NewsApiClient(api_key='92c75fd3c7704a00b972bbc242b9907c')
    top_headlines = newsapi.get_top_headlines(
                                          language='en',
                                          country='us')

    for ar in top_headlines.get('articles'):
        NewsPiece(title=ar.get('title'), blurb=ar.get('description'), source=ar.get('source').get('name')).save()
        #news2.title = ar['title']
        #news2.blurb = ar['description']
        #news2.source = ar['source']
        #news2.save()

    model = NewsPiece
    context_object_name = 'NewsPiece'

def gather_news():
    news1 = NewsPiece()
    news1.title = "Antarctica explodes"
    news1.blurb = "It was wild when it happened"
    news1.source = "The Onion"



