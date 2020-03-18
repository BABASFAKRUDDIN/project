from django.shortcuts import render
from .models import *
# Create your views here.
def get_average_rating_of_movie(movie_obj):
    try:
        r=Rating.objects.get(movie=movie_obj)
        n=1.0*(r.rating_one_count)+2*(r.rating_two_count)+3*(r.rating_three_count) + 4*(r.rating_four_count) + 5*(r.rating_five_count)
        s=r.rating_one_count+r.rating_two_count + r.rating_three_count  + r.rating_four_count + r.rating_five_count
        if(s==0):
            return 0
        return n/s
    except Rating.DoesNotExist:
        return 0

def actordetails(request,actor_id):
    all_actors=Actor.objects.get(actor_id=actor_id)
    movies=Movie.objects.filter(actors=actor_id)
    rating=[]
    for movie in movies:
        rating.append([movie,round(get_average_rating_of_movie(movie),3)])
    return render(request,'imdb_actor.html',{'all_actors':all_actors,'movies':rating})

def moviedetails(request,movie_id):
    movie=Movie.objects.get(movie_id=movie_id)
    all_actors= Movie.objects.get(movie_id=movie_id).actors.all()
    return render(request,'imdb_movie.html',{'all_actors':all_actors,'movie':movie})

def homepage(request):
    all_movies=Movie.objects.all()
    context={'all_movies':all_movies}
    rating=[]
    for movie in all_movies:
        rating.append([movie,round(get_average_rating_of_movie(movie),3)])
    return render(request,'imdb_home.html',{'all_movies':rating})
def movie(request):
    return render(request,'imdb_movie.html')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
def actor(request):
    all_actors=Actor.objects.all()
    context={'all_actors':all_actors}
    return render(request,'imdb_actor.html',context)
def director(request,director_id):
    directors=Director.objects.get(id=director_id)
    dir=Movie.objects.filter(director=director_id)
    return render(request,'imdb_director.html',{'dir':dir,'directors':directors})



def get_polar_chart_data():
    import json
    from imdb.models import Movie
    collections_list=Movie.objects.values_list('box_office_collection_in_crores',flat=True)
    ids_list=Movie.objects.values_list('name',flat=True)
    #print(collections_list)
    polar_chart_data = {
        "datasets": [{
            "data": list(collections_list),
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.8)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0,0,0,0.7)",
                "rgba(0, 123, 255,0.5)"
            ]

        }],
        "labels":list(ids_list)
    }
    return {
        'polar_chart_data_one': json.dumps(
            polar_chart_data),
        'polar_chart_data_one_title': 'Collections'
    }



def analytics(request):
    import json
    from .utils import get_one_bar_plot_data,get_two_bar_plot_data,get_multi_line_plot_data,get_area_plot_data,get_radar_chart_data,get_doughnut_chart_data,get_multi_line_plot_with_area_data,get_pie_chart_data,get_polar_chart_data,execute_sql_query
    
    
    d1=get_one_bar_plot_data()
    d2=get_two_bar_plot_data()
    d7=get_multi_line_plot_with_area_data()
    d4=get_area_plot_data()
    d8=get_pie_chart_data()
    d6=get_doughnut_chart_data()
    '''d3=get_multi_line_plot_data()
    
    d5=get_radar_chart_data()
    
    
    
    d9=get_polar_chart_data()
    data2=get_polar_chart_data()
    data1=get_doughnut_chart_data()
    data2.update(data1)'''
    for d in [d2,d7,d4,d8,d6]:
        d1.update(d)
    
    return render(request,'analytics.html',d1)

