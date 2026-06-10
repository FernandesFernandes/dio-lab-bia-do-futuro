import pandas as pd
import json


def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as file:
        return json.load(file)


def carregar_csv(caminho):
    return pd.read_csv(caminho)