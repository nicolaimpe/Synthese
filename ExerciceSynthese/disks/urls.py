from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_albums),
    path('album/<int:id>', views.view_album, name='show_tracks'),


]
