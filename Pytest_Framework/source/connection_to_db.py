import psycopg2

hostname='localhost'
database='my_pgdb'
username='postgres'
pwd=''
port_id=5432

conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    password = pwd,
    port = port_id
)

print("Connected Successfully")
conn.close()