import streamlit as st

st.set_page_config(
    page_title="Carteira de Identidade",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.lugarh-title {
    color: #000097;
    font-size: 2.3rem;
    font-weight: 750;
    margin-bottom: .25rem;
}

.lugarh-subtitle {
    color: #666666;
    font-size: 1.05rem;
    margin-bottom: 1.5rem;
}

@media (max-width: 600px) {
    .block-container {
        padding-top: 1.2rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .lugarh-title {
        font-size: 1.8rem;
    }

    .lugarh-subtitle {
        font-size: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Cartão SUS</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("Você pode apresentar uma foto do cartão físico ou um print da tela do aplicativo com seu nome completo e o número do Cartão SUS.")

st.subheader("Como localizar no aplicativo")
st.markdown("""
1. Baixe o aplicativo oficial de saúde digital do Governo Federal.
2. Entre com sua conta **gov.br**.
3. Na tela inicial, acesse a área do cartão ou dos seus dados cadastrais.
4. Localize seu nome completo e o número do registro.
5. Tire um print da tela para enviar no Lugarh.
""")
st.markdown('<div class="image-placeholder">[IMAGEM 1: tela inicial do aplicativo e botão de acesso ao cartão SUS]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 2: tela do cartão SUS com nome e número do registro]</div>', unsafe_allow_html=True)
st.warning("O print deve mostrar claramente seu nome e o número do Cartão SUS.")

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
