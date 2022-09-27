import streamlit as st


main, info, carrinho,sair = st.tabs(["Home", "Info", "Carrinho 🛒","Sair"])
with main:
        st.title("Home")
        imagensBanner = ["assets/B1.jpg","assets/B2.jpg"]
        st.image(   
                image=imagensBanner,
                #caption=""
            )


def AbrirHome():
    main, info, carrinho,sair = st.tabs(["Home", "Info", "Carrinho 🛒","Sair"])
    with main:
        st.title("Home")
        imagensBanner = ["assets/B1.jpg","assets/B2.jpg"]
        st.image(   
                image=imagensBanner,
                #caption=""
            )

