

if __name__ == "__main__":
    n1 = input("Digite o primeiro valor: ")
    n2 = input("Digite o segundo valor: ")
    n3 = input("Digite o terceiro valor: ")7

    if (n1 < n2 and n1 < n3):
        print(f"Menor = {n1}")
    if (n2 < n1 and n2 < n3):
        print(f"Menor = {n2}")
    if (n3 < n1 and n3 < n2):
        print(f"Menor = {n3}")