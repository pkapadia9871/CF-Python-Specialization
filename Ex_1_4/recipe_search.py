import pickle

def display_recipe(recipe):
    print('Name', recipe["name"])
    print('Cooking time', recipe["cooking_time"])
    print('Ingredients', recipe["ingredients"])
    print('Difficulty', recipe["difficulty"])

def search_ingredient(data):
    print(list(enumerate(data['all_ingredients'])))
    try:
        no = int(input("select number from this list: "))
        ingredient_searched = data['all_ingredients'][no]
        print('Ingredients at this index: ', ingredient_searched)
    except:
        print('input is incorrect')
    else:
        for i in data['recipes_list']:
            for j in i['ingredients']:
                if j == ingredient_searched:
                    display_recipe(i)

filename = input("Enter the filename where you've stored your recipes: ")

try:
    file = open(filename, 'rb')
    data = pickle.load(file)
except FileNotFoundError:
    print("File doesn't exist - exiting.")
else:
    search_ingredient(data)
finally:
    print("Goodbye!")