import streamlit as st

st.set_page_config(page_title='Comprovante de Escolaridade', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Comprovante de Escolaridade</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para comprovação da formação concluída</div>', unsafe_allow_html=True)

st.write(
    "Apresente um documento oficial que comprove a escolaridade ou formação "
    "já concluída e exigida para a vaga. Este campo é diferente da declaração "
    "de matrícula utilizada nos processos de estágio."
)

st.subheader("Quais documentos podem ser apresentados?")
st.markdown("""
Conforme seu nível de formação, podem ser apresentados:

- **Diploma;**
- **Certificado de conclusão;**
- **Histórico escolar**, quando comprovar a conclusão;
- **Declaração oficial de conclusão**, emitida pela instituição de ensino;
- Outro documento oficial da instituição que comprove a formação concluída.
""")

st.markdown(
    '<div class="image-placeholder">[IMAGEM 1: exemplo de diploma ou certificado de conclusão]</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="image-placeholder">[IMAGEM 2: exemplo de histórico escolar ou declaração oficial de conclusão]</div>',
    unsafe_allow_html=True
)

st.subheader("Como obter o documento")
st.markdown("""
- Consulte o portal acadêmico da instituição de ensino;
- Solicite o documento à secretaria da escola, faculdade ou universidade;
- Se o documento não estiver disponível online, solicite a versão digitalizada ou retire uma via presencialmente;
- Para documentos antigos, entre em contato com a instituição responsável pelo acervo escolar.
""")

st.warning(
    "Não envie apenas uma declaração de matrícula ativa neste campo. "
    "O documento deve comprovar a escolaridade ou formação concluída."
)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
