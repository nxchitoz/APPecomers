
import streamlit as st
import requests

st.set_page_config(page_title="ShopIA - Generador de Publicidad", layout="centered")

st.title("🧠 ShopIA - Generador IA de Contenido Publicitario")

st.markdown("Genera imágenes y textos publicitarios para redes sociales con IA.")

with st.form("form_generador"):
    producto = st.text_input("Nombre del producto", max_chars=100)
    objetivo = st.text_area("¿Qué quieres comunicar?", height=100)
    estilo = st.selectbox("Estilo del anuncio", ["emocional", "divertido", "elegante", "directo"])
    submitted = st.form_submit_button("Generar contenido")

if submitted:
    with st.spinner("Generando contenido con IA..."):
        response = requests.post("http://localhost:8000/generar_contenido", json={
            "producto": producto,
            "objetivo": objetivo,
            "estilo": estilo
        })

        if response.status_code == 200:
            data = response.json()
            st.subheader("📸 Imagen generada:")
            st.image(data["imagen"], use_column_width=True)
            st.subheader("✍️ Copy generado:")
            st.code(data["copy"], language="markdown")
            st.success("¡Contenido generado con éxito!")
        else:
            st.error("Ocurrió un error al generar el contenido.")
