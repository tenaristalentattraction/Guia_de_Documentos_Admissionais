import streamlit as st

st.set_page_config(page_title='CNIS', page_icon="📄", layout="wide")

st.markdown("""
<style>
.block-container { max-width: 1050px; padding-top: 2rem; padding-bottom: 3rem; }
.lugarh-title { color: #000097; font-size: 2.1rem; font-weight: 750; margin-bottom: .25rem; }
.lugarh-subtitle { color: #666666; font-size: 1.05rem; margin-bottom: 1.5rem; }
.image-placeholder { border: 2px dashed #9aa4b2; border-radius: 10px; padding: 22px; text-align: center; color: #59636e; background: #f6f8fa; margin: 12px 0 20px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="lugarh-title">CNIS</div>', unsafe_allow_html=True)
st.markdown('<div class="lugarh-subtitle">Orientações para obtenção e envio do documento</div>', unsafe_allow_html=True)

st.write("O CNIS, Cadastro Nacional de Informações Sociais, pode ser consultado pelo site ou aplicativo Meu INSS. O documento apresenta vínculos, remunerações e contribuições registradas em seu histórico previdenciário.")

st.subheader("Como acessar o CNIS")
st.markdown("""
1. Acesse o site ou aplicativo **Meu INSS**.
2. Selecione **Entrar com gov.br**.
3. Digite seu CPF e toque em **Continuar**.
4. Informe sua senha e conclua o acesso.
5. Autorize o uso dos dados pessoais, caso a solicitação seja apresentada.
6. Permita o registro do aparelho, quando necessário.
7. Na tela inicial, procure por **Extrato de Contribuição (CNIS)**.
8. Abra o extrato e tire prints legíveis das informações solicitadas.
""")

st.markdown('<div class="image-placeholder">[IMAGEM 1: acesso ao site ou aplicativo Meu INSS]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 2: tela Entrar com gov.br e preenchimento do CPF]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 3: tela para preenchimento da senha]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 4: autorização para uso de dados pessoais]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 5: opção para permitir o registro do aparelho]</div>', unsafe_allow_html=True)
st.markdown('<div class="image-placeholder">[IMAGEM 6: opção Extrato de Contribuição CNIS na tela inicial]</div>', unsafe_allow_html=True)

st.subheader("Se não houver informações vinculadas")
st.write("Caso o Meu INSS informe que não existem dados vinculados ao seu CPF, tire um print da mensagem apresentada e envie essa imagem no Lugarh.")

st.info("O extrato CNIS também pode ser utilizado como comprovante do número do PIS. No documento, o número poderá aparecer como NIT.")
st.warning("Em caso de primeiro emprego e ausência de cadastro ativo, informe seu contato no RH para que a situação seja analisada.")

st.divider()
st.info("Antes de enviar, confira se todas as informações estão legíveis e se a imagem não está cortada.")
