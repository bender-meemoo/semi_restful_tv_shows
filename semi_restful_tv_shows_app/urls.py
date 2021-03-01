from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.shows),
    path('shows/new', views.showsnew),
    path('showscreate', views.showscreate),
    path('shows/<int:showID>/edit', views.showsedit),
    path('showsedited/<int:showID>', views.showsedited),
    path('shows/<int:showID>', views.showsshow),
    path('showsdelete/<int:showID>', views.showsdelete)
    
]