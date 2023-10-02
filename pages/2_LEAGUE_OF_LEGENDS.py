import streamlit as st
import webbrowser as wb

#aca esta el apartado de lol, para enviar el curriculum de pro player
st.header("AQUÍ PODRÁS SUBIR TU CURRÍCULUM DE PRO PLAYER PARA SER CONTACTADO POR UN EQUIPO ", divider="violet")
st.write("déjanos aquí tu currículum para que los equipos puedan explorar tu perfil")


def fo():
    wb.open("https://docs.google.com/forms/d/e/1FAIpQLScIXSlLlPFvCAtMn6LZqxlw1sTBHkdP8T_abI-YBpEG6XVSmA/viewform?usp=sf_link")
st.button("FORMULARIO", on_click=fo)
