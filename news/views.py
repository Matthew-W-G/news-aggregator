from django.shortcuts import render
from django.views.generic import ListView
from .models import NewsPiece
from .models import HeadlineBasket
import json, requests
from newsapi.newsapi_client import NewsApiClient

class NewsPieceListView(ListView):
    newsapi = NewsApiClient(api_key='92c75fd3c7704a00b972bbc242b9907c')
    top_headlines = newsapi.get_top_headlines(
                                          language='en',
                                          country='us')


    headline_articles = HeadlineBasket(title="Headlines").save()


    for ar in top_headlines.get('articles'):
        NewsPiece(title=ar.get('title'),
                blurb=ar.get('description'),
                source=ar.get('source').get('name'),
                url=ar.get('url'),
                date=ar.get('publishedAt'),
                headline=headline_articles
                ).save()

    model = NewsPiece
    context_object_name = 'NewsPiece'






