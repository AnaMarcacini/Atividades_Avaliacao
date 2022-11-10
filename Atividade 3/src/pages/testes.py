

import email
import streamlit as st
from models.user import User
from controllers.user_controller import UserController






def testes():
    st.title("TODAS AS CONTAS")
    

    def criarConta():
        #st.write((UserController.getALL()))
        #print((UserController.getALL()))
    


        items = UserController.getALL()
        for item in items:
            print(item)
            st.write(item)

    st.button(
            label="ver Contas ",
            help="Entrar na loja",
            on_click=criarConta
    )
    




testes()