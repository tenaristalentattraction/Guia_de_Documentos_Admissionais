import streamlit as st

st.set_page_config(page_title='CTPS Digital', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">CTPS Digital</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("Baixe o aplicativo Carteira de Trabalho Digital, acesse com seu CPF e envie um print da tela que apresente seus dados pessoais.")
st.subheader("Passo a passo")
st.markdown("""
1. Instale o aplicativo **Carteira de Trabalho Digital**.
2. Acesse com sua conta **gov.br** ou conclua o cadastro solicitado.
3. Faça login no aplicativo.
4. Abra a área com seus dados pessoais.
5. Tire um print legível para envio no Lugarh.
""")
st.markdown('<div class="image-placeholder">[IMAGEM 1: instalação do aplicativo Carteira de Trabalho Digital]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 2: telas de cadastro e acesso]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 3: tela de dados pessoais da CTPS Digital]</div>', unsafe_allow_html=True)
st.info("Para preenchimento no Lugarh: o número da CTPS corresponde aos primeiros números do CPF e a série aos quatro últimos números do CPF, conforme orientação do manual.")

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
