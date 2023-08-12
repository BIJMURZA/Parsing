import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


connection = psycopg2.connect(dbname='games', user='baymurzaev',
                              password='1395', host='localhost')
cursor = connection.cursor()
cursor.execute('SELECT * FROM games')


for i in cursor.fetchall():
    print(i)

