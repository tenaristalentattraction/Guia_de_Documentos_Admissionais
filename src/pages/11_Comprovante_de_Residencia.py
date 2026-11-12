import streamlit as st

st.set_page_config(page_title='Comprovante de Residência', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Comprovante de Residência</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("Apresente um documento que contenha seu endereço completo, incluindo o CEP.")
st.subheader("Exemplos de comprovantes")
st.markdown("""
- Conta de energia;
- Conta de água;
- IPTU;
- Faturas ou outras correspondências que apresentem o endereço completo e o CEP.
""")
st.write("Se você não tiver o comprovante físico, acesse o site ou aplicativo da empresa responsável pelo serviço e obtenha a versão digital.")
st.markdown('<div class="image-placeholder">[IMAGEM 1: exemplo de comprovante com endereço completo e CEP destacados]</div>', unsafe_allow_html=True)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
