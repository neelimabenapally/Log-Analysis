## LOG ANALYSIS PROJECT

    This is a reporting tool designed to analyze the data

## Prerequisites:

    Python 2.x
    Vagrant VM
    Flask
    Psycopg2
    Postgresql

## Technical Details

    - Fork or download the repository and clone it on your computer
    - Move the repository folder into Vagrant folder
    - Install Vagrant (Virtual Machine)
    - cd into vagrant in the terminal(cd /path to vagrant)
    - use 'vagrant up' command to setup vagrant if not done
    - use 'vagrant ssh' command to open the ssh
    - cd into your repository folder(cd newsdata)
    - use 'psql -d news -f newsdata.sql' command to import the database
    - use 'python news.py' command to run the project
    - project runs on the localhost
    - Go to http://localhost:8000 on web browser to view the output

## Sql Queries for creating views

    - sql query to create view for query 1 and 2

        def view_articles_authors():
            db = psycopg2.connect(database="news")
            c = db.cursor()
            c.execute("create view author_gets as
                select articles.author, articles.title, count(log.method) as gets from log
                Join articles on log.path = concat('/article/', articles.slug)
                group by log.path, articles.title,articles.author order by gets desc;")
            db.commit()
            db.close()

    - sql query to create view for query 3

        def view_errors1():
            db = psycopg2.connect(database=DBNAME)
            c = db.cursor()
            c.execute("create view not_founds as
                select count(status) as nf , date(time) as dateonly  from log
                where status LIKE '404 NOT FOUND'
                group by dateonly
                order by dateonly asc")
            db.commit()
            db.close()

    - sql query to create view for query 3

        def view_errors2():
            db = psycopg2.connect(database=DBNAME)
            c = db.cursor()
            c.execute("create view total_gets as
                select count(status) as nf , date(time) as dateonly  from log  
                group by dateonly order by dateonly asc")
            db.commit()
            db.close()
