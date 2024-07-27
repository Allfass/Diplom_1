class TestBun():

    def test_get_name_return_name(self, filled_bun):
        assert filled_bun.get_name() == 'name'

    def test_get_price_return_value(self, filled_bun):
        assert filled_bun.get_price() == 123