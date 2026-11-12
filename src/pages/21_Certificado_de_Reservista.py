import streamlit as st

st.set_page_config(page_title='Certificado de Reservista', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Certificado de Reservista</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento militar</div>', unsafe_allow_html=True)

st.write(
    "Apresente uma foto ou digitalização completa e legível do seu documento "
    "militar. A solicitação pode ser atendida pelo Certificado de Reservista "
    "ou pelo documento militar correspondente à sua situação."
)

st.subheader("Documentos que podem aparecer")
st.markdown("""
Entre os documentos militares, podem existir:

- **Certificado de Reservista (CR);**
- **Certificado de Dispensa de Incorporação (CDI);**
- Outro documento oficial que comprove a situação militar.
""")

st.markdown(
    '<div class="image-placeholder">[IMAGEM 1: exemplo de Certificado de Reservista]</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="image-placeholder">[IMAGEM 2: exemplo de Certificado de Dispensa de Incorporação]</div>',
    unsafe_allow_html=True
)

st.subheader("Como obter uma segunda via")
st.markdown("""
Se você não tiver mais o documento:

1. Consulte o portal oficial do Alistamento Militar ou a Junta de Serviço Militar do seu município;
2. Verifique qual documento corresponde à sua situação militar;
3. Siga as orientações para emissão ou solicitação de segunda via;
4. Se a emissão online não estiver disponível, procure presencialmente a Junta de Serviço Militar;
5. Após obter o documento, envie uma imagem completa e legível no Lugarh.
""")

st.warning(
    "Os procedimentos podem variar conforme o tipo de documento e o município. "
    "Em caso de dúvida sobre qual comprovante apresentar, confirme com o RH."
)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
