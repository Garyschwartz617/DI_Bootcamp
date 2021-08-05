import sqlite3
import requests
import json
import random
from tabulate import tabulate


def create_table():
    connection = sqlite3.connect('countries.db', timeout=10)
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS countries")
   
    sql ='''CREATE TABLE countries(
    name VARCHAR (255),
    capital VARCHAR (255),
    flag VARCHAR (255),
    subregion VARCHAR (255),
    population INT 
    )'''
    cursor.execute(sql)
    connection.commit()
    

def show_results():
    connection = sqlite3.connect('countries.db')  #Make a connection to the database
    cursor = connection.cursor() #Think of the cursor as the place that executes queries
    query = "Select * FROM countries;"
    print(cursor.execute(query))  #Cursor runs the query   
    connection.commit()  #Finalize the result. "Write" it to the DB
    # print(results)
    connection.close()  #Close the connection

def get_inv():
    query = "SELECT * FROM countries;"
    return run_query(query)

def run_query(query):
    connection = sqlite3.connect("countries.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    results = cursor.fetchall()
    connection.close()
    return results

def start():
    create_table()

    for i in range(10):
        num = random.randint(1,250)
        url = 'https://restcountries.eu/rest/v2/all'
        data = requests.get(url)
        data = data.json()
        name = data[num]["name"]
        capital = data[num]["capital"]
        region = data[num]["region"]
        flag = data[num]["flag"]
        population = data[num]["population"]

        connection = sqlite3.connect('countries.db')  #Make a connection to the database
        cursor = connection.cursor() #Think of the cursor as the place that executes queries
        query = f"INSERT INTO countries (name,capital,flag,subregion,population) VALUES ('{name}','{capital}','{flag}','{region}','{population}');"
        cursor.execute(query)  #Cursor runs the query
        connection.commit()  #Finalize the result. "Write" it to the DB
        # results = cursor.fetchall() #Fetch theh results back from the cursor into python variable
        connection.close()  #Close the connection
    inv = get_inv()
    print(tabulate(inv, headers=['name', 'capital','flag','subregion','population']))   
   
start()




# url = 'https://restcountries.eu/rest/v2/all'
# data = requests.get(url)
# data = data.json()
# name = data[0]["name"]
# capital = data[0]["capital"]
# region = data[0]["region"]
# flag = data[0]["flag"]
# population = data[0]["population"]
# print(name)
# print(capital)
# print(region)
# print(flag)
# print(population)

# print(len(data))