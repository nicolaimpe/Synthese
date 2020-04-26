from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('article/<int:id_article>', views.view_article, name='afficher_article'),
    path('articles/<int:year>/<int:month>', views.list_articles),
    path('redirection', views.view_redirection),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('', views.accueil, name='accueil'),
    path('article/<int:id>', views.lire, name='lire'),
    path('article/<int:id>-<slug:slug>$', views.lire, name='lire'),
]
