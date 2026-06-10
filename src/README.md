## ArgosAI

Chatbot educador financeiro desenvolvido com Python, Streamlit e Ollama.

## Estrutura do Projeto

```text
ArgosAI/
│
├── data/
│   ├── historico_atendimento.csv      # Histórico de atendimentos
│   ├── perfil_investidor.json         # Perfil do cliente
│   ├── produtos_financeiros.json      # Produtos financeiros disponíveis
│   └── transacoes.csv                 # Histórico de transações
│
└── src/
    │
    ├── app.py                         # Interface Streamlit
    ├── contexto.py                    # Montagem do contexto para a IA
    ├── prompts.py                     # Prompt do sistema
    │
    ├── services/
    │   ├── contexto_service.py        # Carrega e prepara os dados
    │   └── llm.py                     # Integração com Ollama
    │
    └── utils/
        └── carregador.py              # Leitura de CSV e JSON
```

```
streamlit
openai
python-dotenv

```
# Rodar a aplicação
streamlit run app.py

```
