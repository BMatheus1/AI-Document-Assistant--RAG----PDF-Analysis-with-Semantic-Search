# 🚀 Dev AI Workspace — AI Document Assistant (RAG)

Um assistente inteligente que permite **analisar documentos PDF**, extrair informações e responder perguntas com base no conteúdo utilizando técnicas de **RAG (Retrieval-Augmented Generation)**.

---

## 📌 Visão Geral

Este projeto transforma documentos não estruturados (PDFs) em uma base consultável, permitindo:

* 📄 Upload de arquivos PDF
* 🧠 Extração de texto
* 🧩 Divisão em chunks (segmentação inteligente)
* 🔍 Busca por trechos relevantes
* 🤖 (em breve) Respostas com IA baseadas no conteúdo

---

## 🎯 Objetivo

Demonstrar na prática a construção de um sistema moderno de IA aplicado, combinando:

* Engenharia de software
* Processamento de dados
* Arquitetura de sistemas RAG
* Interface interativa com usuário

---

## 🛠️ Tecnologias Utilizadas

* Python
* Streamlit
* PyPDF
* (Em breve) ChromaDB
* (Em breve) OpenAI / LLM

---

## ⚙️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/dev-ai-workspace.git
cd dev-ai-workspace
```

### 2. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 3. Ative o ambiente

Windows (PowerShell):

```bash
.venv\Scripts\Activate.ps1
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute o projeto

```bash
streamlit run app/ui.py
```

---

## 🖥️ Funcionalidades Atuais

* ✔ Upload de PDF
* ✔ Extração de texto
* ✔ Visualização do conteúdo
* ✔ Geração de chunks
* ✔ Navegação entre chunks

---

## 🔜 Próximas Implementações

* 🔍 Busca semântica com embeddings
* 🧠 Integração com modelo de IA (LLM)
* 💬 Chat com o documento
* 📊 Avaliação de qualidade das respostas
* 🐳 Dockerização do projeto
* ☁ Deploy

---

## 📂 Estrutura do Projeto

```bash
dev-ai-workspace/
│
├── app/
│   ├── ui.py
│   ├── ingest.py
│   ├── rag.py
│   └── utils.py
│
├── data/
├── tests/
├── requirements.txt
└── README.md
```

---

## 💡 Aprendizados

Este projeto aborda conceitos importantes como:

* Manipulação de dados não estruturados
* Pipeline de processamento de texto
* Construção de sistemas baseados em recuperação de informação (RAG)
* Integração de IA em aplicações reais

---

## 👨‍💻 Autor

Matheus Brito da Silva
Desenvolvedor focado em IA aplicada e engenharia de software

---

## ⭐ Considerações Finais

Este projeto faz parte da construção de um portfólio sólido voltado para:

* Desenvolvimento de aplicações com IA
* Engenharia de Machine Learning
* Soluções modernas baseadas em dados

Se achou interessante, deixe uma ⭐ no repositório!
