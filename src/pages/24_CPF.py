import streamlit as st

st.set_page_config(page_title='CPF', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">CPF</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write(
    "Neste campo, apresente um documento ou comprovante oficial no qual o seu "
    "número de CPF esteja visível. Esta solicitação é diferente do campo "
    "“Comprovante de CPF Regular”."
)

st.subheader("O que pode ser apresentado?")
st.markdown("""
- Comprovante de inscrição no CPF;
- Documento oficial que apresente claramente o número do CPF, quando aceito no processo;
- Comprovante digital emitido pelo serviço oficial da Receita Federal.
""")

st.markdown(
    '<div class="image-placeholder">[IMAGEM 1: exemplo de documento ou comprovante com o número do CPF visível]</div>',
    unsafe_allow_html=True
)

st.subheader("Como emitir o comprovante de inscrição no CPF")
st.markdown("""
1. Acesse o serviço oficial da Receita Federal para emissão do comprovante de inscrição no CPF;
2. Preencha os dados solicitados;
3. Gere o comprovante;
4. Salve o documento ou tire um print completo e legível;
5. Envie o comprovante no Lugarh.
""")

st.markdown(
    '<div class="image-placeholder">[IMAGEM 2: página oficial para emissão do comprovante de inscrição no CPF]</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="image-placeholder">[IMAGEM 3: exemplo do Comprovante de Inscrição no CPF]</div>',
    unsafe_allow_html=True
)

st.warning(
    "CPF e Comprovante de CPF Regular são solicitações diferentes. Caso os dois "
    "campos apareçam no Lugarh, envie em cada campo o documento correspondente."
)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
