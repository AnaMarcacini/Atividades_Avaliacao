from models.product import Product


class ProductController():
    def __init__(self) -> None:
        #Carrega os dados dos usuários
        self.produtos = [#estoque
            Product("Produto 1", "100,00"),
            Product("Produto 2", "110,00"),
            Product("Produto 3", "120,00"),
            Product("Produto 4", "130,00"),
            Product("Produto 5", "140,00"),
            Product("Produto 6", "150,00"),
            Product("Produto 7", "160,00"),
            Product("Produto 8", "170,00")
        ]

        self.carrinho = []

    '''
    def checkUser(self,user):
        return user in self.users

    def checkLogin(self, name, password):
        user_teste = User(name=name, password=password, email=None)
        for user in self.users:
            if user.name == user_teste.name and user.password == user_teste.password:
                return True
        return False
'''