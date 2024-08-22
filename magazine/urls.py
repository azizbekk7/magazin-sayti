from django.urls import path

from .views import (
    HomeView, DetailPageView
)
urlpatterns = [
    path('', view=HomeView.as_view(), name='home_page'),
    path('magazine-detail/', view=DetailPageView.as_view(), name='detail_page')
]
