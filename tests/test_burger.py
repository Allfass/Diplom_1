import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger():

    def test_set_buns_may_return_bun_variable(self):
        burger = Burger()
        bun = Mock()
        bun.name = "name"
        burger.set_buns(bun)
        assert burger.bun.name == "name"

    def test_add_ingredient_append_value_to_list(self):
        burger = Burger()
        ingredient_mock = Mock()
        ingredient_mock.name = "name"
        burger.add_ingredient(ingredient_mock)
        assert burger.ingredients[0].name == "name"

    def test_add_ingredient_several_times_append_values_to_list(self):
        burger = Burger()
        ingredient_mock = Mock()
        second_ingredient_mock = Mock()
        ingredient_mock.name = "name"
        second_ingredient_mock.name = "second_name"
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)
        assert burger.ingredients[0].name == "name"
        assert burger.ingredients[1].name == "second_name"

    def test_remove_ingredient_return_empty_list(self):
        burger = Burger()
        ingredient_mock = Mock()
        ingredient_mock.name = "name"
        burger.add_ingredient(ingredient_mock)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient_swap_two_elements_and_check_their_position(self):
        burger = Burger()
        ingredient_mock = Mock()
        second_ingredient_mock = Mock()
        ingredient_mock.name = "name"
        second_ingredient_mock.name = "second_name"
        burger.add_ingredient(ingredient_mock)
        burger.add_ingredient(second_ingredient_mock)
        burger.move_ingredient(0,1)
        assert burger.ingredients[1].name == "name"
        assert burger.ingredients[0].name == "second_name"

    @pytest.mark.parametrize("bun_price,ingredient_price,final_value", [(1,1,3),(0,0,0),(1.3,1.2,3.8)])
    def test_get_price_return_value(self, bun_price, ingredient_price, final_value):
        burger = Burger()
        bun_mock = Mock()
        ingredient_mock = Mock()
        bun_mock.get_price.return_value = bun_price
        ingredient_mock.get_price.return_value = ingredient_price
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_price() == final_value

    def test_get_receipt_return_receipt(self):
        burger = Burger()
        bun_mock = Mock()
        ingredient_mock = Mock()
        bun_mock.get_name.return_value = "name"
        ingredient_mock.get_name.return_value = "ing_name"
        ingredient_mock.get_type.return_value = "ing_type"
        bun_mock.get_price.return_value = 1
        ingredient_mock.get_price.return_value = 1
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        assert burger.get_receipt() == '(==== name ====)\n= ing_type ing_name =\n(==== name ====)\n\nPrice: 3'
