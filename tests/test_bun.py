from praktikum.bun import Bun

class TestBun():

    def test_get_name_return_name(self):
        bun = Bun('name', 123)
        assert bun.get_name() == 'name'

    def test_get_price_return_value(self):
        bun = Bun('name', 123)
        assert bun.get_price() == 123