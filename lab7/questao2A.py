N = int(input("Quantos números quer digitar?"))
contador = 0
#o contador deve ser ser 0 pois nao houve nenhuma tentativa
impares = 0

while contador <= N:
    # nao e <= e sim < pois se for <= iria ter um numero a mais para ser digitado
    num = int(input("Digite um número: "))
    #o while nunca vai ser true pois falta a variavel contador += 1
    contador += 6
    if num % 2 != 0:
        impares += 1
print(f"Quantidade de ímpares entre 1 e {N}: {impares}")
#erro de logica pois a variavel N e quantos numeros a pessoa ira digitar