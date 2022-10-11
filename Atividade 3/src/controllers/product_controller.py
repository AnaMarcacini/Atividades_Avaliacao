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

    def addCarrinho(self,indice):
        self.carrinho.append(self.produtos[indice])

        #c = st.session_state["a"].produtos[indice]
        #st.session_state["a"].carrinho.append(c)

    def  getCarrinho(self):
        return self.carrinho

    def somaCarrinho(self):
        total = 0
        for item in self.carrinho:
            preco = item.getPreco()
            preco = preco[2::]
            preco = preco.replace(',', '. ') 
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
            texto = p + "\n " + texto
        soma = self.somaCarrinho()
        texto = texto + "\n \n \n  -------- \n " + soma

        return texto

