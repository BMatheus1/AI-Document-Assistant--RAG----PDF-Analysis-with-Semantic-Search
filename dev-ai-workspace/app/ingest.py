from pypdf import PdfReader


def extrair_texto_pdf(uploaded_file):
    """
    Lê um PDF enviado pelo usuário e retorna o texto completo.
    """
    reader = PdfReader(uploaded_file)
    texto_paginas = []

    for pagina in reader.pages:
        texto = pagina.extract_text()
        if texto:
            texto_paginas.append(texto)

    return "\n".join(texto_paginas)