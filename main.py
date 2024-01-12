from classes.Recipe import Recipe
from classes.User import User

bread_recipe = Recipe(
    "Amish White Bread",
    [
        "2 cups warm water",
        "0.666 cup white sugar",
        "1.5 tablespoons active dry yeast",
        "0.25 cup vegetable oil",
        "1.5 teaspoons salt",
        "6 cups bread flour",
    ],
)
curry_recipe = Recipe("fish curry")
goat_recipe = Recipe("goat stew")


# Create user instance
user = User(user_id="kachikwu")

# Plan meals
user.plan_meal(bread_recipe)
user.plan_meal(curry_recipe)
user.plan_meal(goat_recipe)

# Generate shopping list
shopping_list = user.generate_shopping_list()

# Display shopping list
print("Shopping List:")
for item in shopping_list:
    print(item)
