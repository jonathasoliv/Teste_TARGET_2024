def calcular_percentuais(faturamentos):
    # Calcula o percentual de representação de cada estado no valor total.

    total = sum(faturamentos.values())

    if total == 0:
        raise ValueError("O valor total de faturamento não pode ser zero.")

    percentuais = {estado: (valor / total) * 100 for estado,
                   valor in faturamentos.items()}
    return percentuais


def exibir_percentuais(percentuais):
    # Exibe os percentuais de representação de forma formatada.

    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")


def main():
    # Função principal para calcular e exibir os percentuais de representação.

    # Dicionário com o valor de faturamento por estado
    faturamentos = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    try:
        percentuais = calcular_percentuais(faturamentos)
        exibir_percentuais(percentuais)
    except ValueError as e:
        print(f"Erro: {e}")


# Executa a função principal
if __name__ == "__main__":
    main()
