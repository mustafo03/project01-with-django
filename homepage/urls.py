from django.urls import path
from .views import HomepageView,AboutPageView


urlpatterns = [
    path('',HomepageView.as_view(),name = 'index'),
    path('about/',AboutPageView.as_view(),name = 'about'),



]