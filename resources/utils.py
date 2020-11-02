def get_one_bar_plot_data():
    import json
    single_bar_chart_data = {
        "labels": ["Sun", "Mon", "Tu", "Wed", "Th", "Fri", "Sat"],
	"datasets"=[{        

		"data": [40, 55, 75, 81, 56, 55, 40],
		"name": "Single Bar Chart",
		"borderColor": "rgba(0, 123, 255, 0.9)",
		"border_width": "0",
		"backgroundColor": "rgba(0, 123, 255, 0.5)"
	}
	]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': 'Title'
    }


def get_two_bar_plot_data():
    import json
    multi_bar_plot_data = {
        "labels": ["January", "February", "March", "April", "May", "June",
                   "July"],
        "datasets": [
            {
                "label": "My First dataset",
                "data": [65, 59, 80, 81, 56, 55, 40],
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "fontFamily": "Poppins"
            },
            {
                "label": "My Second dataset",
                "data": [28, 48, 40, 19, 86, 27, 90],
                "borderColor": "rgba(0,0,0,0.09)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0,0,0,0.07)",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title': 'Title'
    }


def get_multi_line_plot_data():
    import json
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
    area_plot_data = {
        "labels": ["2010", "2011", "2012", "2013", "2014", "2015", "2016"],
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "data": [0, 7, 3, 5, 2, 10, 7],
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
        'area_plot_data_one_title': 'Title'
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
    doughnut_graph_data = {
        "datasets": [{
            "data": [45, 25, 20, 10],
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
        "labels": [
            "Green1",
            "Green2",
            "Green3",
            "Green4"
        ]
    }

    return {
        'doughnut_graph_data_one': json.dumps(doughnut_graph_data),
        'doughnut_graph_data_one_title': 'Title'
    }


def get_multi_line_plot_with_area_data():
    import json
    multi_line_plot_with_area_data = {
        "labels": [
            "January", "February", "March", "April", "May", "June",
            "July"],
        "defaultFontFamily": "Poppins",
        "datasets": [
            {
                "label": "My First dataset",
                "borderColor": "rgba(0,0,0,.09)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0,0,0,.07)",
                "data": [22, 44, 67, 43, 76, 45, 12]
            },
            {
                "label": "My Second dataset",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "pointHighlightStroke": "rgba(26,179,148,1)",
                "data": [16, 32, 18, 26, 42, 33, 44]
            }
        ]
    }

    return {
        'multi_line_plot_with_area_data_one': json.dumps(
            multi_line_plot_with_area_data),
        'multi_line_plot_with_area_data_one_title': 'Title'
    }


def get_pie_chart_data():
    import json

    pie_chart_data = {
        "datasets": [{
            "data": [45, 25, 20, 10],
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
        "labels": [
            "Green",
            "Green",
            "Green"
        ]
    }

    return {
        'pie_chart_data_one': json.dumps(
            pie_chart_data),
        'pie_chart_data_one_title': 'Title'
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
