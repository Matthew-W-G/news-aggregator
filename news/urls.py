from django.urls import path
from .views import HomeListView, PoliticsListView, BusinessListView, \
   WorldListView, EntertainmentListView, OpinionListView

urlpatterns = [
    path('', HomeListView.as_view(), name='news-home'),
    path('Politics/', PoliticsListView.as_view(), name='news-politics'),
    path('Business/', BusinessListView.as_view(), name='news-business'),
    path('World/', WorldListView.as_view(), name='news-world'),
    path('Entertainment/', EntertainmentListView.as_view(), name='news-entertainment'),
    path('Opinion/', OpinionListView.as_view(), name='news-opinion')
]




