from src.models.ice_cream_stand import IceCreamStand
from src.models.ice_cream_stand import ReturnCode
import pytest


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
        assert msg in logs.info
        assert result == ReturnCode.STATUS_OK

    def test_flavors_available_success(self, logs):
        # arrange
        sorveteria = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors)
        sorveteria.add_flavor("napolitano")
        sorveteria.add_flavor("creme")
        msg = "No momento temos os seguintes sabores de sorvete disponíveis: -napolitano -creme"
        # act
        result = sorveteria.flavors_available()
        # assert
        assert msg in logs.info
        assert result == ReturnCode.STATUS_OK

    def test_find_flavor_success(self, logs):
        # arrange
        sorveteria = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors)
        sorveteria.add_flavor("napolitano")
        msg = "Temos no momento napolitano!"
        # act
        result = sorveteria.find_flavor("napolitano")
        # assert
        assert msg in logs.info
        assert result == ReturnCode.STATUS_OK

    def test_find_flavor_not_found(self, logs):
        # arrange
        sorveteria = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors)
        sorveteria.add_flavor("creme")
        msg = "Não temos no momento napolitano!"
        # act
        result = sorveteria.find_flavor("napolitano")
        # assert
        assert msg in logs.info
        assert result == ReturnCode.STATUS_OK

    def test_find_flavor_empty(self, logs):
        # arrange
        sorveteria = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors)
        msg = "Estamos sem estoque atualmente!"
        # act
        result = sorveteria.find_flavor("napolitano")
        # assert
        assert msg in logs.info
        assert result == ReturnCode.STATUS_ERROR

    def test_add_flavor_invalid_empty(self,logs):
        # arrange
        sorveteria = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors)
        msg = "Parametro invalido!"
        # act
        result = sorveteria.add_flavor("")
        # assert
        assert msg in logs.error
        assert result == ReturnCode.STATUS_INVALID

    def test_add_flavor_invalid_int(self,logs):
        # arrange
        sorveteria = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors)
        msg = "Parametro invalido!"
        # act
        result = sorveteria.add_flavor(2)
        # assert
        assert msg in logs.error
        assert result == ReturnCode.STATUS_INVALID

    def test_add_flavor_invalid_None(self,logs):
        # arrange
        sorveteria = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors)
        msg = "Parametro invalido!"
        # act
        result = sorveteria.add_flavor(None)
        # assert
        assert msg in logs.error
        assert result == ReturnCode.STATUS_INVALID

    def test_add_flavor_already_available(self,logs):
        # arrange
        sorveteria = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors)
        msg = "Sabor já disponivel!"
        result = sorveteria.add_flavor("Creme")
        # act
        result = sorveteria.add_flavor("Creme")
        # assert
        assert msg in logs.warning
        assert result == ReturnCode.STATUS_ERROR

    def test_add_flavor_success(self,logs):
        # arrange
        sorveteria = IceCreamStand(self.restaurant_name, self.cuisine_type, self.flavors)
        msg = "Creme adicionado ao estoque!"
        # act
        result = sorveteria.add_flavor("Creme")
        # assert
        assert msg in logs.info
        assert result == ReturnCode.STATUS_OK

    def test_flavor_none(self,logs):
        with pytest.raises(ValueError) as excinfo:
            sorveteria = IceCreamStand(self.restaurant_name, self.cuisine_type, None)
        assert str(excinfo.value) == "Parametros invalidos"
