import math

if __name__ == "__main__":
    #varivaies
    altura: float
    base: float
    area: float
    perimetro: float
    diagonal: float

    #Digite os valores
    altura  = float(input("Altura do retangulo: "))
    base    = float(input("Base do retangulo: "))

    #Calculando
    area        = altura * base
    perimetro   = 2 * (base + altura)
    diagonal    =  math.sqrt(base ** 2 + altura ** 2)

    #Mostrando
    print(f"Area = {area:.2f}\nPerimetro = {perimetro:.2f}\ndiagonal = {diagonal:.2f}")
