# Refatoracao: Como regra geral, todos os  prints foram substituidos por logs.
# Refatoracao: Como regra geral, todos os returns usam a classe ReturnCode na pasta helper.
# Refatoracao: adicionado um metodo para validacao de numeros

from helper.helper_functions import *
import logging


class Restaurant:
    """Modelo de restaurante simples."""

    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        if not is_ok(validate_name(restaurant_name)) or \
                not is_ok(validate_name(cuisine_type)):
            raise ValueError("Parametros invalidos")

        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self) -> ReturnCode:
        """Imprima uma descrição simples da instância do restaurante."""
        # BUG: 1. Variavel utilizada para o nome estava errada. 2. Typo 'restaturante'
        logging.info(f"Esse restaurante chama {self.restaurant_name} and serve {self.cuisine_type}.")
        logging.info(f"Esse restaurante está servindo {self.number_served} consumidores desde que está aberto.")
        return ReturnCode.STATUS_OK

    def open_restaurant(self) -> ReturnCode:
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True  # BUG: valor open deve ser true
            self.number_served = 0  # BUG: numero errado de clientes servidos
            logging.info(f"{self.restaurant_name} agora está aberto!")
            return ReturnCode.STATUS_OK
        else:
            logging.warning(f"{self.restaurant_name} já está aberto!")
            return ReturnCode.STATUS_ERROR

    def close_restaurant(self) -> ReturnCode:
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = 0
            logging.info(f"{self.restaurant_name} agora está fechado!")
            return ReturnCode.STATUS_OK
        else:
            logging.warning(f"{self.restaurant_name} já está fechado!")
            return ReturnCode.STATUS_ERROR

    def set_number_served(self, total_customers: int) -> ReturnCode:
        """
        Defina o número total de pessoas atendidas por este restaurante até o momento.
        :param total_customers
        """
        if self.open:
            if validate_number(total_customers):
                self.number_served = total_customers
                logging.info("Numero alterado")
                return ReturnCode.STATUS_OK
            else:
                logging.error("Numero invalido")
                return ReturnCode.STATUS_INVALID
        else:
            logging.warning("Restaurante fechado")
            return ReturnCode.STATUS_ERROR

    def increment_number_served(self, more_customers: int) -> ReturnCode:
        """
        Aumenta número total de clientes atendidos por este restaurante.
        :param more_customers
        """
        if self.open:
            if validate_number(more_customers):
                self.number_served = self.number_served + more_customers
                logging.info("Numero incrementado")
                return ReturnCode.STATUS_OK
            else:
                logging.error("Numero invalido")
                return ReturnCode.STATUS_INVALID
        else:
            logging.warning(f"{self.restaurant_name} esta fechado!")
            return ReturnCode.STATUS_ERROR
