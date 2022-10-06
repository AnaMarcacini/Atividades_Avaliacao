class Product():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        #self.url = url
    def __str__(self) -> str:
        return f'{self.name}--- preço :{self.price})'