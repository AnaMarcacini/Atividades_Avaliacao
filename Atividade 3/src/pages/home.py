import streamlit as st

def AbrirHome(a):
    main, info, carrinho,sair = st.tabs(["Home", "Info", "Carrinho 🛒","Sair"])
    st.title("Home")
    imagensBanner = ["assets/B1.jpg","assets/B2.jpg"]
    st.image(   
            image=imagensBanner,
            #caption=""
        )

