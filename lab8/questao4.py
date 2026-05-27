soma = 0

while True:
    num = int(input("Digite um número inteiro: "))

    # Encerra o programa se digitar 0
    if num == 0:
        break

    # Ignora números negativos
    if num < 0:
        continue

    # Soma apenas números positivos
    soma += num

    # Para o programa se a soma ultrapassar 100
    if soma > 100:
        break

print(f"Soma total: {soma}")
