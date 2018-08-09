from django.urls import path

from . import views

app_name = 'lunch_finder'
urlpatterns = [
    path('', views.IndexView.as_view(), name='Index'),
]
