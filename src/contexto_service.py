from utils.carregador import carregar_json, carregar_csv
from contexto import montar_contexto

def obter_contexto():
    historico = carregar_csv("../data/historico_atendimento.csv")
    transacoes = carregar_csv("../data/transacoes.csv")

    perfil = carregar_json("../data/perfil_investidor.json")
    produtos = carregar_json("../data/produtos_financeiros.json")

    return montar_contexto(
        perfil,
        historico,
        transacoes,
        produtos
    )