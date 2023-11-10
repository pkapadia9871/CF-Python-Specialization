# Defining the Recipe class
class Recipe(object):
    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = ""

    def calc_difficulty(self, cooking_time, ingredients):
        if cooking_time < 10 and len(ingredients) < 4:
            difficulty = "Easy"
        if cooking_time < 10 and len(ingredients) >= 4:
            difficulty = "Medium"
        if cooking_time >= 10 and len(ingredients) < 4:
            difficulty = "Intermediate"
        if cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = "Hard"
        self.difficulty = difficulty

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
       self.cooking_time =  cooking_time

    def add_ingredients(self, *args):
        for i in args:
            self.ingredients.append(i)
        self.update_all_ingredients()

    def search_ingredient(self, i):
        if i in self.ingredients:
            return True
        else:
            return False
        
    def get_difficulty(self):
        if self.difficulty == "":
            self.calc_difficulty(self.cooking_time, self.ingredients)
        else:
            return self.difficulty

    all_ingredients = []

    def update_all_ingredients(self):
        for i in self.ingredients:
            if i not in Recipe.all_ingredients:
                Recipe.all_ingredients.append(i)
        
    def __str__(self):
        output = "Recipe: " + str(self.name) + " Cooking Time: " + str(self.cooking_time) + " Ingredients: " + ', '.join(self.ingredients) + ' Difficulty: ' + str(self.difficulty)
        return output
    
def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)

tea = Recipe("Tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.get_difficulty()
print(tea)

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.get_difficulty()
print(coffee)

cake = Recipe("Cake", 5)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
cake.get_difficulty()
print(cake)

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
banana_smoothie.get_difficulty()
print(banana_smoothie)

recipes_list = [tea, coffee, cake, banana_smoothie]

recipe_search(recipes_list, "Water")

recipe_search(recipes_list, "Sugar")

recipe_search(recipes_list, "Bananas")
