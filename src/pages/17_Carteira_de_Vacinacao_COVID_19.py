import streamlit as st

st.set_page_config(page_title='Carteira de Vacinação COVID-19', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Carteira de Vacinação COVID-19</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("Para comprovar a vacinação contra a COVID-19, você pode apresentar uma das opções abaixo.")
st.markdown("""
- Foto da carteira física entregue no momento da vacinação;
- Print dos registros oficiais disponíveis no aplicativo de saúde digital do Governo Federal;
- Comprovante digital emitido pela instituição de saúde responsável pela vacinação.
""")
st.subheader("Como obter a carteira digital")
st.markdown("""
1. Entre no aplicativo com sua conta **gov.br**.
2. Acesse a área **Vacinas**.
3. Confira tipo de imunizante, doses e local de vacinação.
4. Toque em **Carteira de Vacinação Digital**.
5. O sistema gerará um documento com seus dados, vacinas e QR Code.
6. Tire prints legíveis das páginas necessárias para enviar no Lugarh.
""")
st.markdown('<div class="image-placeholder">[IMAGEM 1: acesso à área Vacinas]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 2: registros de vacinação contra COVID-19]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 3: Carteira de Vacinação Digital com QR Code]</div>', unsafe_allow_html=True)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
