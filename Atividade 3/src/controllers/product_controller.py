from models.product import Product

"""
Ana Helena A. C. R. Marcacini
        RA: 20.01305-0
"""
class ProductController():
    def __init__(self) -> None:
        #Carrega os dados dos usuários
        self.produtos = [#estoque
            Product(1,"Produto 1", "R$ 100,00"),
            Product(2,"Produto 2", "R$ 110,00"),
            Product(3,"Produto 3", "R$ 120,00"),
            Product(4,"Produto 4", "R$ 130,00","assets/lechonk.jpg"),
            Product(5,"Produto 5", "R$ 140,00","essa/imagem/nao/existe"),
            Product(6,"Produto 6", "R$ 150,00"),
            Product(7,"Produto 7", "R$ 160,00"),
            Product(8,"Produto 8", "R$ 170,00")
        ]

        self.carrinho = []

    def addCarrinho(self,indicee):
        indicee = int(indicee)
        try:
            self.carrinho.append(self.produtos[indicee])
        except:
            a = Product("produto não existe ou esgotou",price="0,00")
            self.carrinho.append(a)

        print("tamanho carrinho")
        print(len(self.carrinho))


    def  getCarrinho(self):
        return self.carrinho

    def somaCarrinho(self):
        total = 0
        for item in self.carrinho:
            preco = item.getPreco()
            preco = preco[2::]
            preco = preco.replace(',', '.') 
            preco = float(preco)
            total = total+preco
        return total


    def verCarrinho(self) :
        texto = ""
        for produto in self.carrinho:
            print("Produto atual")
            print(produto)
            print("\n")
            p = str(produto)
            texto = texto + "\n \n \n " + p
        soma = self.somaCarrinho()
        soma = str(soma)
        texto = texto + "\n \n \n  -------- \n R$ " + soma
        print("resultado final :::::: \n\n\n\n")
        print(texto)
        return texto

    def setCarrinho(self):
        self.carrinho = []
