import streamlit as st
from pypdf import PdfReader
# ===============================================================
# FUNÇÃO – EXTRAIR TEXTO DO PDF
# ===============================================================
def extrair_texto_pdf(arquivo):
    leitor = PdfReader(arquivo)
    texto = ""

    for pagina in leitor.pages:
        texto += pagina.extract_text() or ""

    return texto


# ===============================================================
# FUNÇÃO – DIVIDIR TEXTO EM CHUNKS
# ===============================================================
def dividir_em_chunks(texto, tamanho=500):
    palavras = texto.split()
    chunks = []

    for i in range(0, len(palavras), tamanho):
        chunk = " ".join(palavras[i:i + tamanho])
        chunks.append(chunk)

    return chunks


# ===============================================================
# CONFIGURAÇÃO DA PÁGINA
# ===============================================================
st.set_page_config(page_title="Leitor de PDF com Chunks", layout="wide")

st.title("📄 Leitor de PDF + Chunking")
st.write("Faça upload de um PDF para visualizar o texto e os chunks gerados.")


# ===============================================================
# UPLOAD DO PDF
# ===============================================================
arquivo_pdf = st.file_uploader("Envie um PDF", type=["pdf"])


# ===============================================================
# PROCESSAMENTO
# ===============================================================
if arquivo_pdf is not None:

    st.success("✅ PDF carregado com sucesso!")

    # Extrair texto
    texto_pdf = extrair_texto_pdf(arquivo_pdf)

    # -----------------------------------------------------------
    # TEXTO COMPLETO (ESCONDIDO)
    # -----------------------------------------------------------
    with st.expander("📄 Ver texto completo extraído"):
        st.text_area("Conteúdo do PDF", texto_pdf, height=400)

    # -----------------------------------------------------------
    # GERAR CHUNKS
    # -----------------------------------------------------------
    chunks = dividir_em_chunks(texto_pdf)

    st.subheader("🧩 Chunks gerados")
    st.write(f"Total de chunks: **{len(chunks)}**")

    # -----------------------------------------------------------
    # CONTROLE DE EXIBIÇÃO
    # -----------------------------------------------------------
    quantidade_exibir = st.slider(
        "Quantos chunks deseja visualizar?",
        min_value=1,
        max_value=min(len(chunks), 20),
        value=min(len(chunks), 5)
    )

    # -----------------------------------------------------------
    # EXIBIR CHUNKS
    # -----------------------------------------------------------
    for i, chunk in enumerate(chunks[:quantidade_exibir]):
        with st.expander(f"Chunk {i + 1}"):
            st.write(chunk)

else:
    st.info("📎 Faça upload de um arquivo PDF para começar.")