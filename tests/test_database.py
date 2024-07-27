
from test_data import TestData

class TestDatabase():

    def test_available_buns_return_buns(self, database):
        buns = database.available_buns()
        for iterator, bun in enumerate(buns):
            assert bun.name == TestData.DATABASE_BUNS[iterator][0]
            assert bun.price == TestData.DATABASE_BUNS[iterator][1]
    
    def test_available_ingredients_return_list_of_ingredients(self, database):
        ingredients = database.available_ingredients()
        for iterator, ingredient in enumerate(ingredients):
            assert ingredient.type == TestData.DATABASE_INGREDIENTS[iterator][0]
            assert ingredient.name == TestData.DATABASE_INGREDIENTS[iterator][1]
            assert ingredient.price == TestData.DATABASE_INGREDIENTS[iterator][2]