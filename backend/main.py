# main.py
from backend.spoonacular_api import get_recipe_information, search_recipes_by_ingredients

def display_recipe(recipe):
    """Display details of the recipe."""
    print()
    print("Title:", recipe["title"])
    print()
    print("Source URL:", recipe["sourceUrl"])
    print()
    print("Servings:", recipe["servings"])
    print()
    print("Ready in Minutes:", recipe["readyInMinutes"])
    print()
    print("Image URL:", recipe["image"])
    print()
    print("Instructions:")
    print()
    print(recipe["instructions"])
    print()

def main():
    try:
        # Prompt user for ingredients
        ingredients_input = input("Enter 3 ingredients separated by commas: ")
        ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',')]
        
        if len(ingredients) > 3:
            print("Error: Please enter only up to 3 ingredients.")
            return

        # Search recipes by ingredients
        search_results = search_recipes_by_ingredients(ingredients, number=3)
        
        # Display the recipes
        if 'results' in search_results:
            for recipe in search_results['results']:
                recipe_info = get_recipe_information(recipe['id'])
                print()
                display_recipe(recipe_info)
                print("\n---\n")
        else:
            print("No recipes found.")
        
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
