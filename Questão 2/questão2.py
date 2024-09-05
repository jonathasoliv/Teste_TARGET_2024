def soma_fibonacci(numero_informado):
    """Calcula a soma dos números de Fibonacci até o número informado."""

    a, b = 0, 1
    soma = 0

    # Adiciona os números de Fibonacci à soma até o número informado

    while a <= numero_informado:
        soma += a
        a, b = b, a + b

    return soma


def pertence_fibonacci(numero):
    """Verifica se o número fornecido pertence à sequência de Fibonacci."""

    a, b = 0, 1

    # Gera a sequência de Fibonacci até encontrar o número ou ultrapassá-lo

    while a < numero:
        a, b = b, a + b

    return a == numero


def main():
    """Função principal para interagir com o usuário e exibir os resultados."""

    while True:
        try:
            numero_informado = int(
                input("Digite o valor máximo para calcular a soma dos números de Fibonacci: "))
            if numero_informado < 0:
                print("O Fibonacci aceita apenas numero positivo.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    # Calcula a soma dos números de Fibonacci até o número informado

    resultado = soma_fibonacci(numero_informado)

    # Verifica se o número informado pertence à sequência de Fibonacci

    if pertence_fibonacci(numero_informado):
        print(f"O número {
              numero_informado} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {
              numero_informado} NÃO pertence à sequência de Fibonacci.")

    # Exibe a soma dos números de Fibonacci até o número informado

    print(f"A soma dos números de Fibonacci até {
          numero_informado} é: {resultado}")


# Executa a função principal

if __name__ == "__main__":
    main()
