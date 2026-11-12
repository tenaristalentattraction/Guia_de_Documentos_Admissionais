import streamlit as st

st.set_page_config(page_title='Conselho de Classe', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">Conselho de Classe</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para comprovação do registro profissional</div>', unsafe_allow_html=True)

st.write(
    "Caso sua função exija registro em Conselho de Classe, apresente a carteira "
    "profissional ou um comprovante oficial do registro no respectivo conselho."
)

st.subheader("Exemplos de Conselhos de Classe")
st.markdown("""
Dependendo da formação e da atividade profissional, o registro poderá estar vinculado a conselhos como:

- **CFT** – Conselho Federal dos Técnicos Industriais;
- **CREA** – Conselho Regional de Engenharia e Agronomia;
- **CRQ** – Conselho Regional de Química;
- Outros conselhos relacionados à formação ou atividade profissional.
""")

st.subheader("O que pode ser apresentado?")
st.markdown("""
- Carteira profissional física;
- Carteira profissional digital;
- Certidão, declaração ou comprovante oficial de registro;
- Tela ou documento emitido pelo portal do conselho, desde que identifique o profissional e o número de registro.
""")

st.markdown(
    '<div class="image-placeholder">[IMAGEM 1: exemplo de carteira ou documento de registro no CFT, CREA ou CRQ]</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="image-placeholder">[IMAGEM 2: exemplo de comprovante digital emitido pelo Conselho de Classe]</div>',
    unsafe_allow_html=True
)

st.subheader("Como obter o comprovante")
st.markdown("""
1. Acesse o site ou aplicativo oficial do conselho correspondente à sua profissão;
2. Entre na área de serviços ao profissional;
3. Procure opções como **carteira digital**, **certidão de registro**, **comprovante de registro** ou **regularidade profissional**;
4. Gere o documento ou tire um print da tela oficial;
5. Envie o arquivo ou a imagem no Lugarh.
""")

st.warning(
    "O documento deve corresponder ao conselho relacionado à sua formação ou "
    "atividade e permitir a identificação do nome e do número de registro profissional."
)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
