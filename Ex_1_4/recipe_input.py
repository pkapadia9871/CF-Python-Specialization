import pickle

def take_recipe():
    name = input("Enter name: ")
    cooking_time = int(input("Enter cooking time: "))
    ingredients = input("Enter ingredients: ").split()
    
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}

    recipe['difficulty']  = calc_difficulty(cooking_time, ingredients)

    return recipe

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

filename = input("Enter the filename where you've stored your recipes: ")
try:
    file = open(filename, 'r')
    data = pickle.load(file)
except FileNotFoundError:
    print("File doesn't exist - exiting.")
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    print("An unexpected error occurred.")
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    file.close()
finally:
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]
    print("Goodbye!")

n = int(input("Enter number of recipes: "))

for i in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)
    for i in recipe['ingredients']:
        if i not in all_ingredients:
            all_ingredients.append(i)

data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

file = open(filename, 'wb')
pickle.dump(data, file)
file.close()