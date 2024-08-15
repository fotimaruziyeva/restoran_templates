from django.urls import path
from .views import home_view,ContactListView,MenuListView,ServiceListView,AboutListView

urlpatterns = [
    path('', home_view, name="home-page"),
    path('about/',AboutListView.as_view(), name="about-page"),
    path('contact/',ContactListView.as_view(),name='contact-page'),
    path('menu/',MenuListView.as_view(),name='menu-page'),
     path('service/',ServiceListView.as_view(),name='service-page'),
]
