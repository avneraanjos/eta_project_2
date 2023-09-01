from src.models.restaurant import Restaurant
from helper.helper_functions import *
import logging


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name: str, cuisine_type: str, flavors_list: list[str]):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        # Refatoracao: Adicionado verificacao de parametros para criacao do objeto.
        if flavors_list is None:
            raise ValueError("Parametros invalidos")
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self) -> ReturnCode:
        """Percorra a lista de sabores disponíveis e imprima."""
        if len(self.flavors) > 0:
            all_flavors = ""
            for flavor in self.flavors:
                all_flavors = f"{all_flavors} -{flavor}"
            logging.info(f"No momento temos os seguintes sabores de sorvete disponíveis:{all_flavors}")
        else:
            logging.info("Estamos sem estoque atualmente!")
        return ReturnCode.STATUS_OK

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        # Refatoracao: verificacao se existe sabores disponiveis
        if len(self.flavors) != 0:
            if flavor in self.flavors:
                logging.info(f"Temos no momento {flavor}!")
                return ReturnCode.STATUS_OK
            else:
                logging.info(f"Não temos no momento {flavor}!")
                return ReturnCode.STATUS_OK
        else:
            logging.info("Estamos sem estoque atualmente!")
            return ReturnCode.STATUS_ERROR

    def add_flavor(self, flavor: str) -> ReturnCode:
        """
        Add o sabor informado ao estoque.
        :param flavor
        """
        # Refatoracao: melhoria na logica, adicionando validacao da string de entrada.
        if validate_str(flavor) == ReturnCode.STATUS_OK:
            if flavor in self.flavors:
                logging.warning("Sabor já disponivel!")
                return ReturnCode.STATUS_ERROR
            else:
                self.flavors.append(flavor)
                logging.info(f"{flavor} adicionado ao estoque!")
                return ReturnCode.STATUS_OK
        else:
            logging.error("Parametro invalido!")
            return ReturnCode.STATUS_INVALID
