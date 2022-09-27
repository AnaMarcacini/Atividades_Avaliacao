from cProfile import label
from turtle import onclick
import streamlit as st
import webbrowser
import pages.home as home
import pages.login as log

global pagina


pagina = "login"

if pagina == "login":
    log.AbrirLogin(pagina)


if pagina == "Home":
    home.AbrirHome(pagina)


"""
#st.session_state["pagina"] = "login"


if st.session_state["pagina"] == "login":
    log.AbrirLogin(st.session_state["pagina"])


if st.session_state["pagina"] == "Home":
    home.AbrirHome(st.session_state["pagina"])
    
   """ 
    
    
#st.sidebar.title("temporario")
