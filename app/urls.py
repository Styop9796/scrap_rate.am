from django.urls import path,include
from .views import scrap
urlpatterns = [
    path('',scrap)
]
