cont = 5

while cont > 0: 
    num = int(input("Digite um número inteiro: "))
    cont -= 1

    # Se o número for par, o continue faz o loop ir
    # direto para a próxima repetição, sem executar o print.
    if num % 2 == 0: 
        continue

    # Se o número for ímpar, o continue não acontece
    # e a mensagem abaixo é exibida.
    print(f'{num} é um número ímpar')
 