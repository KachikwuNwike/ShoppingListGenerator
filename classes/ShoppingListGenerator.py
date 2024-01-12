class ShoppingListGenerator:
    def __init__(self):
        self.selected_recipes = []

    def add_recipe(self, recipe):
        self.selected_recipes.append(recipe)

    def generate_shopping_list(self):
        shopping_list = []

        for recipe in self.selected_recipes:
            for ingredient in recipe.ingredients:
                shopping_list.append(ingredient)

        return shopping_list
