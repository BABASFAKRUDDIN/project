from imdb.models import *
from django.urls import path
#from django.conf urls: urls ngs
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[

    path('',views.homepage,name='homepage'),
    path('actor/',views.actor,name='homepage'),
    path('actor/<str:actor_id>/',views.actordetails,name='homepage'),
    path('movie/<str:movie_id>/',views.moviedetails,name='homepage'),
    path('movie/',views.movie,name='homepage'),
    path('director/<int:director_id>/',views.director,name='homepage'),
    path('analytics/',views.analytics,name='analytics')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)