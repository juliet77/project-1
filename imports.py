import psycopg2
conn = psycopg2.connect ("https://git.heroku.com/postgelsql.git")
cur = conn.cursor()
with open('books.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'users', sep=',')

conn.commit()
