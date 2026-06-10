# 🚀 Argos AI

<div align="center">

<img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/Ollama-Local_LLM-green?style=for-the-badge">
<img src="https://img.shields.io/badge/AI-Finance-orange?style=for-the-badge">

### Seu Consultor Financeiro Inteligente com IA Local

Assistente virtual especializado em educação financeira, investimentos e planejamento financeiro pessoal, utilizando Inteligência Artificial Local através do Ollama.

</div>

---

# 📖 Sobre o Projeto

O **Argos AI** é um assistente financeiro inteligente desenvolvido para fornecer orientações educacionais sobre finanças pessoais e investimentos.

O projeto utiliza modelos de linguagem executados localmente através do **Ollama**, combinados com uma base de conhecimento personalizada para oferecer respostas contextualizadas e alinhadas ao perfil do investidor.

O objetivo é democratizar o acesso à educação financeira por meio de uma experiência conversacional simples, segura e personalizada.

---

# ✨ Principais Funcionalidades

✅ Chat financeiro inteligente

✅ Integração com modelos locais via Ollama

✅ Personalização por perfil de investidor

✅ Histórico de conversas

✅ Contextualização por arquivos JSON e CSV

✅ Recomendações educacionais sobre investimentos

✅ Interface amigável com Streamlit

✅ Arquitetura modular e escalável

---

# 🧠 Como Funciona

O Argos AI utiliza uma arquitetura baseada em:

1. Coleta de informações do usuário
2. Carregamento de dados financeiros estruturados
3. Construção de contexto personalizado
4. Geração de respostas através de um LLM local
5. Exibição da resposta em interface Streamlit

Fluxo simplificado:

```text
Usuário
   │
   ▼
Streamlit
   │
   ▼
Context Builder
   │
   ▼
Base de Conhecimento
(JSON + CSV)
   │
   ▼
Prompt Engineering
   │
   ▼
Ollama
   │
   ▼
Resposta Inteligente
```

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia         | Finalidade            |
| ------------------ | --------------------- |
| Python             | Backend               |
| Streamlit          | Interface Web         |
| Ollama             | Execução Local de LLM |
| JSON               | Perfil do Investidor  |
| CSV                | Histórico e Dados     |
| Requests           | Comunicação com APIs  |
| Prompt Engineering | Contextualização      |

---

# 📂 Estrutura do Projeto

```text
ArgosAI/
│
├── data/
│   ├── perfil_investidor.json
│   ├── historico_atendimento.csv
│   └── conhecimentos_financeiros.json
│
├── src/
│   ├── app.py
│   ├── contexto.py
│   ├── prompts.py
│   │
│   └── utils/
│       ├── carregador.py
│       └── helpers.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Instalação

## 1 - Clone o projeto

```bash
git clone https://github.com/FernandesFernandes/dio-lab-bia-do-futuro.git

cd dio-lab-bia-do-futuro
```

## 2 - Crie um ambiente virtual

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## 3 - Instale as dependências

```bash
pip install -r requirements.txt
```

---

# 🤖 Configurando o Ollama

Instale o Ollama:

https://ollama.com

Baixe o modelo desejado:

```bash
ollama pull gpt-oss
```

ou

```bash
ollama pull llama3
```

Inicie o servidor:

```bash
ollama serve
```

---

# ▶️ Executando a Aplicação

```bash
streamlit run src/app.py
```

A aplicação estará disponível em:

```text
http://localhost:8501
```

---

# 🎯 Casos de Uso

* Educação Financeira
* Planejamento Financeiro
* Reserva de Emergência
* Perfil de Investidor
* Introdução aos Investimentos
* Simulação de Cenários Financeiros
* Orientação para iniciantes

---

# 🔒 Privacidade

Uma das principais vantagens do Argos AI é a utilização de modelos executados localmente.

Isso significa:

* Maior privacidade
* Menor dependência de serviços externos
* Controle dos dados
* Redução de custos com APIs pagas

---

# 🚧 Roadmap

* [ ] Integração com banco de dados
* [ ] Memória vetorial
* [ ] Upload de documentos financeiros
* [ ] Dashboard de investimentos
* [ ] Integração com APIs financeiras
* [ ] Múltiplos perfis de usuários
* [ ] Geração de relatórios financeiros

---

# 👨‍💻 Autor

### Fernando Fernandes

Desenvolvedor apaixonado por:

* Inteligência Artificial
* Python
* Automação
* Engenharia de Software
* Soluções Financeiras

GitHub:
https://github.com/FernandesFernandes

---

# ⭐ Apoie o Projeto

Se este projeto foi útil para você:

⭐ Deixe uma estrela no repositório

🍴 Faça um fork

🛠️ Contribua com melhorias

📢 Compartilhe com a comunidade

---

<div align="center">

### Argos AI

### Inteligência Artificial aplicada à Educação Financeira

</div>
