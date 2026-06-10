from services.llm import perguntar
from prompts import SYSTEM_PROMPT
import streamlit as st


# ===================================================================
#                       INTERFACE
# ===================================================================

st.title("ARGOS AI  —  EDUCADOR FINANCEIRO")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))