import streamlit as st

st.set_page_config(page_title='Título Eleitoral', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Título Eleitoral</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("Você pode obter as informações pelo site oficial do Tribunal Superior Eleitoral ou pelo aplicativo e-Título.")
st.subheader("Pelo aplicativo e-Título")
st.markdown("""
1. Instale o aplicativo **e-Título**.
2. Acesse com seus dados pessoais.
3. Abra a tela que apresenta seus dados cadastrais eleitorais.
4. Tire um print legível para enviar no Lugarh.
""")
st.markdown('<div class="image-placeholder">[IMAGEM 1: instalação ou tela inicial do aplicativo e-Título]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 2: tela com os dados cadastrais eleitorais]</div>', unsafe_allow_html=True)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
