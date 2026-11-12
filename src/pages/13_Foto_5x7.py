import streamlit as st

st.set_page_config(page_title='Foto 5x7', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Foto 5x7</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("A foto será utilizada para a confecção do crachá e outras mídias internas. Você pode fazer uma selfie com o celular, desde que siga as orientações abaixo.")
st.subheader("Como tirar a foto")
st.markdown("""
- Use fundo completamente branco;
- Garanta boa iluminação;
- Mantenha o rosto centralizado;
- Evite sombras e objetos ao fundo;
- Não utilize filtros;
- Verifique se a imagem está nítida e com boa resolução.
""")
st.markdown('<div class="image-placeholder">[IMAGEM 1: exemplo de enquadramento correto para foto 5x7 com fundo branco]</div>', unsafe_allow_html=True)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
