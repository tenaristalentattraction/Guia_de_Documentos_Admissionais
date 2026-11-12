import streamlit as st

st.set_page_config(page_title='Diploma ou Declaração de Matrícula', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Diploma ou Declaração de Matrícula</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.subheader("Diploma ou comprovante de escolaridade")
st.write("Apresente diploma, certificado ou declaração oficial que comprove seu nível de escolaridade: Ensino Fundamental, Médio ou Superior. O documento deve ser emitido pela instituição de ensino e conter identificação oficial da instituição.")

st.subheader("Declaração de matrícula")
st.write("Solicite a declaração à secretaria do curso ou faça o download pela plataforma da instituição. O documento deve confirmar que sua matrícula está ativa no ano vigente.")

st.markdown('<div class="image-placeholder">[IMAGEM 1: exemplo de diploma ou declaração oficial de escolaridade]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 2: exemplo de declaração de matrícula ativa]</div>', unsafe_allow_html=True)
st.warning("Certificados de curso técnico devem ser enviados no campo de Cursos Extracurriculares.")

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
