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
# FUNÇÃO – BUSCAR CHUNKS POR PALAVRAS-CHAVE
# ===============================================================
def buscar_chunks(pergunta, chunks, top_k=3):
    """
    Busca simples por palavras-chave.
    Retorna os chunks mais relacionados com a pergunta.
    """

    palavras_pergunta = pergunta.lower().split()
    resultados = []

    for indice, chunk in enumerate(chunks):
        chunk_lower = chunk.lower()

        pontuacao = 0

        for palavra in palavras_pergunta:
            if palavra in chunk_lower:
                pontuacao += 1

        if pontuacao > 0:
            resultados.append({
                "indice": indice,
                "chunk": chunk,
                "pontuacao": pontuacao
            })

    resultados = sorted(
        resultados,
        key=lambda item: item["pontuacao"],
        reverse=True
    )

    return resultados[:top_k]