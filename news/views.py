from django.shortcuts import render
from django.views.generic import ListView
from .models import NewsPiece
from .models import HeadlineBasket
import json, requests
from newsapi.newsapi_client import NewsApiClient
from datetime import datetime, timezone
from dateutil import parser

newsapi = NewsApiClient(api_key='92c75fd3c7704a00b972bbc242b9907c')

class NewsPieceListView(ListView):
    top_headlines = newsapi.get_top_headlines(language='en', country='us')


    top_headline_articles = HeadlineBasket(title="Top Headlines")
    top_headline_articles.save()


    for ar in top_headlines.get('articles'):
        if ar.get('title') not in str(top_headline_articles.newspiece_set.all()):
            NewsPiece(title=ar.get('title'),
                    blurb=ar.get('description'),
                    source=ar.get('source').get('name'),
                    url=ar.get('url'),
                    date=ar.get('publishedAt'),
                    headline=top_headline_articles
                    ).save()


    for ar in top_headline_articles.newspiece_set.all():
        datetime_object = parser.parse(ar.date)
        time_since_publish = datetime.now(timezone.utc) - datetime_object
        if time_since_publish.days >= 1:
            ar.delete()


    queryset = top_headline_articles.newspiece_set.all()
    model = NewsPiece
    context_object_name = 'NewsPiece'



class EconomyListView(ListView):
    model = NewsPiece


class PoliticsListView(ListView):
    model = NewsPiece






