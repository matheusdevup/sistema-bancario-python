print('Bem vindo ao sistema Bancário')
saldo = 0
historico = []
saque_restantes = 3
opcao = 0

def depositar(saldo, historico):
    deposito = int(input('quanto você deseja depositar: '))
    if deposito > 0:
        saldo = saldo + deposito
        historico.append(f'Deposito: R${deposito},00')
        return saldo
    else:
        print('valor invalido')
        return saldo

def saque(saldo , historico ,saque_restantes) :
    sacar = int(input('Quanto você deseja sacar? : '))
    if sacar <= 0:
        print('Valor inválido.')
        return saldo , saque_restantes
    elif saque_restantes <= 0:
        print('Você estourou seu limite de saques diários.')
        return saldo , saque_restantes
    elif saldo < sacar:
        print(f'Saldo insuficiente. Saldo atual: R${saldo},00')
        return saldo, saque_restantes
    else:
        saque_restantes -= 1
        saldo -= sacar
        historico.append(f'Saque: R${sacar},00')
        print(f'Você sacou R${sacar},00')
        return (saldo, saque_restantes)

def extrato(saldo , saque_restantes , historico):
    print('======== EXTRATO ========')
    for i in historico:
        print(i)
    print(f'limite de saques diários: {saque_restantes}')
    print(f'Você tem R${saldo},00')

while True :
    print ('[1]para depositar [2]para sacar [3] extrato [4] sair')
    opcao = int(input('digite um comando : '))

    if opcao == 1 :  # depositar = 1
        saldo = depositar(saldo, historico)

    elif opcao == 2:  # sacar
        saldo , saque_restantes = saque(saldo , historico ,saque_restantes,)

    elif opcao == 3: # extrato = 3
        extrato(saldo , saque_restantes , historico)



    elif opcao == 4 : # sair = 4
        print ('voce esta saindo')
        break



    else:
        print('comando invalido')
