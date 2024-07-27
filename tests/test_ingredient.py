class TestIngredient():

    def test_get_price_return_value(self, filled_ingredient):
        assert filled_ingredient.get_price() == 123

    def test_get_name_return_name(self, filled_ingredient):
        assert filled_ingredient.get_name() == 'name'

    def test_get_type_return_type(self, filled_ingredient):
        assert filled_ingredient.get_type() == 'type'