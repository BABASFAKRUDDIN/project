
from django.shortcuts import render
from .models import *
# Create your views here

def actordetails(request,actor_id):
    all_actors=Actor.objects.get(actor_id=actor_id)
    movies=Movie.objects.filter(actors=actor_id)
    return render(request,'imdb_actor.html',{'all_actors':all_actors,'movies':movies})

def moviedetails(request,movie_id):
    movie=Movie.objects.get(movie_id=movie_id)
    all_actors= Movie.objects.get(movie_id=movie_id).actors.all()
    return render(request,'imdb_movie.html',{'all_actors':all_actors,'movie':movie})

def homepage(request):
    if(request.method=='POST'):
        a=request.POST['name']
       	Movie.objects.get(movie_id=a).delete()
    all_movies=Movie.objects.all()
    context={'all_movies':all_movies}
  
    return render(request,'imdb_home.html',{'all_movies':all_movies})
def movie(request):
    all_actors=Movie.objects.all()
    context={'all_movies':all_actors}
    return render(request,'imdb_actors.html',context)

    return render(request,'imdb_movie.html')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
def actor(request):
    all_actors=Actor.objects.all()
    context={'all_actors':all_actors}
    return render(request,'imdb_movies.html',context)
def director(request,director_id):
    directors=Director.objects.get(id=director_id)
    dir=Movie.objects.filter(director=director_id)
    return render(request,'imdb_director.html',{'dir':dir,'directors':directors})




def analytics(request):
    import json
    from .utils import get_one_bar_plot_data,get_two_bar_plot_data,get_multi_line_plot_data,get_area_plot_data,get_radar_chart_data,get_doughnut_chart_data,get_multi_line_plot_with_area_data,get_pie_chart_data,get_polar_chart_data,execute_sql_query
    
    
  
    d2=get_two_bar_plot_data()
    d7=get_multi_line_plot_with_area_data()
    d4=get_area_plot_data()
    d1=get_one_bar_plot_data()
    d8=get_pie_chart_data()
    #d6=get_doughnut_chart_data()
    #data2=get_polar_chart_data()
    '''d3=get_multi_line_plot_data()
    d5=get_radar_chart_data()
    d9=get_polar_chart_data()
    data1=get_doughnut_chart_data()
    data2.update(data1)'''
    for d in [d4,d2,d8,d7]:
        d1.update(d)
    
    return render(request,'analytics.html',d1)

