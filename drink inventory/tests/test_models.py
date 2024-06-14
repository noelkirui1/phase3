import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Drink, Ingredient, Recipe

class TestDrinkInventory(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_add_drink(self):
        ingredient1 = Ingredient(name="Vodka")
        ingredient2 = Ingredient(name="Orange Juice")
        self.session.add(ingredient1)
        self.session.add(ingredient2)
        self.session.commit()

        drink = Drink(name="Screwdriver")
        self.session.add(drink)
        self.session.commit()

        recipe1 = Recipe(drink_id=drink.id, ingredient_id=ingredient1.id, quantity="1 oz")
        recipe2 = Recipe(drink_id=drink.id, ingredient_id=ingredient2.id, quantity="2 oz")
        self.session.add(recipe1)
        self.session.add(recipe2)
        self.session.commit()
        
        retrieved_drink = self.session.query(Drink).first()
        self.assertEqual(retrieved_drink.name, "Screwdriver")

    def test_add_ingredient(self):
        ingredient = Ingredient(name="Vodka")
        self.session.add(ingredient)
        self.session.commit()
        retrieved_ingredient = self.session.query(Ingredient).first()
        self.assertEqual(retrieved_ingredient.name, "Vodka")

if __name__ == '__main__':
    unittest.main()
