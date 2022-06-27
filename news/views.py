from django.views.generic import ListView
from .models import NewsPiece
from newsapi.newsapi_client import NewsApiClient
from datetime import datetime, timezone
from dateutil import parser
from news import news_logic
newsapi = NewsApiClient(api_key='92c75fd3c7704a00b972bbc242b9907c')


class HomeListView(ListView):
    news_logic.remove_outdated('Front page')

    new_front_headlines = newsapi.get_top_headlines(language='en', country='us').get('articles')

    news_logic.add_articles(new_front_headlines, 'Front page')

    queryset = NewsPiece.objects.filter(category = 'Front page')
    model = NewsPiece
    context_object_name = 'NewsPiece'



class PoliticsListView(ListView):
    news_logic.remove_outdated('Politics')

    new_politics_headlines = newsapi.get_everything(q='Biden Trump Senate Congress Obama Supreme Court D.C. Election'
                                                    , language='en').get('articles')

    news_logic.add_articles(new_politics_headlines, 'Politics')

    queryset = NewsPiece.objects.filter(category = 'Politics')
    model = NewsPiece
    context_object_name = 'NewsPiece'
    template_name = 'news/NewsPiece_list.html'


class BusinessListView(ListView):
    news_logic.remove_outdated('Business')

    new_front_headlines = newsapi.get_top_headlines(language='en', category='business', country='us').get('articles')

    news_logic.add_articles(new_front_headlines, 'Business')

    queryset = NewsPiece.objects.filter(category = 'Business')
    model = NewsPiece
    context_object_name = 'NewsPiece'
    model = NewsPiece

class WorldListView(ListView):
    news_logic.remove_outdated('World')
    for ar in NewsPiece.objects.filter(category = 'World'):
            ar.delete()

    countries = ['ru', 'gb', 'fr', 'au', 'ch','hk', 'br','tw','gr', 'nz', 'jp']
    for c in countries:
        new_world_headlines = newsapi.get_top_headlines(language='en', category='general', country=c, page=2).get('articles')
        news_logic.add_articles(new_world_headlines, 'World')

    queryset = NewsPiece.objects.filter(category = 'World')
    model = NewsPiece
    context_object_name = 'NewsPiece'
    model = NewsPiece

class EntertainmentListView(ListView):
    news_logic.remove_outdated('Entertainment')

    new_front_headlines = newsapi.get_top_headlines(language='en', category='entertainment', country='us').get('articles')

    news_logic.add_articles(new_front_headlines, 'Entertainment')

    queryset = NewsPiece.objects.filter(category = 'Entertainment')
    model = NewsPiece
    context_object_name = 'NewsPiece'
    model = NewsPiece

class OpinionListView(ListView):
    news_logic.remove_outdated('Opinion')

    new_politics_headlines = newsapi.get_everything(qintitle='Opinion', language='en').get('articles')

    news_logic.add_articles(new_politics_headlines, 'Opinion')

    queryset = NewsPiece.objects.filter(category = 'Opinion')
    model = NewsPiece
    context_object_name = 'NewsPiece'
    template_name = 'news/NewsPiece_list.html'

