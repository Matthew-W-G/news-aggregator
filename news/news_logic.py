from .models import NewsPiece
from datetime import datetime, timezone
from dateutil import parser

def remove_outdated(cat):
    for ar in NewsPiece.objects.filter(category = cat):
        datetime_object = parser.parse(ar.date)
        time_since_publish = datetime.now(timezone.utc) - datetime_object
        if time_since_publish.days >= 1:
            ar.delete()

def add_articles(article_list, cat):
    for ar in article_list:
        if not NewsPiece.objects.filter(title = ar.get('title'), category = cat).exists():
            NewsPiece(title=ar.get('title'),
                    blurb=ar.get('description'),
                    source=ar.get('source').get('name'),
                    url=ar.get('url'),
                    date=ar.get('publishedAt'),
                    category=cat
                    ).save()