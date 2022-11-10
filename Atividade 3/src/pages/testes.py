

import streamlit as st
from models.user import User
from controllers.user_controller import UserController


from models.product import Product
from controllers.product_controller import ProductController



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
            on_click=criarConta
    )
    
    def Produtos():
        items = ProductController.getALL()
        for item in items:
            print(f"""{item.id}    '{item._price} '     {item._name}""")
            st.write(f"""{item.id}    '{item._price} '     {item._name}""")
    st.button(
            label="ver Produtos ",
            on_click=Produtos
    )
    



testes()