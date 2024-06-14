# app/cli.py

import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models import Drink, Ingredient, Recipe
from app.database import DATABASE_URL, init_db

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized!")

@cli.command()
@click.option('--name', prompt='Ingredient name', help='The name of the ingredient.')
def add_ingredient(name):
    """Add a new ingredient."""
    session = Session()
    ingredient = Ingredient(name=name)
    session.add(ingredient)
    session.commit()
    click.echo(f'Ingredient {name} added successfully!')

@cli.command()
@click.option('--name', prompt='Drink name', help='The name of the drink.')
@click.option('--ingredient_ids', prompt='Ingredient IDs', help='Comma-separated list of ingredient IDs.')
@click.option('--quantities', prompt='Quantities', help='Comma-separated list of quantities for each ingredient.')
def add_drink(name, ingredient_ids, quantities):
    """Add a new drink."""
    session = Session()
    drink = Drink(name=name)
    session.add(drink)
    session.commit()
    
    ingredient_ids = [int(i) for i in ingredient_ids.split(',')]
    quantities = quantities.split(',')
    
    for ingredient_id, quantity in zip(ingredient_ids, quantities):
        recipe = Recipe(drink_id=drink.id, ingredient_id=ingredient_id, quantity=quantity)
        session.add(recipe)
    
    session.commit()
    click.echo(f'Drink {name} added successfully!')

@cli.command()
def list_drinks():
    """List all drinks."""
    session = Session()
    drinks = session.query(Drink).all()
    for drink in drinks:
        click.echo(f'Drink ID: {drink.id}, Name: {drink.name}')

@cli.command()
def list_ingredients():
    """List all ingredients."""
    session = Session()
    ingredients = session.query(Ingredient).all()
    for ingredient in ingredients:
        click.echo(f'Ingredient ID: {ingredient.id}, Name: {ingredient.name}')

if __name__ == '__main__':
    cli()
