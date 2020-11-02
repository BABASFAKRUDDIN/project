### Templates
Just the way we don't write new web application framework for our web application, Similarly for frontend we use templates

Make use of the below templates 
* Home Page -   `templates/base.html` & `templates/imdb_home.html`
* Movie Page -  `templates/imdb_movie.html`
* Actor Page -   `templates/imdb_actor.html`
* Director Page -   `templates/imdb_director.html`
* Analytics Page -  `templates/analytics_base.html` & `templates/analytics.html`

### Graphs
* Single Bar Plot
    * Refer to `utils.get_one_bar_plot_data` for sample data format
    * Your templates expect data in `single_bar_chart_data_one` key in context
    * You can pass title in `single_bar_chart_data_one_title` key in content
    * You template currently support maximum of 5 single bar plots. Refer to the below  
        * `single_bar_chart_data_one` & `single_bar_chart_data_one_title`
        * `single_bar_chart_data_two` & `single_bar_chart_data_two_title`
        * `single_bar_chart_data_three` & `single_bar_chart_data_three_title`
        * `single_bar_chart_data_four` & `single_bar_chart_data_four_title`
        * `single_bar_chart_data_five` & `single_bar_chart_data_five_title`
        
* Two Bar Plot
    * Refer to `utils.get_two_bar_plot_data` for sample data format
    * Your templates expect data in `multi_bar_plot_data_one` key in context
    * You can pass title in `multi_bar_plot_data_one_title` key in content
    * You template currently support maximum of 5 single bar plots. Refer to the below  
        * `multi_bar_plot_data_one` & `multi_bar_plot_data_one_title`
        * `multi_bar_plot_data_two` & `multi_bar_plot_data_two_title`
        * `multi_bar_plot_data_three` & `multi_bar_plot_data_three_title`
        * `multi_bar_plot_data_four` & `multi_bar_plot_data_four_title`
        * `multi_bar_plot_data_five` & `multi_bar_plot_data_five_title`
        
* Multi Line Plot
    * Refer to `utils.get_multi_line_plot_data` for sample data format
    * Your templates expect data in `multi_line_plot_data_one` key in context
    * You can pass title in `multi_line_plot_data_one_title` key in content
    * You template currently support maximum of 5 single bar plots. Refer to the below  
        * `multi_line_plot_data_one` & `multi_line_plot_data_one_title`
        * `multi_line_plot_data_two` & `multi_line_plot_data_two_title`
        * `multi_line_plot_data_three` & `multi_line_plot_data_three_title`
        * `multi_line_plot_data_four` & `multi_line_plot_data_four_title`
        * `multi_line_plot_data_five` & `multi_line_plot_data_five_title`

* Area Plot
    * Refer to `utils.get_area_plot_data` for sample data format
    * Your templates expect data in `area_plot_data_one` key in context
    * You can pass title in `area_plot_data_one_title` key in content
    * You template currently support maximum of 5 single bar plots. Refer to the below  
        * `area_plot_data_one` & `area_plot_data_one_title`
        * `area_plot_data_two` & `area_plot_data_two_title`
        * `area_plot_data_three` & `area_plot_data_three_title`
        * `area_plot_data_four` & `area_plot_data_four_title`
        * `area_plot_data_five` & `area_plot_data_five_title`


* MultiLine Area Plot
    * Refer to `utils.get_multi_line_plot_with_area_data` for sample data format
    * Your templates expect data in `multi_line_plot_with_area_data_one` key in context
    * You can pass title in `multi_line_plot_with_area_data_one_title` key in content
    * You template currently support maximum of 5 single bar plots. Refer to the below  
        * `multi_line_plot_with_area_data_one` & `multi_line_plot_with_area_data_one_title`
        * `multi_line_plot_with_area_data_two` & `multi_line_plot_with_area_data_two_title`
        * `multi_line_plot_with_area_data_three` & `multi_line_plot_with_area_data_three_title`
        * `multi_line_plot_with_area_data_four` & `multi_line_plot_with_area_data_four_title`
        * `multi_line_plot_with_area_data_five` & `multi_line_plot_with_area_data_five_title`

* Radar Chart
    * Refer to `utils.get_radar_chart_data` for sample data format
    * Your templates expect data in `radar_chart_data_one` key in context
    * You can pass title in `radar_chart_data_one_title` key in content
    * You template currently support maximum of 5 single bar plots. Refer to the below  
        * `radar_chart_data_one` & `radar_chart_data_one_title`
        * `radar_chart_data_two` & `radar_chart_data_two_title`
        * `radar_chart_data_three` & `radar_chart_data_three_title`
        * `radar_chart_data_four` & `radar_chart_data_four_title`
        * `radar_chart_data_five` & `radar_chart_data_five_title`


* Doughnut Chart
    * Refer to `utils.get_doughnut_chart_data` for sample data format
    * Your templates expect data in `doughnut_graph_data_one` key in context
    * You can pass title in `doughnut_graph_data_one_title` key in content
    * You template currently support maximum of 5 single bar plots. Refer to the below  
        * `doughnut_graph_data_one` & `doughnut_graph_data_one_title`
        * `doughnut_graph_data_two` & `doughnut_graph_data_two_title`
        * `doughnut_graph_data_three` & `doughnut_graph_data_three_title`
        * `doughnut_graph_data_four` & `doughnut_graph_data_four_title`
        * `doughnut_graph_data_five` & `doughnut_graph_data_five_title`

* Pie Chart
    * Refer to `utils.get_pie_chart_data` for sample data format
    * Your templates expect data in `pie_chart_data_one` key in context
    * You can pass title in `pie_chart_data_one_title` key in content
    * You template currently support maximum of 5 single bar plots. Refer to the below  
        * `pie_chart_data_one` & `pie_chart_data_one_title`
        * `pie_chart_data_two` & `pie_chart_data_two_title`
        * `pie_chart_data_three` & `pie_chart_data_three_title`
        * `pie_chart_data_four` & `pie_chart_data_four_title`
        * `pie_chart_data_five` & `pie_chart_data_five_title`

* Polar Chart
    * Refer to `utils.get_polar_chart_data` for sample data format
    * Your templates expect data in `polar_chart_data_one` key in context
    * You can pass title in `polar_chart_data_one_title` key in content
    * You template currently support maximum of 5 single bar plots. Refer to the below  
        * `polar_chart_data_one` & `polar_chart_data_one_title`
        * `polar_chart_data_two` & `polar_chart_data_two_title`
        * `polar_chart_data_three` & `polar_chart_data_three_title`
        * `polar_chart_data_four` & `polar_chart_data_four_title`
        * `polar_chart_data_five` & `polar_chart_data_five_title`


### Django Queries:
* Incase you want to write any custom sql for any visualization refer to `utils.execute_sql_query`

