"""
Ana Helena A. C. R. Marcacini
        RA: 20.01305-0
"""
from typing_extensions import Self
from src.dao.item_dao import ProdutoDAO

class Product():
    def __init__(self, id, name, price,url = "assets/prod.png", descricao = "") -> None:
        self.id = id
        self._name = name
        self._price = price
        self._url = url
        self.descricao = descricao
    def __str__(self) -> str:
        return f'{self._name} -- {self._price})'


    def getPreco(self):
        return self._price

    def getNome(self):
        return self._name
        
    def getUrl(self):
        return self._url