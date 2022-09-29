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
    for produto in st.session_state["carrinho"]:
        print(produto)
        print("\n")
        #st.write(produto)
        texto = produto + "\n "
        #st.write(texto)
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

        col1,col2,col3,col4,col5 = st.columns([3,3,3,3,1])
        with col1:
            st.image(   
                    image="assets/prod.png",
                    #caption=""
                )     
                
            st.metric("Preço", "R$ 50,00 ", "12%")
        with col2:
            st.image(   
                    image="assets/prod.png",
                    #caption=""
                )     
                
            st.metric("Preço", "R$ 150,00 ", "15%")
        with col3:
            st.image(   
                    image="assets/prod.png",
                    #caption=""
                )     
                
            st.metric("Preço", "R$ 90,00 ")

        with col4:
            st.image(   
                    image="assets/prod.png",
                    #caption=""
                )     
                
            st.metric("Preço", "R$ 30,00 ", "10%")

        with col5:
            st.image(   
                    image="assets/setinha.png",
                    #caption=""
                )     
        st.header("Produtos Relacionados")

        col1,col2,col3,col4,col5 = st.columns([3,3,3,3,1])
        with col1:
            st.image(   
                    image="assets/prod.png",
                    #caption=""
                )     
                
            st.metric("Preço", "R$ 50,00 ", "12%")
        with col2:
            st.image(   
                    image="assets/prod.png",
                    #caption=""
                )     
                
            st.metric("Preço", "R$ 150,00 ", "15%")
        with col3:
            st.image(   
                    image="assets/prod.png",
                    #caption=""
                )     
                
            st.metric("Preço", "R$ 90,00 ")

        with col4:
            st.image(   
                    image="assets/prod.png",
                    #caption=""
                )
            st.session_state["p14"] = "Produto generico 1" #_____________________ALTERAR__________________
            st.text_input(
                "",
                st.session_state["p14"] ,
                label_visibility="collapsed",
                disabled = True
                )
            st.metric("Preço", "R$ 30,00 ", "10%")

            st.button(
                "Add Carrinho 🛒",            
                on_click = adicionarCarrinho("Ana","R$ 30,00")
                #kwargs={"nome":st.session_state["p14"], "preco":"R$ 30,00"},
                #(nome, preco)
            )


        with col5:
            st.image(   
                    image="assets/setinha.png",
                    #caption=""
                )

    with carrinho:
        dadosCartao, compras = st.columns([4,1])
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
            percorrerCarrinho()


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







