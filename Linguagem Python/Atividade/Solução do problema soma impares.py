
if __name__ == "__main__":
    #Digite o valor de X
    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))
    soma: int

    soma = 0
    if (x > y):
        troca   = x
        x       = y
        y       = troca

soma = 0

for i in range(x+1, y):
    if (i % 2 != 0):
        soma += i


print(f"Soam dos impares = {soma}")

            