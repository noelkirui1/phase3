# app/models.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Drink(Base):
    __tablename__ = 'drinks'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    recipes = relationship('Recipe', back_populates='drink')

    def __repr__(self):
        return f"<Drink(id={self.id}, name='{self.name}')>"

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    recipes = relationship('Recipe', back_populates='ingredient')

    def __repr__(self):
        return f"<Ingredient(id={self.id}, name='{self.name}')>"

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    drink_id = Column(Integer, ForeignKey('drinks.id'), nullable=False)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), nullable=False)
    quantity = Column(String, nullable=False)
    drink = relationship('Drink', back_populates='recipes')
    ingredient = relationship('Ingredient', back_populates='recipes')

    def __repr__(self):
        return f"<Recipe(id={self.id}, drink_id={self.drink_id}, ingredient_id={self.ingredient_id}, quantity='{self.quantity}')>"
