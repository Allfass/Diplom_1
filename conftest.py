from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
import pytest

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def database():
    database = Database()
    return database

@pytest.fixture
def filled_bun():
    bun = Bun('name', 123)
    return bun

@pytest.fixture
def filled_ingredient():
    ingredient = Ingredient('type', 'name', 123)
    return ingredient
