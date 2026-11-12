import streamlit as st

st.set_page_config(page_title='Certidão de Nascimento', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Certidão de Nascimento</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("Apresente uma imagem legível da sua Certidão de Nascimento. Caso não possua o documento, solicite uma segunda via no cartório do registro ou pela plataforma oficial do Registro Civil.")

st.subheader("Solicitação online da segunda via")
st.markdown("""
1. Acesse o site oficial do **Registro Civil**.
2. Escolha a opção **Nascimento** e entre com sua conta **gov.br**.
3. Selecione onde deseja receber o código de segurança.
4. Acesse **Pedidos de certidões**.
5. Informe estado, cidade, cartório e os demais dados solicitados.
6. Conclua o pedido e aguarde a emissão.
7. Quando receber o documento, tire imagens legíveis das páginas para enviar no Lugarh.
""")
st.markdown('<div class="image-placeholder">[IMAGEM 1: página do Registro Civil com a opção Nascimento destacada]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 2: tela de entrada com gov.br]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 3: escolha do método para receber o código de segurança]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 4: opção Pedidos de certidões]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 5: formulário para preenchimento dos dados da certidão]</div>', unsafe_allow_html=True)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
