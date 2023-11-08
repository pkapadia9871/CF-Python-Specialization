recipes_list = []
ingredients_list = []
n = int(input("Enter n: "))

def take_recipe():
    name = str(input("Enter name: "))
    cooking_time = int(input("Enter cooking time: "))
    ingredients = input("Enter ingredients: ").split()
    
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    return recipe

for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for i in recipes_list:
    if i['cooking_time'] < 10 and len(i['ingredients']) < 4:
        i['difficulty'] = "Easy"
    if i['cooking_time'] < 10 and len(i['ingredients']) >= 4:
        i['difficulty'] = "Medium"
    if i['cooking_time'] >= 10 and len(i['ingredients']) < 4:
        i['difficulty'] = "Intermediate"
    if i['cooking_time'] >= 10 and len(i['ingredients']) >= 4:
        i['difficulty'] = "Hard"

for i in recipes_list:
    print('Name: ', i['name'])
    print('Cooking time: ', i['cooking_time'])
    print('Ingredients: ', i['ingredients'])
    print('Difficulty: ', i['difficulty'])

ingredients_list.sort()
print('Ingredients Available Across All Recipes')
for i in ingredients_list:
    print(i)