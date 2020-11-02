from imdb.models import *
from django.urls import path
#from django.conf urls: urls ngs
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[

    path('',views.homepage,name='homepage'),
    path('home/',views.homepage,name='homepage'),
    path('actors/',views.actor,name='actor'),
    path('actor/<str:actor_id>/',views.actordetails,name='actordetails'),
    path('movie/<str:movie_id>/',views.moviedetails,name='moviedetails'),
    path('movies/',views.actor,name='actor'),
    path('director/<int:director_id>/',views.director,name='director'),
    path('analytics/',views.analytics,name='analytics')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


