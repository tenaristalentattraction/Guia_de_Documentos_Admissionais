import streamlit as st

st.set_page_config(page_title='CTPS - Todos os Registros', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">CTPS - Todos os Registros</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("Após entrar na Carteira de Trabalho Digital, consulte seus dados pessoais, últimas anotações e contratos de trabalho.")
st.subheader("Como exportar")
st.markdown("""
1. No rodapé do aplicativo, acesse **Contratos** para visualizar os vínculos empregatícios.
2. Responda às perguntas de segurança, caso sejam apresentadas.
3. Acesse a opção **Enviar** ou **Exportar CTPS**.
4. Selecione os dados pessoais e todos os contratos de trabalho.
5. Toque em **Compartilhar** para gerar o documento.
6. Como o Lugarh recebe imagens, tire prints de todas as páginas necessárias.
""")
st.markdown('<div class="image-placeholder">[IMAGEM 1: tela com vínculos e contratos de trabalho]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 2: seleção dos itens para exportação da CTPS]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 3: exemplo do documento exportado]</div>', unsafe_allow_html=True)

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
