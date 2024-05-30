document.getElementById('searchForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const ingredientsInput = document.getElementById('ingredients').value;
    const ingredients = ingredientsInput.split(',').map(ingredient => ingredient.trim());

    if (ingredients.length !== 3) {
        alert('Please enter exactly 3 ingredients separated by commas.');
        return;
    }

    try {
        const response = await fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ ingredients })
        });

        const data = await response.json();
        displayResults(data);
    } catch (error) {
        console.error('Error:', error);
    }
});

function displayResults(recipes) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';

    recipes.forEach(recipe => {
        const recipeDiv = document.createElement('div');
        recipeDiv.classList.add('recipe');

        const title = document.createElement('h2');
        title.textContent = recipe.title;

        const image = document.createElement('img');
        image.src = recipe.image;

        const link = document.createElement('a');
        link.href = recipe.sourceUrl;
        link.textContent = 'View Recipe';

        recipeDiv.appendChild(title);
        recipeDiv.appendChild(image);
        recipeDiv.appendChild(link);

        resultsContainer.appendChild(recipeDiv);
    });
}
