import streamlit as st

st.set_page_config(page_title='Conta Corrente Itaú', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Conta Corrente Itaú</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("Apresente um documento original do banco que mostre claramente seu nome, agência e conta. A conta pode ser corrente ou poupança.")
st.subheader("Comprovantes aceitos")
st.markdown("""
- Foto do cartão da conta;
- Print do aplicativo Itaú com identificação, agência e conta;
- E-mail enviado pelo Itaú após a aprovação da conta, contendo agência e conta.
""")
st.markdown('<div class="image-placeholder">[IMAGEM 1: exemplo de cartão com agência e conta]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 2: tela do aplicativo Itaú com nome, agência e conta]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 3: e-mail de abertura com agência e conta]</div>', unsafe_allow_html=True)
st.error("Não são aceitas informações manuscritas, conta de terceiros ou conta-salário de outra empresa.")
st.info("Caso não possua conta Itaú, será necessário abrir uma conta. Para conta-salário, solicite ao RH a carta para apresentação ao banco.")

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
