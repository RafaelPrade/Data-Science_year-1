print('\n******************* Python Calculator *******************')
while True:
    print('\nSelecione o número da operação desejada:')

    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')

    opcao = input('\nDigite sua opção (1/2/3/4):')
    primnum = input('\nDigite o primeiro número:')
    segnum = input('\nDigite o segundo número:')

    if opcao == '1':
        print('\nResultado:', float(primnum) + float(segnum))
    elif opcao == '2':
        print('\nResultado:', float(primnum) - float(segnum))
    elif opcao == '3':
        print('\nResultado:', float(primnum) * float(segnum))
    else:
        if opcao == '4':
            print('\nResultado:', float(primnum) / float(segnum))