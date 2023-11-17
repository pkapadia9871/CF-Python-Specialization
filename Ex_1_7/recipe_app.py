from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column

from sqlalchemy.types import Integer, String

engine = create_engine("mysql://cf-python:password@localhost/task_database")

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "final_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + "-" + self.difficulty + ">"
    
    def __str__(self):
        return "ID: " + str(self.id) + " Name: " + str(self.id) + " Ingredients: " + str(self.ingredients) + " Cooking Time " + str(self.cooking_time) + " Difficulty: " + str(self.difficulty)

    def calc_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients.split(", ")) < 4:
            difficulty = "Easy"
        if self.cooking_time < 10 and len(self.ingredients.split(", ")) >= 4:
            difficulty = "Medium"
        if self.cooking_time >= 10 and len(self.ingredients.split(", ")) < 4:
            difficulty = "Intermediate"
        if self.cooking_time >= 10 and len(self.ingredients.split(", ")) >= 4:
            difficulty = "Hard"
        return difficulty

    def return_ingredients_as_list(self):
        if self.ingredients == "":
            return []
        else:
            return list(self.ingredients.split(', ').strip())

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()


def create_recipe():

    print("create recipe: ")
    name = input("name of recipe: ")
    cooking_time = int(input("cooking time: "))

    if len(name) > 50 or name.isalnum == False:
        print("name not valid")
    #if cooking_time.isnumeric() == False:
    #    print("cooking time not valid")
    
    ingredients = []
    num_ing = int(input("number of ingredients: "))
    for i in range(num_ing):
        ing = input("Ingredient: " + str(i+1) + " ")
        ingredients.append(ing)
    ingredients_str = ", ".join(ingredients).strip()

    recipe_entry = Recipe(name=name, ingredients=ingredients_str, cooking_time=cooking_time)

    recipe_entry.difficulty = recipe_entry.calc_difficulty()

    print(recipe_entry)

    session.add(recipe_entry)
    session.commit()


def view_all_recipes():

    print("view all recipes")
    recipes_list = session.query(Recipe).all()
    if recipes_list == []:
        print("no entries in database")
        return None
    else:
        for i in recipes_list:
            print(i)

def search_by_ingredients():
    print("search by ingredients")

    if session.query(Recipe).count() == 0:
        print("no entries")
        return None
    else:
        results = session.query(Recipe.ingredients).all()
        all_ingredients = []
        for i in results:
            ingredients = list(i[0].lower().split(", "))
            for j in ingredients:
                if j not in all_ingredients:
                    all_ingredients.append(i)

        list_ingredients = list(enumerate(all_ingredients, 1))
        for i in list_ingredients:
            print(str(i[0]) + ": " + str(i[1]))
    
        numbers_of_ings = input("which numbers of ingredients you want? ")

        numbers_of_ings = numbers_of_ings.split()

        for i in numbers_of_ings:
            if i.isdigit() == False:
                print("not valid")
                return None
        
        search_ingredients = []

        for i in numbers_of_ings:
            search_ingredients.append(list(all_ingredients[int(i)-1]))

        conditions = []

        for i in search_ingredients:
            conditions.append(Recipe.ingredients.like("%"+str(i)+"%"))

        recipes = session.query(Recipe).filter(*conditions).all()

        for i in recipes:
            print(i)

def edit_recipe():
    print("edit recipe")

    if session.query(Recipe).count() == 0:
        print("no entries")
        return None
    
    else:
        results = session.query(Recipe.id, Recipe.name).all()
        for i in results:
            print("ID: ", str(i[0]), " Name: ", str(i[1]))
        
        id_no = int(input("Enter id of recipe to edit: "))

        recipe_to_edit = session.query(Recipe).get(id_no)

        print("Recipe to be edited: ")
        print(recipe_to_edit)

        print("1. Name 2. Ingredients 3. Cooking Time")

        edit_attribute = int(input("attribute to be edited: "))

        if edit_attribute == 1:
            new_name = input("Enter new name: ")
            recipe_to_edit.name = new_name
        if edit_attribute == 2:
            new_ings = input("Enter new ingredients: ")
            recipe_to_edit.ingredients = new_ings
        if edit_attribute == 3:
            new_cooking_time = int(input("Enter new cooking time: "))
            recipe_to_edit.cooking_time = new_cooking_time

        recipe_to_edit.difficulty = recipe_to_edit.calc_difficulty()

        session.commit()

def delete_recipe():
    print("delete recipe")

    if session.query(Recipe).count() == 0:
        print("No recipes in database")
        return None
    else:
        all_recipes = session.query(Recipe.id, Recipe.name).all()
        for i in all_recipes:
            print("ID: ", str(i[0]), " Name: ", i[1])
        
        id_name = int(input("Enter id of recipe to delete: "))
        recipe_id = session.query(Recipe).get(int(id_name))
        
        yes_no = input("like to delete this entry? yes or no: ")
        if yes_no == "yes":
            session.delete(recipe_id)
            session.commit()
        else:
            return "not deleted"
            
def main_menu():

    print('enter something: ')

    your_choice = ''

    while your_choice != 'quit':
        print('Main Menu')
        print("=========")
        print("Pick a choice:")
        print("create recipe")
        print("view all recipes")
        print("search by ingredients")
        print("edit recipe")
        print("delete_recipe")
        print("Type quit to exit the program")
        your_choice = input("Your choice: ")

        if your_choice == '1':
            create_recipe()
        if your_choice == '2':
            view_all_recipes()
        if your_choice == '3':
            search_by_ingredients()
        if your_choice == '4':
            edit_recipe()
        if your_choice == '5':
            delete_recipe()
        
    session.close()
    engine.dispose()

main_menu()