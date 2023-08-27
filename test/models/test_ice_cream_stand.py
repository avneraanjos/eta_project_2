from src.models.ice_cream_stand import IceCreamStand
from src.models.ice_cream_stand import ReturnCode


class TestIceCreamStand:
    def setup(self):
        self.restaurant_name = 'Ice_eu_lambo'.title()
        self.cuisine_type = 'Sorveteria'
        self.flavors = []

    def test_flavors_available_empty(self, logs):
        # arrange
        sorveteria = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors)
        msg = "Estamos sem estoque atualmente!"
        # act
        result = sorveteria.flavors_available()
        # assert
        assert msg in logs.warning
        assert result == ReturnCode.STATUS_ERROR

    def test_flavors_available_success(self, logs):
        # arrange
        sorveteria = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors)
        sorveteria.add_flavor('napolitano')
        sorveteria.add_flavor('creme')
        msg = "No momento temos os seguintes sabores de sorvete disponíveis: -napolitano -creme"
        # act
        result = sorveteria.flavors_available()
        # assert
        assert msg in logs.info
        assert result == ReturnCode.STATUS_OK

    def test_find_flavor(self):
        assert False

    def test_add_flavor(self):
        assert False
