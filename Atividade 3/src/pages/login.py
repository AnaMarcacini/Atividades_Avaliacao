from cProfile import label
from turtle import onclick
import streamlit as st
import webbrowser
import pages.home as home


def AbrirLogin():
    st.title("Login")
    st.write("Faça seu login ou crie uma conta com a gente 😁")


    col1, col2= st.columns([3,1])
    with col1:
        text_input = st.text_input(
            "Digite o nome do Usuário :",
            placeholder = "Usuário 🙍‍♂️"
        )
        text_input = st.text_input(
            "Digite a senha :",
            placeholder = "Senha 🔒"
        )

    def fui_apertado():
        print("Chamar validador de senhas")
        st.session_state["A1"] = "Chamar validador de senhas"
        home.AbrirHome()
        #st.session_state["pagina"] == "Home"
        #pagina = "Home"
        #a = "Home"


    st.button(
            label="🚪 Entrar 🔓",
            help="Entrar na loja",
            on_click=fui_apertado,
    )
    with col2:
        st.image(   
            image="assets/perfilb.png",
            #caption=""
        )
        
    st.snow()
    if "A1" in st.session_state:
            text_input = st.text_input("",value = st.session_state["A1"], disabled = True,
            
        )

