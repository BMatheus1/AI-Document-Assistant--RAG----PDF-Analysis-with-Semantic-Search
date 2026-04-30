def dividir_em_chunks(texto, tamanho=800, sobreposicao=100):
    """
    Divide o texto em partes menores para busca semântica.
    """
    chunks = []
    inicio = 0

    while inicio < len(texto):
        fim = inicio + tamanho
        chunk = texto[inicio:fim]
        chunks.append(chunk)
        inicio += tamanho - sobreposicao

    return chunks