# recipe-app-api
# Django REST API Project

This project is a Django-based REST API for managing recipes, tags, and ingredients. It includes user authentication and uses PostgreSQL as the database. API documentation is provided via drf-spectacular and Swagger.

## Table of Contents
- [Installation](#installation)
- [Project Features](#project-features)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Documentation](#documentation)
- [Usage](#usage)
- [Testing](#testing)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <project-folder>

    Install Docker: Make sure Docker is installed and running on your machine. For installation instructions, visit Docker's website.

    Run the project: Use Docker Compose to set up and run the project.
    docker-compose up --build

    Install required Python packages: If running locally without Docker, install the necessary dependencies:
    pip install -r requirements.txt

    Database setup: Make sure PostgreSQL is running. Create a database, then apply the migrations:
    python manage.py migrate

    Create a superuser:
    python manage.py createsuperuser

## Project Features
User Management:

    User registration and authentication (using email as the unique identifier).
    Admin and superuser support.
Recipe Management:

    Create, read, update, and delete recipes.
    Filter recipes by tags and ingredients.
Tag and Ingredient Management:

    Create and manage tags and ingredients associated with recipes.

## API Endpoints

### User Endpoints
- **POST** `/api/user/create/`: Create a new user.
- **POST** `/api/user/token/`: Obtain an authentication token.
- **GET** `/api/user/me/`: Retrieve user profile (requires authentication).

### Recipe Endpoints
- **GET** `/api/recipes/`: List all recipes (supports filters by tags and ingredients).
- **POST** `/api/recipes/`: Create a new recipe (requires authentication).
- **GET** `/api/recipes/:id/`: Retrieve a specific recipe by ID.
- **PUT** `/api/recipes/:id/`: Update a recipe (requires authentication).
- **PATCH** `/api/recipes/:id/`: Partially update a recipe (requires authentication).
- **DELETE** `/api/recipes/:id/`: Delete a recipe (requires authentication).
- **POST** `/api/recipes/:id/upload-image/`: Upload an image for a recipe (requires authentication).

### Tag Endpoints
- **GET** `/api/tags/`: List all tags (requires authentication).
    - Supports `assigned_only=1` query parameter to filter tags assigned to recipes.
- **POST** `/api/tags/`: Create a new tag (requires authentication).
- **PUT** `/api/tags/:id/`: Update an existing tag (requires authentication).
- **DELETE** `/api/tags/:id/`: Delete a tag (requires authentication).

### Ingredient Endpoints
- **GET** `/api/ingredients/`: List all ingredients (requires authentication).
    - Supports `assigned_only=1` query parameter to filter ingredients assigned to recipes.
- **POST** `/api/ingredients/`: Create a new ingredient (requires authentication).
- **PUT** `/api/ingredients/:id/`: Update an existing ingredient (requires authentication).
- **DELETE** `/api/ingredients/:id/`: Delete an ingredient (requires authentication).

### Schema & Documentation Endpoints
- **GET** `/api/schema/`: Retrieve the OpenAPI schema for the API.
- **GET** `/api/docs/`: Access the Swagger documentation interface.


## Models
    ### User
    Custom user model with email as the unique identifier.

    ### Recipe
    A recipe model containing:
    - **User**: (ForeignKey) Reference to the user who created the recipe.
    - **Title**: (CharField) The title of the recipe.
    - **Description**: (TextField) Optional detailed description of the recipe.
    - **Time in minutes**: (IntegerField) Time required to prepare the recipe.
    - **Price**: (DecimalField) The cost of the recipe.
    - **Link**: (CharField) Optional URL link for more information about the recipe.
    - **Tags**: (ManyToManyField) Tags used to categorize recipes.
    - **Ingredients**: (ManyToManyField) Ingredients used in the recipe.
    - **Image**: (ImageField) Optional image associated with the recipe.

    ### Tag
    A tag model for filtering recipes:
    - **Name**: (CharField) The name of the tag.
    - **User**: (ForeignKey) Reference to the user who created the tag.

    ### Ingredient
    An ingredient model:
    - **Name**: (CharField) The name of the ingredient.
    - **User**: (ForeignKey) Reference to the user who added the ingredient.

## Documentation
API documentation is automatically generated using drf-spectacular and can be accessed at:

OpenAPI Schema: /api/schema/
Swagger UI: /api/docs/

## Usage
To interact with the API, you can use tools like Postman or cURL. Ensure you include the JWT token in the request headers for endpoints requiring authentication.

    Example of obtaining a token:

    curl -X POST http://localhost:8000/api/user/token/ \
    -d '{"email": "user@example.com", "password": "password"}'

    Example of creating a recipe:

        curl -X POST http://localhost:8000/api/recipes/ \
    -H "Authorization: Bearer <your-token>" \
    -d '{"title": "Pasta", "time_minutes": 10, "price": 5.99}'

## Testing
Run tests with:

    python manage.py test

To check code quality using Flake8:
    flake8







