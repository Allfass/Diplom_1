from praktikum.ingredient import Ingredient

class TestIngredient():

    def test_get_price_return_value(self):
        ingredient = Ingredient('type', 'name', 123)
        assert ingredient.get_price() == 123

    def test_get_name_return_name(self):
        ingredient = Ingredient('type', 'name', 123)
        assert ingredient.get_name() == 'name'

    def test_get_type_return_type(self):
        ingredient = Ingredient('type', 'name', 123)
        assert ingredient.get_type() == 'type'