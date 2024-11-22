
if __name__ == "__main__":
    #Digite o valor
    n = int(input("Quantos numeros: "))

    vetor: float = [0 for x in range(n)]
    soma = 0

    for i in range(0, n):
        vetor[i] = float(input("Digite o valor: "))
        soma += vetor[i]

    #Resultado
    print("Valores = ", end="")
    for i in range(0, n):
        print(vetor[i], end=" ")

    media = soma / n

    print(f"\nSoma = {soma}\nMedia = {media}")