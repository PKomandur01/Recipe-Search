from flask import Flask, render_template, request
import logging
from spoonacular_api import get_recipe_information, search_recipes_by_ingredients

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    ingredients_input = request.form['ingredients']
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',')]

    logging.debug(f'User input ingredients: {ingredients}')
    
    if len(ingredients) > 3:
        logging.warning('More than 3 ingredients entered.')
        return render_template('error.html', message="Please enter only up to 3 ingredients.")

    try:
        search_results = search_recipes_by_ingredients(ingredients, number=3)
        logging.debug(f'API search results: {search_results}')

        if search_results and isinstance(search_results, list) and len(search_results) > 0:
            recipes = []
            for recipe in search_results:
                recipe_info = get_recipe_information(recipe['id'])
                recipes.append(recipe_info)
            return render_template('results.html', recipes=recipes)
        else:
            logging.info('No recipes found with the given ingredients.')
            return render_template('error.html', message="No recipes found.")
    except Exception as e:
        logging.error(f'Error during API request: {e}')
        return render_template('error.html', message="An error occurred while searching for recipes. Please try again.")

if __name__ == "__main__":
    app.run(debug=True)
