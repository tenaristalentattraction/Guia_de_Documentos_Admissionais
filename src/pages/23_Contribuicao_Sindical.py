import streamlit as st

st.set_page_config(page_title='Contribuição Sindical', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Contribuição Sindical</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para comprovação do desconto</div>', unsafe_allow_html=True)

st.write(
    "Se este documento for solicitado no seu processo, apresente um comprovante "
    "em que o desconto da contribuição sindical esteja identificado."
)

st.subheader("Opção 1: Holerite")
st.write(
    "Você pode apresentar um holerite em que a contribuição sindical esteja "
    "registrada entre os descontos."
)
st.markdown("""
Antes de enviar, confira se aparecem:

- Seu nome ou identificação;
- O período de referência;
- A descrição do desconto sindical;
- O valor descontado.
""")

st.markdown(
    '<div class="image-placeholder">[IMAGEM 1: exemplo de holerite indicando onde localizar o desconto da contribuição sindical]</div>',
    unsafe_allow_html=True
)

st.subheader("Opção 2: CTPS física")
st.write(
    "Também pode ser apresentada a página da CTPS física que contenha a anotação "
    "referente à contribuição sindical."
)

st.markdown(
    '<div class="image-placeholder">[IMAGEM 2: exemplo da página da CTPS física com anotação de contribuição sindical]</div>',
    unsafe_allow_html=True
)

st.warning(
    "Não envie páginas da CTPS ou holerites que não apresentem o registro do desconto. "
    "A informação precisa estar visível no documento."
)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
