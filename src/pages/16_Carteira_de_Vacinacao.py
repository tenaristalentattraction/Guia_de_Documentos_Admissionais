import streamlit as st

st.set_page_config(page_title='Carteira de Vacinação', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Carteira de Vacinação</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("Acesse o aplicativo oficial de saúde digital do Governo Federal para consultar as vacinas registradas no SUS.")
st.subheader("Passo a passo")
st.markdown("""
1. Baixe o aplicativo e entre com sua conta **gov.br**.
2. Na página inicial, acesse **Vacinas**.
3. Confira os registros disponíveis.
4. Tire prints das telas com seus dados e os registros de vacinação.
""")
st.markdown('<div class="image-placeholder">[IMAGEM 1: tela inicial do aplicativo com o ícone Vacinas]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 2: tela com os registros de vacinação]</div>', unsafe_allow_html=True)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
