import streamlit as st


st.set_page_config(
    page_title="Cartão Transporte URBS",
    page_icon="🚌",
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

.image-placeholder {
    background-color: #F3F6FD;
    border: 1px dashed #000097;
    border-radius: 10px;
    color: #333333;
    padding: 1.2rem;
    margin-top: 1rem;
    margin-bottom: 1.5rem;
    text-align: center;
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


# TÍTULO

st.markdown(
    '<div class="lugarh-title">Cartão Transporte URBS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="lugarh-subtitle">'
    'Orientações para o envio do cartão de transporte público'
    '</div>',
    unsafe_allow_html=True
)


# INTRODUÇÃO

st.write(
    "Apresente uma imagem do seu **cartão de transporte público URBS**."
)


# CHECKLIST

st.markdown("### O que conferir antes do envio:")

st.markdown("""
- O cartão deve aparecer por completo na imagem;
- A imagem deve estar nítida e legível;
- Nenhuma parte do cartão deve estar cortada;
- Evite reflexos, sombras ou objetos cobrindo o cartão;
- Confira se a imagem corresponde ao cartão utilizado por você.
""")


# COMO ENVIAR

st.markdown("#### Como fotografar o cartão")

st.write(
    "Posicione o cartão sobre uma superfície plana, em um local bem "
    "iluminado, e fotografe de forma que toda a parte frontal fique visível."
)

st.markdown(
    """
    <div class="image-placeholder">
        IMAGEM DE REFERÊNCIA<br>
        Inserir aqui um exemplo de cartão Transporte URBS fotografado
        completamente, sem cortes e com boa iluminação.
    </div>
    """,
    unsafe_allow_html=True
)


# SITUAÇÕES QUE DEVEM SER EVITADAS

st.subheader("Evite enviar")

st.markdown("""
- Foto do cartão parcialmente cortado;
- Imagem desfocada ou escura;
- Foto com reflexo que impeça a visualização;
- Imagem de outro cartão ou de cartão pertencente a outra pessoa;
- Somente o número do cartão digitado ou escrito em um papel.
""")


# CONFERÊNCIA FINAL

st.subheader("Confira antes de finalizar")

st.write(
    "Antes de concluir o envio no Lugarh, abra a imagem e confirme se "
    "o cartão está completo e se as informações estão visíveis."
)

st.warning(
    "Envie a imagem do cartão de transporte utilizado por você. "
    "Não envie somente o número do cartão ou informações escritas à mão."
)