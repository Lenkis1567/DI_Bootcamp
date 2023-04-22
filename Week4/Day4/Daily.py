import requests
from random import choice
import psycopg2
url='https://restcountries.com/v3.1/all'


def get_data(url):
    response=requests.get(url)
    data=response.json()
    return data
def get_random_instance(data_list: list, n:int):
    instances=[]
    for _ in range(n):
        random_list=choice(data_list)
        instances.append(random_list)
    return instances
def extract(instance: dict):
    try:
        name=instance['name']['common']
        capital=instance['capital'][0]
        flag=instance['flag']
        return name, capital, flag
    except KeyError:
        return None

def prepocess(instances: list|dict):
    preprocessed=[]
    for instance in instances:
        preprocessed_inst=extract(instance)
        preprocessed.append(preprocessed_inst)
    return preprocessed

    
data=get_data(url)
random_inst=get_random_instance(data, 10)
clean_inst=prepocess(random_inst)
print(clean_inst)

HOSTNAME='localhost'
USERNAME='postgres'
PASSWORD='220879'
DATABASE='Countries'

connection=psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
def insert_query(columns_names: tuple[str], data:tuple, table_name:str)->str:
    columns=", ".join(columns_names)
    name, capital, flag = data
    query=f"insert into {table_name}' ({columns}) values ('{name}', '{capital}', '{flag}')" 
    return query
columns=['name', 'capital', 'flag']

def run_change_query(query:str):

q=insert_query(columns_names=columns, data=clean_inst, table_name='countries')
print(q)


===================
HOSTNAME = 'localhost'
USERNAME = 'yussiroz' 
PASSWORD = 'cluster'
DATABASE = 'countries'


connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)


def insert_query(columns_names: list[str], data: tuple, table_name:str) -> str:
    columns = ", ".join(columns_names)
    name, capital, flag_emoji, flag_url, subregion, population = data
    query = f"insert into {table_name} ({columns}) values ('{name}', '{capital}', '{flag_emoji}', '{flag_url}', '{subregion}', {population})"

    return query

columns = ['name', 'capital', 'flag_emoji', 'flag_url', 'subregion', 'population']

def run_change_query(query: str): 
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()
        print("SUCCESS")




url = 'https://restcountries.com/v3.1/all'

data = get_data(url)
random_inst = get_random_instances(data, 10)
clean_instances = preprocess(random_inst)


for clean_inst in clean_instances:
    q = insert_query(columns_names=columns, data=clean_inst, table_name='countries')
    run_change_query(q)