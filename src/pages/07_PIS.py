import streamlit as st

st.set_page_config(
    page_title="PIS",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
<style>
.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.lugarh-title {
    color: #000097;
    font-size: 2.1rem;
    font-weight: 750;
    margin-bottom: .25rem;
}

.lugarh-subtitle {
    color: #666666;
    font-size: 1.05rem;
    margin-bottom: 1.5rem;
}

.image-placeholder {
    border: 2px dashed #9aa4b2;
    border-radius: 10px;
    padding: 22px;
    text-align: center;
    color: #59636e;
    background: #f6f8fa;
    margin: 12px 0 20px 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="lugarh-title">PIS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="lugarh-subtitle">'
    'Orientações para consulta e envio do número do PIS'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "O número do PIS pode ser consultado pelo aplicativo Meu INSS. "
    "Caso você já possua um número cadastrado, apresente essa informação "
    "no Lugarh. Se ainda não houver PIS vinculado ao seu CPF, também será "
    "necessário apresentar a tela que comprova essa situação."
)

st.subheader("Como consultar o PIS")

st.markdown("""
1. Baixe o aplicativo **Meu INSS** no seu celular.
2. Acesse o aplicativo utilizando sua conta **gov.br** e informe seu CPF.
3. Após entrar, consulte seus dados cadastrais e verifique se existe um número de **PIS** vinculado ao seu CPF.
4. Se houver um número cadastrado, tire um print da tela em que a informação aparece e apresente no **Lugarh**.
5. Se não houver PIS cadastrado para o seu CPF, o aplicativo informará que não há registro disponível. Nesse caso, tire um print dessa mensagem e apresente-o no **Lugarh**.
""")

st.markdown(
    '<div class="image-placeholder">'
    '[IMAGEM 1: tela de acesso ao aplicativo Meu INSS]'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="image-placeholder">'
    '[IMAGEM 2: tela do Meu INSS mostrando o número do PIS cadastrado]'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="image-placeholder">'
    '[IMAGEM 3: tela do Meu INSS informando que não há PIS cadastrado para o CPF]'
    '</div>',
    unsafe_allow_html=True
)

st.info(
    "Não encontrou um número de PIS cadastrado? Não tem problema. "
    "Faça um print da mensagem apresentada no Meu INSS e envie essa imagem "
    "no Lugarh como comprovação."
)

st.subheader("Outras formas de comprovar o número do PIS")

st.write(
    "Caso você já possua o número do PIS em outro documento, também poderá "
    "utilizá-lo como comprovante."
)

st.markdown("""
São aceitos:

- **Cartão Cidadão**, desde que o número do PIS esteja visível;
- **Extrato CNIS**, no qual o número correspondente poderá aparecer identificado como **NIT**.

Ambos podem ser utilizados como alternativa ao cartão do PIS.
""")

st.markdown(
    '<div class="image-placeholder">'
    '[IMAGEM 4: exemplo de onde localizar o número no Cartão Cidadão]'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="image-placeholder">'
    '[IMAGEM 5: exemplo do Extrato CNIS indicando onde localizar o número NIT]'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

st.info(
    "Antes de enviar, confira se seu nome, CPF e o número do PIS/NIT, "
    "quando existente, estão legíveis e se a imagem não está cortada."
)
