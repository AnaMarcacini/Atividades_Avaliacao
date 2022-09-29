from ipaddress import collapse_addresses
from numpy import true_divide
import streamlit as st
import models.product as prod

### Funções

def adicionarCarrinho(nome, preco):#futuramente um tipo carrinho
    st.session_state["carrinho"].append(f'Produto {nome} - {preco}')
    #percorrerCarrinho()

#def adicionarCarrinhoN(Product produto):
#    pass




def percorrerCarrinho() :
    texto = ""
    for produto in st.session_state["carrinho"]:
        print(produto)
        print("\n")
        st.write(produto)
        texto = produto + "\n " + texto
        return texto

def AbrirHome():
    
    st.session_state["carrinho"] = []

    main, info, carrinho,sair = st.tabs(["Home", "Info", "Carrinho 🛒","Sair"])
    with main:

        st.title("Home")
        imagensBanner = ["assets/B1.jpg","assets/B2.jpg"]
        st.image(   
                image=imagensBanner,
                #caption=""
            )
        st.header("Mais Vendidos")
##PRODUTOS __________________________________________________________________________________

        p11,p12,p13,p14,p15 = st.columns([3,3,3,3,1])
        a = "fone de ouvido"
        b = "Computador"
        c = "Tablet"
        d = "Celular"
        with p11:
            st.image(   
                    image="assets/prod.png",
                    caption=a
                )     
                
            st.metric("Preço", "R$ 50,00 ", "12%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho(a, "R$ 50,00 ")
            )

        with p12:
            st.image(   
                    image="assets/prod.png",
                    caption= b
                )     
                
            st.metric("Preço", "R$ 150,00 ", "15%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho(a,"R$ 150,00"),
                key= 1111
                #kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                #(nome, preco)
            )
        with p13:
            st.image(   
                    image="assets/prod.png",
                    caption=c
                )     
                
            st.metric("Preço", "R$ 90,00 ",0)
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho(c,"R$ 90,00 "),
                key=12
                #kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                #(nome, preco)
            )

        with p14:
            st.image(   
                    image="assets/prod.png",
                    caption=d
                )     
                
            st.metric("Preço", "R$ 30,00 ", "10%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho(d,"R$ 30,00"),
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
            st.image(   
                    image="assets/prod.png",
                    caption=c
                )     
                
            st.metric("Preço", "R$ 50,00 ", "12%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho(c,"R$ 50,00 "),
                key=13
                #kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                #(nome, preco)
            )
        with p2:
            st.image(   
                    image="assets/prod.png",
                    caption=d
                )     
                
            st.metric("Preço", "R$ 150,00 ", "15%")
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho(d,"R$ 150,00 "),
                key=2
                #kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                #(nome, preco)
            )
        with p3:
            st.image(   
                    image="assets/prod.png",
                    caption=b
                )     
                
            st.metric("Preço", "R$ 90,00 ",0)
            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho(b,"R$ 90,00 "),
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
                on_click = adicionarCarrinho(st.session_state["p14"],"R$ 30,00"),
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
        with compras:#lista de compras
            st.header("Carrinho🛒")
            st.write(percorrerCarrinho())


#FUNÇÕES BASE

def somar_dois(v1,v2):
    resultado = v1+v2
    st.session_state["kratos"] = resultado


if "kratos" in st.session_state:
        st.metric(
                label="Resultado:",
                value=st.session_state["kratos"]
        )
#else:
        #st.write("Ainda nenhum calculo foi realizado!")


    



#______________________________________________________________________________________________
#______________________________________________________________________________________________
#______________________________________________________________________________________________
#______________________________________________________________________________________________


AbrirHome()

#__________________________________________________________________________________________________







