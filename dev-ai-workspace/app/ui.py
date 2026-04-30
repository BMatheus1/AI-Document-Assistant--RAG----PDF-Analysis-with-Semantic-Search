import streamlit as st
from pypdf import PdfReader
from rag import dividir_em_chunks, buscar_chunks


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
# CONFIGURAÇÃO DA PÁGINA
# ===============================================================
st.set_page_config(page_title="Dev AI Workspace", layout="wide")

st.title("🚀 Dev AI Workspace")
st.write("Assistente para leitura, divisão e busca em documentos PDF.")


# ===============================================================
# UPLOAD DO PDF
# ===============================================================
arquivo_pdf = st.file_uploader("Envie um PDF", type=["pdf"])


# ===============================================================
# PROCESSAMENTO
# ===============================================================
if arquivo_pdf is not None:
    st.success("✅ PDF carregado com sucesso!")

    texto_pdf = extrair_texto_pdf(arquivo_pdf)

    with st.expander("📄 Ver texto completo extraído"):
        st.text_area("Conteúdo do PDF", texto_pdf, height=400)

    chunks = dividir_em_chunks(texto_pdf)

    st.subheader("🧩 Chunks gerados")
    st.write(f"Total de chunks: **{len(chunks)}**")

    quantidade_exibir = st.slider(
        "Quantos chunks deseja visualizar?",
        min_value=1,
        max_value=min(len(chunks), 20),
        value=min(len(chunks), 5)
    )

    for i, chunk in enumerate(chunks[:quantidade_exibir]):
        with st.expander(f"Chunk {i + 1}"):
            st.write(chunk)

    st.divider()

    # ===============================================================
    # BUSCA NOS CHUNKS
    # ===============================================================
    st.subheader("🔍 Buscar informação no documento")

    pergunta = st.text_input(
        "Digite uma pergunta ou palavra-chave:",
        placeholder="Ex: Qual o salário do Analista de Informática?"
    )

    if pergunta:
        resultados = buscar_chunks(pergunta, chunks)

        if resultados:
            st.success(f"Foram encontrados {len(resultados)} trecho(s) relevante(s).")

            for resultado in resultados:
                numero_chunk = resultado["indice"] + 1
                pontuacao = resultado["pontuacao"]

                with st.expander(f"Resultado — Chunk {numero_chunk} | Pontuação: {pontuacao}"):
                    st.write(resultado["chunk"])
        else:
            st.warning("Nenhum trecho relevante encontrado para essa pergunta.")

else:
    st.info("📎 Faça upload de um arquivo PDF para começar.")