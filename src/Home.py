from pathlib import Path
import tomllib
import streamlit as st

# ==================================================
# CONFIG
# ==================================================

CONFIG_FILE = Path(__file__).parent / "config.toml"

with open(CONFIG_FILE, "rb") as file:
    config = tomllib.load(file)

portal = config.get("portal", {})
contact = config.get("contact", {})
assets = config.get("assets", {})

BASE_DIR = Path(__file__).parent

logo_path = BASE_DIR / assets["logo"]
hero_path = BASE_DIR / assets["hero"]

# ==================================================
# STREAMLIT
# ==================================================

st.set_page_config(
    page_title=portal["title"],
    page_icon="📄",
    layout="wide"
)

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

.block-container{
    padding-top:0rem;
    max-width:1100px;
}

.hero-img img{
    border-radius:0px 0px 12px 12px;
}

.section{
    padding-top:1rem;
    padding-bottom:1rem;
}

.info-card{
    background:#ffffff;
    border:1px solid #e6eaf0;
    border-radius:12px;
    padding:18px;
    margin-bottom:12px;
}

.category-card{
    background:white;
    border:1px solid #dbe2f0;
    border-left:5px solid #000097;
    border-radius:12px;
    padding:18px;
    margin-bottom:12px;
    font-weight:600;
}

.contact-box{
    background:#f3f6fd;
    border-radius:12px;
    padding:18px;
}

.hero-banner img {
    height: 180px !important;
    width: 100% !important;
    object-fit: cover !important;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HERO
# ==================================================

st.markdown('<div class="hero-banner">', unsafe_allow_html=True)

st.image(
    str(hero_path),
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div style="
        background:#000097;
        color:white;
        padding:18px 24px;
        border-radius:0 0 12px 12px;
        margin-bottom:25px;
    ">
        <h1 style="
            margin:0;
            font-size:2rem;
            font-weight:700;
        ">
            Guia de Documentos Admissionais
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    Bem-vindo(a)!

    Este portal reúne orientações para auxiliar no envio correto dos documentos
    admissionais solicitados durante o seu processo de contratação.
    """
)

# ==================================================
# PESQUISA (FUTURA)
# ==================================================

documentos = {
    "Carteira de Identidade": "pages/01_Carteira_de_Identidade.py",
    "Cartão SUS": "pages/02_Cartao_SUS.py",
    "Certidão de Nascimento": "pages/03_Certidao_de_Nascimento.py",
    "Diploma ou Declaração de Matrícula": "pages/04_Diploma_ou_Declaracao_de_Matricula.py",
    "CNIS": "pages/05_CNIS.py",
    "CNH": "pages/06_CNH.py",
    "PIS": "pages/07_PIS.py",
    "CTPS Digital": "pages/08_CTPS_Digital.py",
    "CTPS - Todos os Registros": "pages/09_CTPS_Todos_os_Registros.py",
    "Conta Corrente Itaú": "pages/10_Conta_Corrente_Itau.py",
    "Comprovante de Residência": "pages/11_Comprovante_de_Residencia.py",
    "3 Últimos Cursos Extracurriculares": "pages/12_Cursos_Extracurriculares.py",
    "Foto 5x7": "pages/13_Foto_5x7.py",
    "Título Eleitoral": "pages/14_Titulo_Eleitoral.py",
    "Comprovante de CPF Regular": "pages/15_Comprovante_de_CPF_Regular.py",
    "Carteira de Vacinação": "pages/16_Carteira_de_Vacinacao.py",
    "Carteira de Vacinação COVID-19": "pages/17_Carteira_de_Vacinacao_COVID_19.py",
    "CTPS Física": "pages/18_CTPS_Fisica.py",
    "Comprovante de Escolaridade": "pages/19_Comprovante_de_Escolaridade.py",
    "Certidão de Casamento": "pages/20_Certidao_de_Casamento.py",
    "Certificado de Reservista": "pages/21_Certificado_de_Reservista.py",
    "Conselho de Classe": "pages/22_Conselho_de_Classe.py",
    "Contribuição Sindical": "pages/23_Contribuicao_Sindical.py",
    "CPF": "pages/24_CPF.py",
    "Cartão Transporte URBS": "pages/25_Cartao_Transporte_URBS.py",
    "Certificação ABENDI / FBTS": "pages/26_Certificacao_Abendi_FBTS.py",
    "Currículo": "pages/27_Curriculo.py",
    "Cursos Profissionalizantes": "pages/28_Cursos_Profissionalizantes.py",
}

documento_escolhido = st.selectbox(
    "🔎 Pesquisar documento",
    options=list(documentos.keys()),
    index=None,
    placeholder="Ex.: CNIS, RG, CTPS..."
)

if documento_escolhido:
    st.switch_page(documentos[documento_escolhido])
st.info(
    """
    🔍 Procurando um documento específico?

    Utilize o campo de pesquisa acima para localizar rapidamente um documento
    ou navegue pelas categorias no menu lateral para visualizar todas as orientações
    disponíveis.
    """
)

st.divider()

# ==================================================
# ORIENTAÇÕES GERAIS
# ==================================================

st.header("Orientações Gerais")

st.markdown("""
<div class='info-card'>
📅 Respeite os prazos informados pela equipe de RH.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='info-card'>
📷 Utilize imagens completas e legíveis.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='info-card'>
✅ Sempre confira os dados antes de realizar o envio.
</div>
""", unsafe_allow_html=True)

st.divider()

# ==================================================
# FAQ
# ==================================================

st.header("Precisa de ajuda?")

with st.expander("Não possuo CNH. O que devo fazer?"):
    st.write(
        "Entre em contato com a equipe de RH para avaliação da exigência do documento para sua vaga."
    )

with st.expander("Não possuo cursos extracurriculares."):
    st.write(
        "Informe a equipe de RH para análise da obrigatoriedade do documento."
    )

with st.expander("Nunca trabalhei. Como apresento PIS ou CNIS?"):
    st.write(
        "Consulte o tutorial do documento correspondente para verificar as orientações para primeiro emprego."
    )

with st.expander("Não encontrei informações vinculadas ao meu CPF."):
    st.write(
        """
        Consulte o tutorial do documento solicitado.

        Em alguns casos será necessário apresentar
        um print comprovando a ausência da informação.
        """
    )

with st.expander("Estou com dúvidas sobre uma pendência específica."):
    st.write(
        f"Entre em contato com a nossa Equipe de Atração de Talentos via WhatsApp."
    )
