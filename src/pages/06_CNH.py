import streamlit as st

st.set_page_config(page_title='CNH', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">CNH</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("Apresente uma foto legível da sua Carteira Nacional de Habilitação. Você pode utilizar a versão física ou a versão digital disponível no aplicativo Carteira Digital de Trânsito.")

st.subheader("Envio da CNH física")
st.markdown("""
- Fotografe a frente e o verso do documento, quando aplicável;
- Garanta que seu nome, número do documento, categoria e validade estejam legíveis;
- Evite reflexos, sombras e partes cortadas;
- Verifique se a imagem está nítida antes de enviar.
""")

st.markdown('<div class="image-placeholder">[IMAGEM 1: exemplo de foto legível da CNH física]</div>', unsafe_allow_html=True)

st.subheader("Como acessar a CNH Digital")
st.markdown("""
1. Baixe o aplicativo **Carteira Digital de Trânsito**.
2. Entre com sua conta **gov.br**.
3. Conclua as etapas de cadastro e validação solicitadas pelo aplicativo.
4. Acesse a área de documentos.
5. Abra sua CNH Digital.
6. Tire um print da tela com os dados do documento para enviar no Lugarh.
""")

st.markdown('<div class="image-placeholder">[IMAGEM 2: tela inicial do aplicativo Carteira Digital de Trânsito]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 3: área de documentos com acesso à CNH Digital]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 4: tela da CNH Digital com os dados do documento]</div>', unsafe_allow_html=True)

st.warning("Caso você não possua habilitação, informe seu contato no RH. A exigência será analisada de acordo com a vaga e, quando não for obrigatória, a cobrança poderá ser retirada do sistema.")

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
