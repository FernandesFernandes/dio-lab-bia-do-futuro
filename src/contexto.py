import json


def montar_contexto(perfil, historico, transacoes, produtos):

    return f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔMNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index = False)}

ATENDIMENTO ANTERIORES:
{historico.to_string(index = False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent = 2, ensure_ascii = False)}
"""