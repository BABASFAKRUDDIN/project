from imdb.models import *

def actor_database():
    a=open('/home/rgukt/Desktop/complete_data/actors_5000.json','r')
    r=a.read()
    import json
    data=json.loads(r)
    for actor in data:
        Actor.objects.create(actor_id=actor["actor_id"],
        name=actor["name"],
        gender=actor['gender'],
        fb_likes=actor['fb_likes']
        )
def director_database():
    a=open('/home/rgukt/Desktop/complete_data/directors_5000.json','r')
    r=a.read()
    import json
    data=json.loads(r)
    for actor in data:
        Director.objects.create(name=actor["name"],
        gender=actor['gender'],
        no_of_facebook_likes=actor['no_of_facebook_likes']
        )
def movie_database():
    a=open('/home/rgukt/Desktop/complete_data/movies_5000.json','r')
    r=a.read()
    import json
    import random
    data=json.loads(r)
    for movies in data:
        Movie.objects.create(movie_id=movies['movie_id'],
        name=movies['name'],
        box_office_collection_in_crores=movies["box_office_collection_in_crores"],
        release_date=movies['release_date'],
        director=Director.objects.get(name=movies['director_name']),
        genre=random.choice(movies['genres']),
        no_of_users_voted=movies['no_of_users_voted'],
        language=movies['language'],
        average_rating=movies['average_rating'],
        fb_likes=movies['likes_on_fb']
        )
    
        for actor in movies['actors']:
            Cast.objects.create(actor=Actor.objects.get(actor_id=actor['actor_id']),
            movie=Movie.objects.get(movie_id=movies['movie_id']),
            is_debut_movie=actor['is_debut_movie'])



def execute_sql_query(sql_query):
    """
    Executes sql query and return data in the form of lists (
        This function is similar to what you have learnt earlier. Here we are
        using `cursor` from django instead of sqlite3 library
    )
    :param sql_query: a sql as string
    :return:
    """
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
    return rows



def get_one_bar_plot_data():
    import json
    collections_list=Movie.objects.values_list('box_office_collection_in_crores',flat=True)
    ids_list=Movie.objects.values_list('name',flat=True)
    data1=execute_sql_query("""
        select max(box_office_collection_in_crores) from imdb_movie group by release_date
    """)
    data2=execute_sql_query("""
        select strftime('%Y',release_date) from imdb_movie group by release_date
    """)



    single_bar_chart_data = {
        "labels": list(data2),
	    "datasets":[
        {        
		"data": list(data1),
		"name": "Single Bar Chart",
		"borderColor": "rgba(0, 123, 255, 0.9)",
		"border_width": "0",
		"backgroundColor": "rgba(0, 123, 255, 0.5)"
	    }
	]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': 'Year-Max_Collections'
    }

def get_two_bar_plot_data():
    import json
    import copy
    data1=execute_sql_query("""
    select strftime('%Y',m.release_date),gender,count(*) from imdb_movie as m,imdb_cast as c , imdb_actor as a where m.movie_id=c.movie_id and c.actor_id=a.actor_id  group by strftime('%Y',m.release_date),gender;
    """
    )
    data3=execute_sql_query("""
    select strftime('%Y',m.release_date) from imdb_movie as m,imdb_cast as c , imdb_actor as a where m.movie_id=c.movie_id and c.actor_id=a.actor_id  group by strftime('%Y',m.release_date);
    """
    )
    y={}
    g={'M':0,
    'F':0}
    for year in data3:
        y[year[0]]=copy.deepcopy(g)
    for year,gender,count in data1:
        if(gender == 'M'):
            y[year]['M']=copy.deepcopy(count)
        else:
             y[year]['F']=copy.deepcopy(count)
    l1=[]
    l2=[]
    for x in y.values():
        l1.append(x['M'])
        l2.append(x['F'])
    multi_bar_plot_data = {
        "labels":list(data3),
        "datasets": [
            {
                "label": "Male-Count",
                "data":l1 ,
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "fontFamily": "Poppins"
            },
            {
                "label": "Female-Count",
                "data":l2,
                "borderColor": "rgba(0,0,0,0.09)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0,0,0,0.07)",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title': 'Male-Female count vs Year'
    }


def get_multi_line_plot_data():
    import json
    data1=execute_sql_query("""
    select count(*) from imdb_movie as m,imdb_cast as c , imdb_actor as a where m.movie_id=c.movie_id and c.actor_id=a.actor_id and a.gender="M" group by strftime('%Y',m.release_date);
    """
    )
    data1=execute_sql_query("""
    select count(*) from imdb_movie as m,imdb_cast as c , imdb_actor as a where m.movie_id=c.movie_id and c.actor_id=a.actor_id and a.gender="M" group by strftime('%Y',m.release_date);
    """
    )
    data1=execute_sql_query("""
    select count(*) from imdb_movie as m,imdb_cast as c , imdb_actor as a where m.movie_id=c.movie_id and c.actor_id=a.actor_id and a.gender="M" group by strftime('%Y',m.release_date);
    """
    )
    data1=execute_sql_query("""
    select count(*) from imdb_movie as m,imdb_cast as c , imdb_actor as a where m.movie_id=c.movie_id and c.actor_id=a.actor_id and a.gender="M" group by strftime('%Y',m.release_date);
    """
    )
    multi_line_plot_data = {
        "labels": ["2010", "2011", "2012", "2013", "2014", "2015", "2016"],
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "label": "Foods",
            "data": [0, 30, 10, 120, 50, 63, 10],
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(220,53,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(220,53,69,0.75)',
        }, {
            "label": "Electronics",
            "data": [0, 50, 40, 80, 40, 79, 120],
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(40,167,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(40,167,69,0.75)',
        }]
    }
    return {
        'multi_line_plot_data_one': json.dumps(multi_line_plot_data),
        'multi_line_plot_data_one_title': 'Title'
    }


def get_area_plot_data():
    import json
    data1=execute_sql_query("""
    select strftime('%Y',m.release_date),count(*) from imdb_movie as m,imdb_director as d where d.id=m.director_id and d.id=1 group by strftime('%Y',m.release_date);
    """
    )
    l1=[]
    l2=[]
    for year,count in data1:
        l1.append(year)
        l2.append(count)
    area_plot_data = {
        "labels": l1,
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "data": l2,
            "label": "Expense",
            "backgroundColor": 'rgba(0,103,255,.15)',
            "borderColor": 'rgba(0,103,255,0.5)',
            "borderWidth": 3.5,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(0,103,255,0.5)',
        }, ]
    }
    return {
        'area_plot_data_one': json.dumps(area_plot_data),
        'area_plot_data_one_title': 'Director-Movies'
    }


def get_radar_chart_data():
    import json
    radar_chart_data = {
        "labels": [["Eating", "Dinner"], ["Drinking", "Water"], "Sleeping",
                   ["Designing", "Graphics"], "Coding", "Cycling", "Running"],
        "defaultFontFamily": 'Poppins',
        "datasets": [
            {
                "label": "My First dataset",
                "data": [65, 59, 66, 45, 56, 55, 40],
                "borderColor": "rgba(0, 123, 255, 0.6)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.4)"
            },
            {
                "label": "My Second dataset",
                "data": [28, 12, 40, 19, 63, 27, 87],
                "borderColor": "rgba(0, 123, 255, 0.7",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'radar_chart_data_one': json.dumps(radar_chart_data),
        'radar_chart_data_one_title': 'Title'
    }


def get_doughnut_chart_data():
    import json
    data1=execute_sql_query("""
        select genre,round((count(genre)*100.0/(select count(*) from imdb_movie)),3) from 
        imdb_movie group by genre
    """)
    genre=[]
    percentage=[]
    for i in data1:
        genre.append(i[0])
        percentage.append(i[1])
    doughnut_graph_data = {
        "datasets": [{
            "data":percentage,
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels":genre
    }

    return {
        'doughnut_graph_data_one': json.dumps(doughnut_graph_data),
        'doughnut_graph_data_one_title': 'Title'
    }


def get_multi_line_plot_with_area_data():
    import json
    import copy

    data1=execute_sql_query("""
    select strftime('%Y',release_date),result,count(*) from imdb_movie group by strftime('%Y',release_date),result;
    """
    )
    print(data1)
    y={}
    r={'Block Buster':0,
        'Average':0,
        'Disaster':0
    }
    data4=execute_sql_query("""
    select strftime('%Y',release_date) from imdb_movie group by strftime('%Y',release_date);
    """
    )
    for year in data4:
        y[year[0]]=copy.deepcopy(r)
    
    for i in data1:
        if(i[1] == 'Block Buster'):
            y[i[0]]['Block Buster']=copy.deepcopy(i[2])
        elif(i[1] == 'Average'):
             y[i[0]]['Average']=copy.deepcopy(i[2])
        else:
            y[i[0]]['Disaster']=copy.deepcopy(i[2])
    l1=[]
    l2=[]
    l3=[]
    for x in y.values():
        l1.append(x['Block Buster'])
        l2.append(x['Average'])
        l3.append(x['Disaster'])
    print(l1)
        

    multi_line_plot_with_area_data = {
        "labels": list(data4),
        "defaultFontFamily": "Poppins",
        "datasets": [
            {
                "label": "Block Buster",
                "borderColor": "rgba(0,0,0,.09)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0,0,0,.07)",
                "data":l1
            },
            {
                "label": "Average",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "pointHighlightStroke": "rgba(26,179,148,1)",
                "data":l2
            },
            {
                "label": "Disaster",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "pointHighlightStroke": "rgba(26,179,148,1)",
                "data": l3
            }
        ]
    }

    return {
        'multi_line_plot_with_area_data_one': json.dumps(
            multi_line_plot_with_area_data),
        'multi_line_plot_with_area_data_one_title': "Movie vs Result"
    }


def get_pie_chart_data():
    import json
    data1=execute_sql_query("""
    SELECT (count(gender)*100.0)/(select count(*) from imdb_actor) from imdb_actor group by gender;
    """
    )

    pie_chart_data = {
        "datasets": [{
            "data":list(data1),
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": [
            "Male",
            "Female"
        ]
    }

    return {
        'pie_chart_data_one': json.dumps(
            pie_chart_data),
        'pie_chart_data_one_title': 'Percentage of actors'
    }


def get_polar_chart_data():
    import json

    polar_chart_data = {
        "datasets": [{
            "data": [15, 18, 9, 6, 19],
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.8)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0,0,0,0.2)",
                "rgba(0, 123, 255,0.5)"
            ]

        }],
        "labels": [
            "Green1",
            "Green2",
            "Green3",
            "Green4",
            "Green5"
        ]
    }
    return {
        'polar_chart_data_one': json.dumps(
            polar_chart_data),
        'polar_chart_data_one_title': 'Title'
    }






'''from .utils import get_one_bar_plot_data,get_two_bar_plot_data,get_multi_line_plot_data,get_area_plot_data,get_radar_chart_data,get_doughnut_chart_data,get_multi_line_plot_with_area_data,get_pie_chart_data,get_polar_chart_data
    d1=get_one_bar_plot_data()
    d2=get_two_bar_plot_data()
    d3=get_multi_line_plot_data()
    d4=get_area_plot_data()
    d5=get_radar_chart_data()
    d6=get_doughnut_chart_data()
    d7=get_multi_line_plot_with_area_data()
    d8=get_pie_chart_data()
    d9=get_polar_chart_data()'''
