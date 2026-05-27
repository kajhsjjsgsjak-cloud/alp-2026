total = 0

while True:  # laço infinito

    print("\n===== CARDÁPIO =====")
    print("1. Açaí 300ml - R$ 12.00")
    print("2. Mousse - R$ 6.50")
    print("3. Salada de frutas - R$ 10.00")
    print("4. Fechar a conta")

    opcao = int(input("Escolha uma opção: "))

    # Verifica opções inválidas
    if opcao < 1 or opcao > 4:
        print("Opção inválida! Tente novamente.")
        continue

    # Fecha a conta
    if opcao == 4:
        print(f"\nTotal da conta: R$ {total:.2f}")
        break

    # Soma os preços dos itens
    if opcao == 1:
        total += 12
        print("Açaí 300ml adicionado!")

    elif opcao == 2:
        total += 6.50
        print("Mousse adicionado!")

    elif opcao == 3:
        total += 10
        print("Salada de frutas adicionada!")

print("Obrigado pela preferência!")