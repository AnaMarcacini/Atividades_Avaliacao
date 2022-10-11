from ipaddress import collapse_addresses
from itertools import product
from numpy import true_divide
import streamlit as st
import models.product as p
#import controllers.product_controller as controladorProduto
from controllers.product_controller import ProductController
import pages.login as log


def adicionarCarrinho(indice):
    indice = int(indice)
    st.session_state["a"].addCarrinho(indice)


def percorrerCarrinho() :
    return st.session_state["a"].verCarrinho()

def limparCarrinho():
    st.session_state["a"].setCarrinho()
    #return st.session_state["a"].verCarrinho()




def AbrirHome():
   

    if "a" not in st.session_state:
        st.session_state["a"] = ProductController()


    main, info, carrinho,sair = st.tabs(["Home", "Info", "Carrinho 🛒","Sair"])

    with main:

        st.title("Home")
        
        imagensBanner = ["assets/B1.jpg","assets/B2.jpg"]
        st.image( #Banner  
                image=imagensBanner,
            )
##PRODUTOS __________________________________________________________________________________
        st.header("Mais Vendidos")
        p11,p12,p13,p14,p15 = st.columns([3,3,3,3,1])
        with p11:            

            st.image(   
                    image=st.session_state["a"].produtos[0].getUrl() ,
                    caption=st.session_state["a"].produtos[0].getNome()+"aaa"
                )     
                
            st.metric("Preço",st.session_state["a"].produtos[0].getPreco(), "12%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"indice":0},
                
            )

        with p12:

            st.image(   
                    image=st.session_state["a"].produtos[1].getUrl() ,
                    caption= st.session_state["a"].produtos[1].getNome()+"teste"
                )     
                
            st.metric("Preço", st.session_state["a"].produtos[1].getPreco(), "15%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"indice":1},
                key= 1111
            )
        with p13:
            st.image(   
                    image=st.session_state["a"].produtos[2].getUrl() ,
                    caption=st.session_state["a"].produtos[2].getNome()
                )     
                
            st.metric("Preço", st.session_state["a"].produtos[2].getPreco(),0)
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"indice":2},
                key=12
            )

        with p14:

            st.image(   
                    image=st.session_state["a"].produtos[3].getUrl() ,
                    caption=st.session_state["a"].produtos[3].getNome()
                )     
                
            st.metric("Preço",st.session_state["a"].produtos[3].getPreco() , "10%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"indice":3},
                key=1
            )

        with p15:
            st.image(   
                    image="assets/setinha.png"
                )     
        
        
        st.header("Produtos Relacionados")
        p1,p2,p3,p4,p5 = st.columns([3,3,3,3,1])
        with p1:
            st.image(   
                    image=st.session_state["a"].produtos[4].getUrl() ,
                    caption=st.session_state["a"].produtos[4].getNome()
                )     
                
            st.metric("Preço", st.session_state["a"].produtos[4].getPreco() , "12%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"indice":4},
                key=13
            )
        with p2:
            st.image(   
                    image=st.session_state["a"].produtos[5].getUrl() ,
                    caption=st.session_state["a"].produtos[5].getNome()
                )     
                
            st.metric("Preço",st.session_state["a"].produtos[5].getPreco() , "15%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"indice":5},
                key=2
            )
        with p3:
            st.image(   
                    image=st.session_state["a"].produtos[6].getUrl() ,
                    caption=st.session_state["a"].produtos[6].getNome()
                )     
                
            st.metric("Preço", st.session_state["a"].produtos[6].getPreco(),0)
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"indice":6},
                key = 3
            )
        with p4:
            st.image(   
                    image=st.session_state["a"].produtos[7].getUrl() ,
                    caption= st.session_state["a"].produtos[7].getNome()
                )

            st.metric("Preço", st.session_state["a"].produtos[7].getPreco(), "10%")

            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho,
                kwargs={"indice":7},
                key = 4
            )
        with p5:
            st.image(   
                    image="assets/setinha.png"
                )

    with carrinho:
        dadosCartao, compras = st.columns([8,3])
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
            st.markdown(percorrerCarrinho())
            st.button(
                "Limpar Carrinho 🛒",            
                on_click = limparCarrinho
            )

    with info:
        a,b = st.columns([3,1])
        with a:
            st.write("Lorem ipsum dolor sit amet. Hic eligendi minus sit consequatur nihil ea similique nesciunt sed repellat quasi ex aperiam sint non nisi repellat. Vel tenetur repellendus aut vitae voluptatem aut dolorem tempora et iure inventore sit quibusdam iusto qui quaerat autem cum tenetur sequi. Et commodi minus et sint blanditiis non rerum earum.Est veniam totam ea praesentium dicta cum omnis quibusdam eos sint voluptatem. Aut eligendi incidunt ut reprehenderit asperiores ad provident dolore qui fugiat voluptatem et omnis quibusdam ut delectus voluptas nam totam voluptatem. In doloribus vitae aut maiores ")
        with b:
            st.image(
                image="assets/P.png",

            )
    #with sair:
        #log.AbrirLogin()


#______________________________________________________________________________________________
#______________________________________________________________________________________________
#______________________________________________________________________________________________
#______________________________________________________________________________________________


AbrirHome()

#__________________________________________________________________________________________________







