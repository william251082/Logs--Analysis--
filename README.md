# Logs analysis

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, this code will answer questions about the site's user activity.

The program will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

This code will analyze data from the logs of a web service to answer questions using advanced SQL queries.
Thes are the 3 questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Files

* newsdata.sql
* newsdata.py
* vagrant file
* readme.md


## Directions

1. You will need a virtual machine on your computer directory. Here is [a link](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0) on how to install it. 

2. Load the file newsdata.sql to build the reporting tool, you'll need to load the site's data into your local database. 
To load the data, use the command psql -d news -f newsdata.sql.
Here's what this command does:
psql — the PostgreSQL command line program
-d news — connect to the database named news which has been set up for you
-f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

3. There is a view called Q1 that has the answer to the first question.
		Q1 query:
			news=> create view Q1 as select articles.title, count (*) as views from articles join log on articles.slug = (regexp_split_to_array(path, E'/article/'))[2] where path != '/' group by (regexp_split_to_array(path, E'/article/'))[2], articles.title order by views desc limit 3;
		CREATE VIEW

4. Views for the second question:
		titleViews - has the titles and total views of all articles.
		query:
			news=> create view titleViews as select articles.title, count (*) as views from articles join log on articles.slug = (regexp_split_to_array(path, E'/article/'))[2] where path != '/' group by (regexp_split_to_array(path, E'/article/'))[2], articles.title order by views desc;
			CREATE VIEW

		NiAt - a view consisting of columns name, id, author and title.
		query: 
			news=> create view NiAt as select authors.name, authors.id, articles.author, articles.title from authors, articles where authors.id = articles.author order by id desc;
			CREATE VIEW

		NameViews - a view joining NiAt and title views.
		query:
			create view nameViews as select NiAt.name, titleViews.views from NiAt join titleViews on NiAt.title = titleViews.title group by NiAt.name, titleViews.views order by NiAt.name;
			CREATE VIEW

		descViews - a summed up views and group by name.
			query:
			create view descViews as select nameViews.name, sum(views) as views from nameViews group by nameViews.name;
			CREATE VIEW
			
5. Views for the third question.
		timeRqst - date and summed up requests
		query:
		news=> create view timeRqst as select time ::timestamp::date, count (*) as rqst from log group by time ::timestamp::date;
		CREATE VIEW

		timeStat - time and status column
		query:
		news=> create view timeStat as select time ::timestamp::date, status from log;
		CREATE VIEW

		time404 - dates and failed request view
		query:
		news=> create view time404 as select timeRqst.time, timeStat.status from timeRqst join timeStat on timeRqst.time = timeStat.time where status = '404 NOT FOUND';
		CREATE VIEW

		rnum404 - summed up failed request
		query:
		news=> create view rnum404 as select time, count (*) as num404 from time404 group by time;
		CREATE VIEW

		tQ3 - is the time and percent table
		query:
		news=> create view tQ3 as select timeRqst.time, cast (rnum404.num404 as float) / cast(timeRqst.rqst as float)* 100 as percent from timeRqst join rnum404 on timeRqst.time = rnum404.time;
		CREATE VIEW

6. On your virtual machine, run:
		news ==> python.newsdata.py
# LogsAnalysis
# LogsAnalysis
# LogsAnalysis
# LogsAnalysis
# LogsAnalysis
# Logs_Analysis
# Logs_Analysis
# Logs_Analysis
# LogsAnalysis
# LogsAnalysis
# LogsAnalysis
# Logs--Analysis--
