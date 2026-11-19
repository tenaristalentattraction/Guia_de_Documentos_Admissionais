import streamlit as st

st.set_page_config(
    page_title="Cartão SUS",
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
    font-size: 2.1rem;
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


# TÍTULO

st.markdown(
    '<div class="lugarh-title">Cartão SUS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="lugarh-subtitle">'
    'Orientações para obtenção e envio do documento'
    '</div>',
    unsafe_allow_html=True
)


# INTRODUÇÃO

st.write(
    "Você pode apresentar uma foto do **Cartão SUS físico** ou um print "
    "da versão digital que mostre seu nome e o número do CNS."
)


# CARTÃO FÍSICO

st.markdown("### Cartão SUS físico")

st.write(
    "Se você possui o cartão físico, fotografe o documento de forma que "
    "as informações estejam completas e legíveis."
)

st.image(
    "src/assets/tutoriais/exemplo_cartao_sus_frente_verso.png",
    use_container_width=True
)

st.info(
    "O número do CNS está localizado no verso do cartão, identificado "
    "como **Nº do Cartão**."
)


# VERSÃO DIGITAL

st.markdown("### Não possui o cartão físico?")

st.write(
    "Você também pode consultar as informações do Cartão SUS pela versão digital."
)

with st.expander("📱 Ver como consultar pelo aplicativo"):
    
    st.markdown("""
    1. Baixe o aplicativo oficial de saúde digital do Governo Federal.
    2. Entre com sua conta **gov.br**.
    3. Na tela inicial, acesse a área do seu cartão ou dos seus dados cadastrais.
    4. Localize seu **nome completo** e o **número do CNS**.
    5. Tire um print da tela para enviar no Lugarh.
    """)

    st.image(
        "src/assets/tutoriais/cartao_sus_app_01.png",
        caption="Acesso ao Cartão SUS pelo aplicativo",
        use_container_width=True
    )

    st.image(
        "src/assets/tutoriais/cartao_sus_app_02.png",
        caption="Tela com nome e número do CNS",
        use_container_width=True
    )

    st.warning(
        "O print deve mostrar claramente seu nome e o número do CNS."
    )


# CONFERÊNCIA DO FORMULÁRIO

st.markdown("### Confira também os dados preenchidos no Lugarh")

st.write(
    "Além de anexar a imagem do documento, você deverá informar "
    "o número do seu CNS no formulário."
)

st.markdown("""
Confira:

- **Número do CNS**.
""")

st.warning(
    "O número preenchido no Lugarh deve corresponder ao número apresentado "
    "no documento anexado. Revise a informação antes de finalizar o envio."
)