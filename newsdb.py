import psycopg2


# query 1
# sql query for 1. What are the most popular three articles of all time?
def get_articles():
    articles = get_query_results("select title, gets from author_gets limit 3")
    return articles


# query 2
#  sql query for 2. Who are the most popular article authors of all time?
def get_populr_authors():
    authors = get_query_results("select "
                                "authors.name as name , sum(author_gets.gets) as total from "
                                "author_gets join "
                                "authors on author_gets.author = authors.id "
                                "group by (authors.name,author_gets.author) "
                                "order by total desc")

    return authors


# query 3
# sql query for 3. On which days did more than 1% of requests lead to errors?
def request_errors():
    errors = get_query_results("select "
                               "n.dateonly as date, "
                               "round(cast "
                               "(float8 (cast (n.nf as float) * 100 / cast (t.nf as float) ) as numeric ) ,2) "
                               "as percentage "
                               "from not_founds n join "
                               "total_gets t  on n.dateonly = "
                               "t.dateonly where (cast (n.nf as float) )* 100 / cast (t.nf as float) > 1")
    return errors


# function to fetch the result set for sql queries
def get_query_results(query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result
