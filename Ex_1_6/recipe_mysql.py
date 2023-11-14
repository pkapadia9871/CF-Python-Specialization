print("Welcome to program!")

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

cursor.execute("USE task_database")

cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
                id                  INT PRIMARY KEY AUTO_INCREMENT,
                name                VARCHAR(50),
                ingredients         VARCHAR(255),
                cooking_time        INT,
                difficulty          VARCHAR(20)
            ) ''')

def main_menu(conn, cursor):

    print('enter something: ')

    your_choice = ''

    while your_choice != 'quit':
        print('Main Menu')
        print("=========")
        print("Pick a choice:")
        print("create_recipe")
        print("search_recipe")
        print("update_recipe")
        print("delete_recipe")
        print("Type quit to exit the program")
        your_choice = input("Your choice: ")

        if your_choice == '1':
            create_recipe(conn, cursor)
        if your_choice == '2':
            search_recipe(conn, cursor)
        if your_choice == '3':
            update_recipe(conn, cursor)
        if your_choice == '4':
            delete_recipe(conn, cursor)


def create_recipe(conn, cursor):
    print("create recipe: ")
    name = input("name of recipe: ")
    cooking_time = int(input("cooking time: "))
    ingredients = input("ingredients: ").split(", ")
    difficulty = calc_difficulty(cooking_time, ingredients)
    ingredients = ", ".join(ingredients).strip()
    cursor.execute("INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)",(name, ingredients, cooking_time, difficulty))
    conn.commit()

def search_recipe(conn, cursor):
    print("search recipe: ")
    all_ingredients = []
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    for i in results:
        ingredients = i[0].split(', ')
        for j in ingredients:
            if j not in all_ingredients:
                all_ingredients.append(j)
    
    print("All ingredients: ")
    for i in all_ingredients:
        print(i)

    search_ingredient = input("search ingredient: ")
    sql = "SELECT name, ingredients FROM Recipes WHERE ingredients LIKE %s"
    val = f"%{search_ingredient}%"

    cursor.execute(sql, (val,))

    for i, j in cursor:
        print("Name: ", i, ", Ingredients: ", j)

def update_recipe(conn, cursor):
    print("update recipe: ")

    cursor.execute("SELECT id, name FROM Recipes")

    results = cursor.fetchall()

    for row in results:
        print("ID: ", row[0], ", Name: ", row[1])

    id_input = int(input("Enter id to update: "))
    column_input = input("Enter column to update: ")
    new_row = input("New value for variable: ")
    
    if column_input == "cooking_time":
        column_input = int(column_input)

    if column_input == "cooking_time" or column_input == "ingredients":
        cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (id_input, ))
        ingredients = cursor.fetchall()[2]
        cooking_time = cursor.fetchall()[3]

        difficulty = calc_difficulty(column_input, ingredients.split(", "))

        cursor.execute("UPDATE Recipes SET %s = %s, difficulty = %s WHERE id = %s", (column_input, new_row, difficulty, id_input))

    conn.commit()

def delete_recipe(conn, cursor):
    print('delete recipe')
    rec_del =  int(input(('Enter recipe to delete: ')))
    cursor.execute("DELETE FROM Recipes WHERE id = %s", (rec_del,))
    conn.commit()

def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    if cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    if cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    if cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"
    return difficulty

main_menu(conn, cursor)