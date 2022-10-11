class Product():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        #self.url = url especifica futuro
        self.url = "assets/prod.png"
    def __str__(self) -> str:
        return f'{self.name}--- preço :{self.price})'


    def getPreco(self):
        return self.price
