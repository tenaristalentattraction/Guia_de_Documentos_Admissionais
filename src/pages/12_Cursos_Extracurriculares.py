import streamlit as st

st.set_page_config(page_title='3 Últimos Cursos Extracurriculares', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">3 Últimos Cursos Extracurriculares</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("Envie os certificados dos três cursos extracurriculares mais recentes que você realizou.")
st.subheader("O que conferir")
st.markdown("""
- Seu nome completo;
- Nome do curso;
- Instituição responsável;
- Data de conclusão;
- Carga horária, quando disponível;
- Boa qualidade e leitura completa da imagem.
""")
st.markdown('<div class="image-placeholder">[IMAGEM 1: exemplo de certificado de curso extracurricular]</div>', unsafe_allow_html=True)
st.warning("O certificado de formação técnica também deve ser apresentado neste campo, caso você possua.")
st.info("Se você não possuir certificados, informe seu contato no RH para que seja analisada a exigência para a vaga.")

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
