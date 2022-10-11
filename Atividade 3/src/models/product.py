"""
Ana Helena A. C. R. Marcacini
        RA: 20.01305-0
"""
class Product():
    def __init__(self, name, price,url = "assets/prod.png") -> None:
        self.name = name
        self.price = price
        #self.url = url especifica futuro
        self.url = url
    def __str__(self) -> str:
        return f'{self.name} -- {self.price})'


    def getPreco(self):
        return self.price

    def getNome(self):
        return self.name
        
    def getUrl(self):
        return self.url