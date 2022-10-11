"""
Ana Helena A. C. R. Marcacini
        RA: 20.01305-0
"""
class Product():
    def __init__(self, name, price,url = "assets/prod.png") -> None:
        self._name = name
        self._price = price
        #self.url = url especifica futuro
        self._url = url
    def __str__(self) -> str:
        return f'{self._name} -- {self._price})'


    def getPreco(self):
        return self._price

    def getNome(self):
        return self._name
        
    def getUrl(self):
        return self._url