from models.product import Product


class ProductController():
    def __init__(self) -> None:
        #Carrega os dados dos usuários
        self.produtos = [#estoque
            Product("Produto 1", "R$ 100,00"),
            Product("Produto 2", "R$ 110,00"),
            Product("Produto 3", "R$ 120,00"),
            Product("Produto 4", "R$ 130,00"),
            Product("Produto 5", "R$ 140,00"),
            Product("Produto 6", "R$ 150,00"),
            Product("Produto 7", "R$ 160,00"),
            Product("Produto 8", "R$ 170,00")
        ]

        self.carrinho = []

    def addCarrinho(self,indicee):
        print("entrou na segunda fnção")
        indicee = int(indicee)
        print(indicee)
        self.carrinho.append(self.produtos[indicee])
        print("add")
        print(len(self.carrinho))

        #c = st.session_state["a"].produtos[indice]
        #st.session_state["a"].carrinho.append(c)

    def  getCarrinho(self):
        return self.carrinho

    def somaCarrinho(self):
        total = 0
        for item in self.carrinho:
            preco = item.getPreco()
            print(preco)
            preco = preco[2::]
            print(preco)
            preco = preco.replace(',', '.') 
            print(preco)
            preco = float(preco)
            print(preco)

            total = total+preco
        return total


    def verCarrinho(self) :
        texto = ""
        for produto in self.carrinho:
            print("Produto atual")
            print(produto)
            print("\n")
            p = str(produto)
            texto = p + "\n " + texto
        soma = self.somaCarrinho()
        soma = str(soma)
        texto = texto + "\n \n \n  -------- \n " + soma

        return texto

    def setCarrinho(self):
        self.carrinho = []