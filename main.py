print('Bem vindo ao sistema Bancário')
saldo = 0
historico = []
saque_restantes = 3
opcao = 0

while True :
    print ('[1]para depositar [2]para sacar [3] extrato [4] sair')
    opcao = int(input('digite um comando : '))

    if opcao == 1 :  # depositar = 1
        deposito = int(input('quanto você deseja depositar: '))
        if deposito > 0 :
            saldo = saldo + deposito
            historico.append(f'Deposito: R${deposito},00')
        else:
            print('valor invalido')



    elif opcao == 2:  # sacar
        sacar = int(input('Quanto você deseja sacar? : '))
        if sacar <= 0:
            print('Valor inválido.')

        elif saque_restantes <= 0:
            print('Você estourou seu limite de saques diários.')

        elif saldo < sacar:
            print(f'Saldo insuficiente. Saldo atual: R${saldo},00')

        else:
            saque_restantes -= 1
            saldo -= sacar
            historico.append(f'Saque: R${sacar},00')
            print(f'Você sacou R${sacar},00')


    elif opcao == 3: # extrato = 3
        print('======== EXTRATO ========')
        for i in historico :
            print (i)
        print(f'limite de saques diários: {saque_restantes}')
        print(f'Você tem R${saldo},00')



    elif opcao == 4 : # sair = 4
        print ('voce esta saindo')
        break



    else:
        print('comando invalido')
