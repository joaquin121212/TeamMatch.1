import streamlit as st
from PIL import Image
#aqui se encuentra la pagina principal con sus elementos de titutlo y de imagen
st.header("BIENVENIDO A :violet[TeamMatch] ", divider="violet")

st.write("ENCUENTRA TU PRÓXIMO EQUIPO Y TRIUNFA")

#aqui esta la imagen
image= Image.open("faker.jpg")
st.image (image, caption="")
