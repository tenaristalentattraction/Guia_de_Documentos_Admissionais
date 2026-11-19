import streamlit as st


st.set_page_config(
    page_title="Certificação ABENDI / FBTS",
    page_icon="📜",
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
    '<div class="lugarh-title">Certificação ABENDI / FBTS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="lugarh-subtitle">'
    'Orientações para o envio de certificações técnicas'
    '</div>',
    unsafe_allow_html=True
)


# INTRODUÇÃO

st.write(
    "Este campo é destinado ao envio de certificações profissionais "
    "emitidas ou reconhecidas pela **ABENDI** ou pela **FBTS**, quando "
    "aplicáveis à função para a qual você está sendo contratado(a)."
)

st.info(
    "Essas certificações são normalmente relacionadas a atividades "
    "técnicas de inspeção, soldagem e Ensaios Não Destrutivos (END)."
)


# O QUE ENVIAR

st.markdown("### O que enviar:")

st.markdown("""
- Imagem do certificado correspondente à qualificação informada;
- Frente e verso, caso existam informações nos dois lados;
- Documento completo, sem cortes;
- Certificação dentro do prazo de validade, quando houver;
- Imagem na qual seja possível identificar o nome do profissional,
  o tipo de certificação e a entidade emissora.
""")


# EXEMPLOS DE CERTIFICAÇÕES

st.markdown("#### Exemplos de certificações relacionadas")

st.write(
    "Dependendo da atividade e dos requisitos da vaga, o campo pode "
    "abranger certificações relacionadas a:"
)

st.markdown("""
- Ensaios Não Destrutivos (END);
- Partículas Magnéticas;
- Líquido Penetrante;
- Ultrassom;
- Ensaio Visual;
- Radiografia;
- Inspetor de Soldagem;
- Inspetor de Dutos;
- Outras qualificações técnicas emitidas pela ABENDI ou FBTS.
""")

st.markdown(
    """
    <div class="image-placeholder">
        IMAGEM DE REFERÊNCIA<br>
        Inserir aqui um exemplo ilustrativo de certificado ABENDI ou FBTS,
        sem dados pessoais reais.
    </div>
    """,
    unsafe_allow_html=True
)


# NÃO POSSUI CERTIFICAÇÃO

st.subheader("Não possui certificação ABENDI ou FBTS?")

st.write(
    "Este tipo de certificação é aplicável apenas a determinadas funções. "
    "Se o campo aparecer em seu perfil e você não possuir a certificação, "
    "não envie um certificado de curso diferente apenas para preencher "
    "a pendência."
)

st.warning(
    "Entre em contato com o profissional de RH responsável pelo seu "
    "processo para confirmar se a certificação é exigida para a vaga."
)


# CONFERÊNCIA FINAL

st.subheader("Confira antes de finalizar")

st.markdown("""
Confirme se o certificado apresenta:

- Seu nome completo;
- Nome ou tipo da certificação;
- Nível da qualificação, quando aplicável;
- Nome ou identificação da ABENDI ou FBTS;
- Número de registro ou certificação, quando houver;
- Data de emissão;
- Data de validade, quando houver.
""")

st.warning(
    "Não envie certificados sem relação com o campo. Certificados de "
    "outros cursos devem ser anexados em Cursos Profissionalizantes ou "
    "Cursos Extracurriculares, conforme a solicitação exibida no Lugarh."
)