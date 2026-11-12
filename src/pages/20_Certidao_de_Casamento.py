import streamlit as st

st.set_page_config(page_title='Certidão de Casamento', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Certidão de Casamento</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write(
    "Apresente uma imagem legível e completa da sua Certidão de Casamento. "
    "O documento deve permitir a leitura dos nomes, da data do registro e "
    "das demais informações da certidão."
)

st.subheader("Se você já possui a certidão")
st.markdown("""
- Fotografe ou digitalize o documento completo;
- Inclua todas as páginas ou lados que contenham informações;
- Não corte bordas, nomes, datas, averbações ou carimbos;
- Verifique se eventuais anotações ou averbações estão legíveis.
""")

st.markdown(
    '<div class="image-placeholder">[IMAGEM 1: exemplo de Certidão de Casamento completa e legível]</div>',
    unsafe_allow_html=True
)

st.subheader("Como solicitar uma segunda via")
st.markdown("""
Caso não tenha mais o documento:

1. Entre em contato com o Cartório de Registro Civil onde o casamento foi registrado;
2. Verifique se o cartório permite a solicitação online;
3. Informe os dados solicitados para localizar o registro;
4. Escolha o formato disponível, digital ou impresso;
5. Após receber a certidão, envie uma imagem legível no Lugarh.
""")

st.markdown(
    '<div class="image-placeholder">[IMAGEM 2: exemplo de solicitação online de segunda via da Certidão de Casamento]</div>',
    unsafe_allow_html=True
)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
