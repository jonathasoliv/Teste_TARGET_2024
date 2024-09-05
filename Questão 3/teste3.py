import json
import os

def carregar_dados(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
        return []
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON.")
        return []

def calcular_faturamento(dados):
    valores = [item['valor'] for item in dados if item['valor'] > 0]
    
    if not valores:
        return None, None, 0

    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)

    dias_acima_media = sum(1 for item in dados if item['valor'] > media_mensal)

    return menor_valor, maior_valor, dias_acima_media

def main():
    nome_arquivo = 'faturamento.json'  # Nome do arquivo JSON
    caminho_arquivo = os.path.join('Questao 3', nome_arquivo)  # Caminho relativo
    dados = carregar_dados(caminho_arquivo)

    if not dados:
        print("Não foi possível carregar os dados ou o arquivo está vazio.")
        return

    menor_valor, maior_valor, dias_acima_media = calcular_faturamento(dados)

    if menor_valor is not None:
        print(f"Menor valor de faturamento: {menor_valor:.2f}")
        print(f"Maior valor de faturamento: {maior_valor:.2f}")
        print(f"Número de dias com faturamento superior à média mensal: {dias_acima_media}")
    else:
        print("Não há dados válidos de faturamento para calcular.")

if __name__ == "__main__":
    main()


