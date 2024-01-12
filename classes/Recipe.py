import requests


class Recipe:
    API_URL = "https://recipeapi-kachikwu-37473924f8f6.herokuapp.com"

    def __init__(self, name, ingredients=None):
        self.name = name
        self.ingredients = ingredients or self.fetch_ingredients()

    def fetch_ingredients(self):
        try:
            response = requests.get(f"{self.API_URL}/recipes?search={self.name}")
            data = response.json()
            if response.status_code == 200 and data:
                return data[0]["ingredients"]
            else:
                print(f"Failed to fetch ingredients for {self.name}.")
        except Exception as e:
            print(f"Error fetching ingredients: {e}.")

        return []
