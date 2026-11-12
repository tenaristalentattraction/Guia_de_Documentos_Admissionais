import streamlit as st

st.set_page_config(page_title='CTPS Física', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">CTPS Física</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para envio da Carteira de Trabalho física</div>', unsafe_allow_html=True)

st.write(
    "Para este campo, apresente uma foto da página de identificação da sua "
    "Carteira de Trabalho e Previdência Social (CTPS) física, na qual constam "
    "o número, a série e os demais dados do documento."
)

st.subheader("Qual página devo enviar?")
st.write(
    "Localize na CTPS física a página que apresenta os dados de identificação "
    "do titular e as informações da carteira."
)

st.markdown("""
Na imagem, certifique-se de que estejam visíveis e legíveis:

- **Número da Carteira de Trabalho;**
- **Série do documento;**
- **Dados de identificação do titular;**
- Demais informações presentes na página.
""")

st.markdown(
    '<div class="image-placeholder">[IMAGEM 1: exemplo da página de identificação da CTPS física, indicando onde localizar o número e a série]</div>',
    unsafe_allow_html=True
)

st.subheader("Como fotografar o documento")
st.markdown("""
- Posicione a carteira aberta sobre uma superfície plana;
- Fotografe a página inteira, sem cortar as bordas;
- Garanta que o número e a série estejam visíveis;
- Evite reflexos ou sombras;
- Confira se todos os dados podem ser lidos antes do envio.
""")

st.markdown(
    '<div class="image-placeholder">[IMAGEM 2: exemplo de enquadramento correto da página de identificação da CTPS física]</div>',
    unsafe_allow_html=True
)

st.warning(
    "Neste campo, envie somente a página de identificação da CTPS física. "
    "Os vínculos profissionais são solicitados separadamente no campo "
    "“CTPS - Todos os Registros”."
)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
