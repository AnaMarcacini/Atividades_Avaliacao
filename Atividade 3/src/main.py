from cProfile import label
from turtle import onclick
import streamlit as st
import webbrowser
import pages.home as home
import pages.login as log
"""
Ana Helena A. C. R. Marcacini
        RA: 20.01305-0
        atualiza a pag ao carregar para carregar corretamente
"""
global pagina

pagina = "login"

if pagina == "login":
    log.AbrirLogin()


if pagina == "Home":
    home.AbrirHome()


##st.session_state["pagina"] = "login"


#if st.session_state["pagina"] == "login":
#    log.AbrirLogin(st.session_state["pagina"])


#if st.session_state["pagina"] == "Home":
#    home.AbrirHome(st.session_state["pagina"])
    
    
    
#st.sidebar.title("temporario")
