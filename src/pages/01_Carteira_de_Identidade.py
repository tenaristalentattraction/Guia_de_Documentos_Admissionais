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
    '<div class="lugarh-title">Carteira de Identidade</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="lugarh-subtitle">'
    'Orientações para o envio do documento'
    '</div>',
    unsafe_allow_html=True
)


# INTRODUÇÃO

st.write(
    "Apresente imagens da **frente e do verso** da sua Carteira de Identidade."
)


# CHECKLIST

st.subheader("O que conferir antes do envio")

st.markdown("""
- Todos os dados devem estar **legíveis**;
- As imagens não devem apresentar reflexos ou sombras;
- Nenhuma informação ou parte do documento deve estar cortada;
- O número do documento deve aparecer completo, incluindo o dígito.
""")


# RG

st.subheader("RG - Modelo tradicional")

st.write(
    "Se este for o seu modelo de documento, utilize como referência:"
)

st.image(
    "src/assets/tutoriais/exemplo_rg_frente_verso.png",
    use_container_width=True
)


# CIN

st.subheader("Carteira de Identidade Nacional (CIN)")

st.write(
    "Se você já possui a nova identidade, utilize este modelo como referência:"
)

st.image(
    "src/assets/tutoriais/exemplo_cin_frente_verso.png",
    use_container_width=True
)


# CONFERÊNCIA DOS DADOS PREENCHIDOS

st.subheader("Confira também os dados preenchidos no Lugarh")

st.write(
    "Além de anexar as imagens, alguns dados do documento precisam ser "
    "preenchidos. Antes de finalizar, compare as informações "
    "digitadas com as que aparecem na sua Carteira de Identidade."
)

st.markdown("""
Confira:

- **Número do documento com dígito**;
- **Data de expedição**;
- **Órgão emissor**;
- **UF de emissão**;
""")

st.warning(
    "Os dados preenchidos no Lugarh devem corresponder às informações "
    "do documento anexado. Revise tudo antes de finalizar o envio."
)