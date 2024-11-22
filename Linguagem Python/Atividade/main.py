idade: int
salario: float
genero: str
nome: str

idade = 20
salario = 5700.5
altura = 1.63
genero = "F"

print(f"Idade = {idade}\nSalario = {salario:.2f}\nAltura = {altura}\nGenero = {genero}")

N = int(input("Quantos numeros? "))
vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Digite o numero: "))

print("Numeros digitados = ")
for i in range(0, N):
    print(f"{vet[i]:.2f}")