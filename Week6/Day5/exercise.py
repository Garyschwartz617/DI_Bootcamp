import psycopg2   # importing a module to connect to postgres
import psycopg2.extras
from pprint import pprint
import json

def show_user_menu():
    while True:
        print('''MENU
        (a) Add an item
        (d) Delete an item
        (v) View the menu
        (x) Exit
        ''')
        user_input = input('WHAT WOULD YOU LIKE TO DO? ')
        if user_input == 'x':
            show_restaurant_menu()
            print('good by!!!!')
            break
        elif user_input == 'a':
            add_item_to_menu() 
        elif  user_input == 'd':
            remove_item_from_menu()
        elif  user_input == 'v':
            show_restaurant_menu()
        else:
            print('not a valid input!!!!!!!!!!')    
                    

def load_manager():

    show_user_menu()


def add_item_to_menu():
    item = input('which item would you like to add? ')
    price = input('At what price? ')
    query = f"SELECT * FROM save_item ('{item}', '{price}')"
    execute(query)
    pass

def remove_item_from_menu():
    user_input = input('which item would you like to delete? ')
    query = f"SELECT * FROM delete_item ('{user_input}')"
    execute(query)
    pass

def show_restaurant_menu():
    # query = "SELECT * FROM item() AS (id int,name VARCHAR(50), price SMALLINT)"
    query = "SELECT name, price FROM MenuItem ORDER BY price"
    execute(query)
    

def execute(query):
     # defining our connection criteria
    HOSTNAME = 'localhost'
    USERNAME = 'garyschwartz'
    PASSWORD = 'letmein'
    DATABASE = 'restaurant'

    # making the connection to the database
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

    # accessing the query editor
    # cursor = connection.cursor()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(query)
    connection.commit()

# fetching the results
    results = cursor.fetchall()

# closing the connection
    connection.close()
    results =json.dumps(results)
    print(results.replace("\"", "").replace("[", "").replace("]", "").replace("{", "").replace("}, ", "\n").replace("}", ""))

load_manager()