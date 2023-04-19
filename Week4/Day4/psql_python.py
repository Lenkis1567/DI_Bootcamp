import psycopg2

HOSTNAME='localhost'
USERNAME='postgres'
PASSWORD='220879'
DATABASE='Hollywood'
connection=psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
# cursor=connection.cursor()
query='select * from actors'
with connection.cursor() as cursor:
    cursor.execute(query)
    result=cursor.fetchall()
print(result)
def select_column(column_name:str, table_name:str)->str:
    query=f'select {column_name} from {table_name}'
    return query

def select_columns(columns: list[str], table_name: str)->str:
    tab=''
    for i in columns:
        tab=tab+i+", "
    tab=tab[0:-2]
    query= f'select {tab} from {table_name}'
    return query
query1=select_columns(["first_name", "last_name"], 'actors')
with connection.cursor() as cursor: 
    cursor.execute(query1)
    result=cursor.fetchall()