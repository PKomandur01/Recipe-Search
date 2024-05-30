import requests
from config import API_KEY

BASE_URL = 'https://api.spoonacular.com/'

def get_recipe_information(recipe_id):
    """Fetch recipe information by ID."""
    endpoint = f'recipes/{recipe_id}/information'
    url = f'{BASE_URL}{endpoint}'
    params = {
        'apiKey': API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def search_recipes_by_ingredients(ingredients, number=3):
    """Search for recipes by ingredients."""
    endpoint = 'recipes/findByIngredients'
    url = f'{BASE_URL}{endpoint}'
    params = {
        'apiKey': API_KEY,
        'ingredients': ','.join(ingredients),
        'number': number
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
