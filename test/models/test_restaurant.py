from src.models.restaurant import Restaurant
from helper.helper_functions import ReturnCode
import pytest


class TestRestaurant:
    def setup(self):
        self.restaurant_name = 'Chopchop_tay_food'.title()
        self.cuisine_type = 'Taylandesa'

    def test_describe_restaurant(self, logs):
        # arrange
        msg1 = f"Esse restaurante chama {self.restaurant_name} and serve {self.cuisine_type}."
        msg2 = f"Esse restaurante está servindo 0 consumidores desde que está aberto."

        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        # act
        result = restaurant.describe_restaurant()
        # assert
        assert result == ReturnCode.STATUS_OK
        assert msg1 in logs.info
        assert msg2 in logs.info

    def test_open_restaurant_success(self, logs):
        # arrange
        msg = f"{self.restaurant_name} agora está aberto!"
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        # act
        result = restaurant.open_restaurant()
        # assert
        assert result == ReturnCode.STATUS_OK
        assert msg in logs.info

    def test_already_opened_restaurant(self, logs):
        # arrange
        msg = f"{self.restaurant_name} já está aberto!"
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()
        # act
        result = restaurant.open_restaurant()
        # assert
        assert result == ReturnCode.STATUS_ERROR
        assert msg in logs.warning

    def test_close_restaurant(self, logs):
        # arrange
        msg = f"{self.restaurant_name} agora está fechado!"
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()
        # act
        result = restaurant.close_restaurant()
        # assert
        assert result == ReturnCode.STATUS_OK
        assert msg in logs.info

    def test_already_closed_restaurant(self, logs):
        # arrange
        msg = f"{self.restaurant_name} já está fechado!"
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        # act
        result = restaurant.close_restaurant()
        # assert
        assert result == ReturnCode.STATUS_ERROR
        assert msg in logs.warning

    def test_set_number_served(self, logs):
        # arrange
        msg = "Numero alterado"
        expected_number = 100
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()
        # act
        result = restaurant.set_number_served(100)
        # assert
        assert result == ReturnCode.STATUS_OK
        assert restaurant.number_served == expected_number
        assert msg in logs.info

    def test_set_number_served_invalid_number(self, logs):
        # arrange
        msg = "Numero invalido"
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()
        # act
        result = restaurant.set_number_served('100')
        # assert
        assert result == ReturnCode.STATUS_INVALID
        assert msg in logs.error

    def test_set_number_served_negative_number(self, logs):
        # arrange
        msg = "Numero invalido"
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()
        # act
        result = restaurant.set_number_served(-1)
        # assert
        assert result == ReturnCode.STATUS_INVALID
        assert msg in logs.error

    def test_set_number_served_closed_restaurant(self, logs):
        # arrange
        msg = "Restaurante fechado"
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        # act
        result = restaurant.set_number_served(100)
        # assert
        assert result == ReturnCode.STATUS_ERROR
        assert msg in logs.warning

    def test_increment_number_served_success(self, logs):
        # arrange
        msg = "Numero incrementado"
        new_number = 110
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()
        restaurant.set_number_served(100)
        # act
        result = restaurant.increment_number_served(10)
        # assert
        assert restaurant.number_served == new_number
        assert result == ReturnCode.STATUS_OK
        assert msg in logs.info

    def test_increment_number_served_negative_number(self, logs):
        # arrange
        msg = "Numero invalido"
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()
        restaurant.set_number_served(100)
        # act
        result = restaurant.increment_number_served(-10)
        # assert
        assert result == ReturnCode.STATUS_INVALID
        assert msg in logs.error

    def test_increment_number_served_str(self, logs):
        # arrange
        msg = "Numero invalido"
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        restaurant.open_restaurant()
        restaurant.set_number_served(100)
        # act
        result = restaurant.increment_number_served('10')
        # assert
        assert result == ReturnCode.STATUS_INVALID
        assert msg in logs.error

    def test_increment_number_served_closed(self, logs):
        # arrange
        msg = f"{self.restaurant_name} esta fechado!"
        restaurant = Restaurant(self.restaurant_name, self.cuisine_type)
        # act
        result = restaurant.increment_number_served(10)
        # assert
        assert result == ReturnCode.STATUS_ERROR
        assert msg in logs.warning

    def test_invalid_init_name_empty(self, logs):
        with pytest.raises(ValueError) as excinfo:
            Restaurant('', self.cuisine_type)
        assert str(excinfo.value) == "Parametros invalidos"

    def test_invalid_init_name_int(self, logs):
        with pytest.raises(ValueError) as excinfo:
            Restaurant(0, self.cuisine_type)
        assert str(excinfo.value) == "Parametros invalidos"


    def test_invalid_init_type_empty(self, logs):
        with pytest.raises(ValueError) as excinfo:
            Restaurant(self.restaurant_name, '')
        assert str(excinfo.value) == "Parametros invalidos"

    def test_invalid_init_type_int(self, logs):
        with pytest.raises(ValueError) as excinfo:
            Restaurant(self.restaurant_name, 0)
        assert str(excinfo.value) == "Parametros invalidos"
