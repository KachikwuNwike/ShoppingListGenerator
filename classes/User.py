from classes.ShoppingListGenerator import ShoppingListGenerator


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.shopping_list_generator = ShoppingListGenerator()

    def plan_meal(self, recipe):
        self.shopping_list_generator.add_recipe(recipe)

    def generate_shopping_list(self):
        return self.shopping_list_generator.generate_shopping_list()
