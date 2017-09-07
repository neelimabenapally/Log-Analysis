import psycopg2

DBNAME = "news"

# sql query to create view for query 1 and 2
def view_articles_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view author_gets as select articles.author, articles.title, count(log.method) as gets from log Join articles on slug = overlay(log.path placing '' from 1 for 9) where log.path ~ '^\/article\/.*' group by log.path, articles.title,articles.author order by gets desc")
    db.commit()
    db.close()

# sql query to create view for query 3
def view_errors1():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view not_founds as select count(status) as nf , date(time) as dateonly  from log where status LIKE '404 NOT FOUND' group by dateonly order by dateonly asc")
    db.commit()
    db.close()

# sql query to create view for query 3
def view_errors2():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("create view total_gets as select count(status) as nf , date(time) as dateonly  from log  group by dateonly order by dateonly asc")
    db.commit()
    db.close()

# query 1
# sql query for 1. What are the most popular three articles of all time?
def get_articles():
    db = psycopg2.connect(database=DBNAME)
    c =db.cursor()
    c.execute("select title, gets from author_gets limit 3")
    articles = c.fetchall()
    db.close()
    return articles

# query 2
# sql query for 2. Who are the most popular article authors of all time?
def get_populr_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select authors.name as name , sum(author_gets.gets) as total from author_gets join authors on author_gets.author = authors.id group by (authors.name,author_gets.author) order by total desc")
    authors = c.fetchall()
    db.close()
    return authors

# query 3
# sql query for 3. On which days did more than 1% of requests lead to errors?
def request_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select n.dateonly as date, round(cast (float8 (cast (n.nf as float) * 100 / cast (t.nf as float) ) as numeric ) ,2) as percentage from not_founds n join total_gets t  on n.dateonly = t.dateonly where (cast (n.nf as float) )* 100 / cast (t.nf as float) > 1")
    errors = c.fetchall()
    db.close()
    return errors