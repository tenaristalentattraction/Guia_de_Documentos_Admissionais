import streamlit as st

st.set_page_config(page_title='Comprovante de CPF Regular', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Comprovante de CPF Regular</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("Consulte a situação cadastral do CPF no site oficial da Receita Federal e envie um print do comprovante emitido.")
st.subheader("Passo a passo")
st.markdown("""
1. Acesse a consulta de situação cadastral do CPF no site oficial da Receita Federal.
2. Preencha os dados solicitados.
3. Realize a consulta.
4. Confira o resultado apresentado.
5. Tire um print da tela do comprovante para enviar no Lugarh.
""")
st.markdown('<div class="image-placeholder">[IMAGEM 1: formulário de consulta da situação cadastral do CPF]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 2: comprovante emitido com a situação cadastral]</div>', unsafe_allow_html=True)
st.error("Se a situação aparecer como Pendente de Regularização, Suspenso, Cancelado ou Nulo, entre em contato com a Receita Federal e avise o RH.")

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
