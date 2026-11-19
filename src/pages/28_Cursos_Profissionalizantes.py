import streamlit as st


st.set_page_config(
    page_title="Cursos Profissionalizantes",
    page_icon="🎓",
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
    '<div class="lugarh-title">Cursos Profissionalizantes</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="lugarh-subtitle">'
    'Orientações para o envio dos certificados'
    '</div>',
    unsafe_allow_html=True
)


# INTRODUÇÃO

st.write(
    "Apresente imagens dos certificados dos **cursos profissionalizantes** "
    "que você possui."
)


# CHECKLIST

st.markdown("### O que conferir antes do envio:")

st.markdown("""
- O certificado deve apresentar seu nome completo;
- O nome do curso deve estar visível;
- A instituição responsável deve estar identificada;
- A carga horária deve aparecer, quando informada no certificado;
- A data de conclusão deve estar legível;
- A imagem deve apresentar o certificado completo;
- Nenhuma informação deve estar cortada.
""")


# EXEMPLOS DE CURSOS

st.markdown("#### Exemplos de cursos profissionalizantes")

st.write(
    "Podem ser apresentados certificados relacionados à sua formação "
    "ou experiência profissional, como:"
)

st.markdown("""
- Cursos de qualificação profissional;
- Cursos técnicos ou operacionais;
- Cursos de mecânica, elétrica, manutenção ou produção;
- Cursos de soldagem ou inspeção;
- Cursos de segurança e qualidade;
- Cursos administrativos ou de informática;
- Outras capacitações relevantes para sua atuação profissional.
""")

st.markdown(
    """
    <div class="image-placeholder">
        IMAGEM DE REFERÊNCIA<br>
        Inserir aqui um exemplo de certificado de curso profissionalizante,
        sem dados pessoais reais.
    </div>
    """,
    unsafe_allow_html=True
)


# MAIS DE UM CERTIFICADO

st.subheader("Possui mais de um certificado?")

st.write(
    "Se você possuir mais de um curso profissionalizante, envie uma "
    "imagem para cada certificado."
)

st.info(
    "Antes do envio, organize as imagens e confira se todos os "
    "certificados estão completos e legíveis."
)


# NÃO POSSUI CURSOS

st.subheader("Não possui cursos profissionalizantes?")

st.write(
    "Não envie um documento que não corresponda ao campo apenas para "
    "concluir a pendência."
)

st.warning(
    "Caso o campo apareça como obrigatório e você não possua cursos "
    "profissionalizantes, entre em contato com o profissional de RH "
    "responsável pelo seu processo."
)


# CONFERÊNCIA FINAL

st.subheader("Confira antes de finalizar")

st.markdown("""
Confirme se cada certificado apresenta:

- Seu nome completo;
- Nome do curso;
- Nome da instituição;
- Data de conclusão;
- Carga horária, quando disponível;
- Assinatura, validação ou código de autenticidade, quando aplicável.
""")

st.warning(
    "Não envie somente uma lista com os nomes dos cursos. "
    "Anexe a imagem dos certificados ou comprovantes correspondentes."
)