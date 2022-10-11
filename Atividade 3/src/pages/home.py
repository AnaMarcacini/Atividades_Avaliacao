from ipaddress import collapse_addresses
from itertools import product
from numpy import true_divide
import streamlit as st
import models.product as p
#import controllers.product_controller as controladorProduto

from controllers.product_controller import ProductController



### Funções
# Carrinho em formato de string e texto sem o tipo carrinho
# def adicionarCarrinho(nome, preco):#futuramente um tipo carrinho
#     """
#     preco = preco[2::]
#     preco = preco.replace(',', '. ') 
#     preco = float(preco)
#     prod = Product(nome , preco)
#     print (prod)
    
#     st.session_state["carrinho"].append(prod)
#     """
#     st.session_state["carrinho"].append(f'Produto {nome} - {preco}')
#     #percorrerCarrinho()

# def percorrerCarrinho() :
#     texto = ""
#     for produto in st.session_state["carrinho"]:
#         print("Produto atual")
#         #st.write(produto)
#         texto = produto + "\n " + texto
#     return texto



def adicionarCarrinho(indice):
    st.session_state["a"].addCarrinho(indice)
#     c = st.session_state["a"].produtos[indice]
#     st.session_state["a"].carrinho.append(c)
    #st.session_state["a"].carrinho.append(st.session_state["a"].produtos[indice])



# '''
# def adicionarCarrinho(nome, preco ):
#         b = p.Product(nome,preco)
#         st.session_state["a"].carrinho.append(b)
#         #controladorProduto.ProductController().carrinho.append
# '''
def percorrerCarrinho() :
    texto = ""
    for produto in st.session_state["a"].carrinho:
        print("Produto atual")
        print(produto)
        print("\n")
        p = str(produto)
        texto = p + "\n " + texto
    return texto



def AbrirHome():
    st.session_state["a"] = ProductController()


    #st.session_state["carrinho"] = []
    #st.session_state["a"] = controladorProduto.ProductController()

    main, info, carrinho,sair = st.tabs(["Home", "Info", "Carrinho 🛒","Sair"])
    with main:

        st.title("Home")
        imagensBanner = ["assets/B1.jpg","assets/B2.jpg"]
        st.image( #Banner  
                image=imagensBanner,
                #caption=""
            )
        st.header("Mais Vendidos")
##PRODUTOS __________________________________________________________________________________

        p11,p12,p13,p14,p15 = st.columns([3,3,3,3,1])
        with p11:
            fone = "fone de ouvido"
            preco_fone = "R$ 50,00"

            st.image(   
                    image="assets/prod.png",
                    caption=fone
                )     
                
            st.metric("Preço",preco_fone, "12%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                #kwargs={"indice":1},
                args=(1),


            )

        with p12:
            pc = "Computador"
            preco_pc = "R$ 150,00 "

            st.image(   
                    image="assets/prod.png",
                    caption= pc
                )     
                
            st.metric("Preço", preco_pc, "15%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"nome":pc, "preco":preco_pc},
                key= 1111
                #kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                #(nome, preco)
            )
        with p13:
            tablet = "Tablet"
            preco_tablet = "R$ 90,00 "
            st.image(   
                    image="assets/prod.png",
                    caption=tablet
                )     
                
            st.metric("Preço", preco_tablet,0)
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"nome":tablet, "preco":preco_tablet},
                key=12
                #kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                #(nome, preco)
            )

        with p14:

            preco_fone2 = "R$ 30,00"
            st.image(   
                    image="assets/prod.png",
                    caption=fone
                )     
                
            st.metric("Preço",preco_fone2 , "10%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"nome":fone, "preco":preco_fone},
                key=1
                #kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                #(nome, preco)
            )

        with p15:
            st.image(   
                    image="assets/setinha.png"
                )     
        
        
        st.header("Produtos Relacionados")
        p1,p2,p3,p4,p5 = st.columns([3,3,3,3,1])
        with p1:
            preco_fone3 = "R$ 50,00"
            st.image(   
                    image="assets/prod.png",
                    caption=fone
                )     
                
            st.metric("Preço", preco_fone3 , "12%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"nome":fone, "preco":preco_fone3},
                key=13
                #kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                #(nome, preco)
            )
        with p2:
            cel = "Celular"
            preco_cel = "R$ 150,00"

            st.image(   
                    image="assets/prod.png",
                    caption=cel
                )     
                
            st.metric("Preço",preco_cel , "15%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"nome":cel, "preco":preco_cel},
                key=2
                #kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                #(nome, preco)
            )
        with p3:
            preco_cel2 = "R$ 1500,00"
            st.image(   
                    image="assets/prod.png",
                    caption=cel
                )     
                
            st.metric("Preço", preco_cel2,0)
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"nome":cel, "preco":preco_cel2},
                key = 3
                #kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                #(nome, preco)
            )
        with p4:
            st.session_state["p14"] = "Produto generico 1" 
            st.image(   
                    image="assets/prod.png",
                    caption= st.session_state["p14"]
                )
            
            #st.text_input(
                #"",
                #st.session_state["p14"] ,
                #label_visibility="collapsed",
                #disabled = True
                #)
            st.metric("Preço", "R$ 30,00 ", "10%")

            st.button(
                "Add Carrinho 🛒",            
                #on_click = adicionarCarrinho(st.session_state["p14"],"R$ 30,00"),
                
                on_click = adicionarCarrinho,
                kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                key = 4
                #kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                #(nome, preco)
            )
        with p5:
            st.image(   
                    image="assets/setinha.png"
                )

    with carrinho:
        dadosCartao, compras = st.columns([3,1])
        with dadosCartao:#Dados da compra
            st.text_input("Titular: ")
            st.text_input("CPF ou CNPJ: ")
            st.text_input("Numero: ")
            st.text_input("codigo cvv: ")
            st.write("Validade")
            option = st.selectbox(
                    'més',
                    ('1', '2', '3',"4","5","6","7","8","9","10","12"))
            option = st.selectbox(
                    'Ano',
                    ('2022', '2023',"2024","2025","2026","2027","2028","2029"))
            st.text_input("Endereço ")
            st.text_input("Numero do apartamento: ")
        with compras:#lista de compras
            st.header("Carrinho🛒")
            st.write(percorrerCarrinho())


#______________________________________________________________________________________________
#______________________________________________________________________________________________
#______________________________________________________________________________________________
#______________________________________________________________________________________________


AbrirHome()

#__________________________________________________________________________________________________







