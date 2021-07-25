from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('', Home.as_view(), name='HomePage'),
    path('about/', About.as_view(), name='AboutPage'),
    path('journal/', Journal.as_view(), name='JournalPage'),
    path('contact/', ContactPage.as_view(), name='ContactPage'),
    path('work/', Work.as_view(), name='WorkPage'),
]