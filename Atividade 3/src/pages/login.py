from cProfile import label
from turtle import onclick
import streamlit as st
import webbrowser
import pages.home as home
import controllers.user_controller as verificar
from models.user import User
import pages.criar_conta as novaConta
"""
Ana Helena A. C. R. Marcacini
        RA: 20.01305-0
"""
def AbrirLogin():
    st.title("Login")
    st.write("Faça seu login ou crie uma conta com a gente 😁")

    col1, col2= st.columns([3,1])
    with col1:
        usuario = st.text_input(
            "Digite o nome do Usuário :",
            placeholder = "Usuário 🙍‍♂️"
        )
        senha = st.text_input(
            "Digite a senha :",
            placeholder = "Senha 🔒",
            type= "password"

        )

    def fui_apertado():
        print("Chamar validador de senhas")
        user1 = User(usuario, usuario, senha)
        print (user1)
        if (verificar.UserController().checkLogin(usuario,senha)):
            home.AbrirHome()
            #st.session_state["pagina"] == "Home"
            #pagina = "Home"
            #a = "Home"
            #print("usuario encontrado mas vc é uma anta")
        else:
            print("usuario não encontrado")
            st.write("usuario não encontrado")
    st.button(
            label="🚪 Entrar 🔓",
            help="Entrar na loja",
            on_click=fui_apertado,
    )
    def CriarConta():
        novaConta.AbrirCriacaoConta()
    st.button(
            label="Criar Conta🎇",
            help="Entrar na loja",
            on_click=CriarConta,
    )

    with col2:
        st.image(   
            image="assets/perfilb.png",
        )
        
    st.snow()


AbrirLogin()