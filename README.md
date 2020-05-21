# **WebCrawler project**

Simple python program, which crawls the web and records every unique visited url.

- Entry point of the program -> main.py
- Generates a database ('sites.db') with three tables -> urls, servers, domain
- If the program is terminated, it will start again from the last visited site.
- Run ./run_multiple_threads with different urls and it will crawl more things at the same time
- Visualizations available 
    -> run servers_visualization.py to get severs pie chart
    -> run user_analytics.py to get information about crawled domains
