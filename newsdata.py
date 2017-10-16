#! /usr/bin/env python
import psycopg2

DBNAME = "news"

# Database code to connect to newsdata.sql.
def execute_query(query):
    """execute_query takes an SQL query as a parameter.
    Executes the query and returns the results as a list of tuples."""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if c is not None:
            db.close()


# Fetch some records from the database.
def question_1():
    """ This function fetch a postgreSQl query to answer question
    1. What are the most popular three articles of all time?"""
    query = "select * from Q1;"
    rows = execute_query(query)
    print("The Top Three Articles are: ")
    for row in rows:
        print("\"{}\" -- {} views").format(row[0], row[1])
    print("\n")


def question_2():
    """ This function fetch a postgreSQl query to answer question
    2. Who are the most popular article authors of all time?"""
    query = "select name, views from descViews order by views desc;"
    rows = execute_query(query)
    print("The Top Article Authors are: ")
    for row in rows:
        print("\"{}\" -- {} views").format(row[0], row[1])
    print("\n")


def question_3():
    """ This function fetch a postgreSQl query to answer question
    3. On which days did more than 1% of requests lead to errors? """
    query = "select time, percent from tQ3 where percent > 1.0;"
    # percent column is divided by 100 in tQ3
    rows = execute_query(query)
    print("Days with more than 1 percent error is ")
    for row in rows:
        print("\"{}\" -- {} percent").format(row[0], row[1])
    print("\n")


if __name__ == '__main__':
    question_1()
    question_2()
    question_3()
