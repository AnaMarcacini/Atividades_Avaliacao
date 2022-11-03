
import email
import streamlit as st
from models.user import User
from controllers.user_controller import UserController






def AbrirCriacaoConta():
    st.title("Criação de conta")
    col1, col2= st.columns([3,1])
    with col1:
        email = st.text_input(
            "Digite o seu email :",
            placeholder = "email 💌"
        )
        usuario = st.text_input(
            "Digite o seu nome de Usuário :",
            placeholder = "Usuário 🙍‍♂️"
        )        
        senha = st.text_input(
            "Digite a sua senha :",
            placeholder = "Senha 🔒",
            type= "password"

        )

    def fui_apertado():
        print("Chamar validador de senhas")
        user1 = User(usuario, email, senha)
        print (user1)
        if (UserController.novoUsuario):
            print('usuario criado com sucesso')
        else:
            print("Erro na criação do usuario")
            st.write("usuario não encontrado")

    st.button(
            label="Criar conta ",
            help="Entrar na loja",
            on_click=fui_apertado
    )
    
    with col2:
        st.image(   
            image="assets/perfilb.png",
        )
        



AbrirCriacaoConta()