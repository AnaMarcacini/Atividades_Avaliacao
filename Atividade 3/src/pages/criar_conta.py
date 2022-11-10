
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

    def criarConta(usuario, email, senha):
        print("cRIANDO A CONTA")
        user1 = User(usuario, email, senha)
        print (user1)
        print("Erro de falta do argumento usuario a baixo")
        if (UserController.inserirUsuario(usuario = user1)):
            print('usuario criado com sucesso')
            st.write("usuario Criado")
        else:
            print("Erro na criação do usuario")
            st.write("usuario já cadastrado")

    st.button(
            label="Criar conta ",
            help="Entrar na loja",
            on_click=criarConta,
            #usuario, email, senha
             kwargs={"usuario":usuario,"senha":senha, "email": email},
    )
    
    with col2:
        st.image(   
            image="assets/perfilb.png",
        )
        



AbrirCriacaoConta()