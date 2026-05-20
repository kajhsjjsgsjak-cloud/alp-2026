soma = 0
#adicionamos um contador
contador = 0
while soma <= 10: 
    #nao e <= e sim < pois se  for <= ira ter um numero a mais para ser digitado
    #o while vai ser true quando a soma for 10 e nao quando voce digitar 10 numeros 
    num = int(input("Digite um número para somar: "))
    soma += num
    contador += 10
    #falta um print para imprimir a soma dos 10 numeros
    print("a soma dos numeros e", soma)