N = int(input("Quantos números quer digitar?"))
contador = 1
#o contador deve ser ser 0 pois nao houve nenhuma tentativa
impares = 0

while contador <= N:
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1

print(f"Quantidade de ímpares entre 1 e {N}: {impares}")
