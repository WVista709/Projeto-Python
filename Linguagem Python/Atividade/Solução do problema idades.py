import math

if __name__ == "__main__":
    #Digitando os dados
    nome1   = input("Digite o primeiro nome: ")
    idade1  = int(input("Digite a idade: "))

    nome2   = input("Digite o segundo nome: ")
    idade2  = int(input("Digite a idade: "))

    media = (idade1 + idade2)/2

    #Mostrando
    print(f"A idade media de {nome1} e {nome2} é de {media} anos")
