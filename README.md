# Drink Inventory CLI

This is a CLI application for managing a drink inventory system. It allows users to add drinks and ingredients, and to list all drinks and ingredients.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies using Pipenv:
    ```bash
    pipenv install
    ```
4. Initialize the database:
    ```bash
    pipenv run python -m app.cli init
    ```

## Usage

- To add a drink:
    ```bash
    pipenv run python -m app.cli add-drink
    ```

- To add an ingredient:
    ```bash
    pipenv run python -m app.cli add-ingredient
    ```

- To list all drinks:
    ```bash
    pipenv run python -m app.cli list-drinks
    ```

- To list all ingredients:
    ```bash
    pipenv run python -m app.cli list-ingredients
    ```

## Testing

To run the tests, use:
```bash
pipenv run python -m unittest discover -s tests


###  Run the Application

1. Initialize the database:
    ```bash
    pipenv run python -m app.cli init
    ```

2. Add an ingredient:
    ```bash
    pipenv run python -m app.cli add-ingredient
    ```

3. Add a drink:
    ```bash
    pipenv run python -m app.cli add-drink
    ```

4. List all drinks:
    ```bash
    pipenv run python -m app.cli list-drinks
    ```

5. List all ingredients:
    ```bash
    pipenv run python -m app.cli list-ingredients
    ```
# phase3project
