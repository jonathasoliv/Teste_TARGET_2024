def inverter_string(palavra):
    # Inverte os caracteres de uma string sem usar funções prontas.

    if not isinstance(palavra, str):
        raise ValueError("A entrada deve ser uma string.")

    # Inicializa uma lista para armazenar a string invertida

    string_invertida = []

    # Adiciona os caracteres da string original na ordem inversa

    for caractere in palavra:
        string_invertida.insert(0, caractere)

    # Converte a lista de volta para uma string

    return ''.join(string_invertida)


def main():
    # Função principal para inverter uma string e exibir o resultado.

    while True:
        try:
            # Solicita ao usuário que informe uma string

            entrada_usuario = input(
                "Digite a string que deseja inverter: ").strip()

            # Verifica se a entrada não está vazia

            if not entrada_usuario:
                raise ValueError("A entrada não pode estar vazia.")

            # Inverte a string e exibe o resultado

            resultado = inverter_string(entrada_usuario)
            print(f"String invertida: {resultado}")
            break  # Sai do loop se a entrada for válida
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")


# Executa a função principal
if __name__ == "__main__":
    main()
