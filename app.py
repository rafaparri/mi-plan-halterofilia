import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Mi Plan Halterofilia",
    page_icon="🏋️",
    layout="wide",
)

# Oculta la interfaz propia de Streamlit (menú, cabecera, pie, márgenes)
# para que se vea y se sienta como una app independiente, no como una
# página dentro de Streamlit. También añade el icono para "Añadir a
# pantalla de inicio" en iPhone (requiere el archivo static/apple-touch-icon.png
# y enableStaticServing=true en .streamlit/config.toml).
st.markdown(
    """
    <link rel="apple-touch-icon" href="/app/static/apple-touch-icon.png">
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {height: 100vh !important; width: 100% !important; border: none !important;}
    </style>
    """,
    unsafe_allow_html=True,
)

# El archivo mi-plan-halterofilia.html debe estar en la MISMA carpeta que
# este app.py dentro del repositorio de GitHub.
html_path = Path(__file__).parent / "mi-plan-halterofilia.html"
html_content = html_path.read_text(encoding="utf-8")

st.components.v1.html(html_content, height=1000, scrolling=True)
