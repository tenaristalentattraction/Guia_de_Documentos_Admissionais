import streamlit as st


st.set_page_config(
    page_title="Currículo",
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
    '<div class="lugarh-title">Currículo</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="lugarh-subtitle">'
    'Orientações para o envio do currículo'
    '</div>',
    unsafe_allow_html=True
)


# INTRODUÇÃO

st.write(
    "Apresente uma imagem legível e atualizada do seu **currículo**."
)


# CHECKLIST

st.markdown("### O que conferir antes do envio:")

st.markdown("""
- Seu nome completo deve estar correto;
- O telefone e o e-mail devem estar atualizados;
- As informações de formação acadêmica devem estar completas;
- As experiências profissionais devem estar atualizadas;
- Cursos e certificações relevantes podem ser incluídos;
- Todas as páginas devem estar legíveis;
- Nenhuma parte do currículo deve estar cortada.
""")


# CONTEÚDO DO CURRÍCULO

st.markdown("#### Informações recomendadas")

st.write(
    "Antes de gerar a imagem, revise se o currículo apresenta, quando aplicável:"
)

st.markdown("""
- **Dados de contato:** telefone e e-mail;
- **Objetivo profissional** ou área de interesse;
- **Formação acadêmica:** curso, instituição e período;
- **Experiências profissionais:** empresa, função e período;
- **Cursos e certificações relevantes**;
- **Conhecimentos técnicos e idiomas**, quando aplicável.
""")

st.markdown(
    """
    <div class="image-placeholder">
        IMAGEM DE REFERÊNCIA<br>
        Inserir aqui um exemplo visual de currículo organizado,
        sem informações pessoais reais.
    </div>
    """,
    unsafe_allow_html=True
)


# MAIS DE UMA PÁGINA

st.subheader("Currículo com mais de uma página")

st.write(
    "Se o currículo possuir mais de uma página, transforme cada página "
    "em uma imagem e anexe todas as páginas na ordem correta."
)


# CONFERÊNCIA FINAL

st.subheader("Confira antes de finalizar")

st.markdown("""
Antes de realizar o envio:

- Verifique se nenhuma página está faltando;
- Confira se o texto está legível;
- Confirme se os dados de contato estão atualizados;
- Remova informações desatualizadas;
- Organize as imagens na ordem correta.
""")

st.warning(
    "Não envie currículo desfocado, cortado ou com informações de "
    "contato desatualizadas."
)