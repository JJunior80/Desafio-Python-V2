from datetime import datetime

def exibir_menu():
    """Exibe o menu de opções do sistema."""
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

def depositar(saldo, extrato, transacoes):
    """Realiza um depósito na conta."""
    if len(transacoes) >= 10:
        print("Você atingiu o limite de 10 transações diárias.")
        return saldo, extrato, transacoes
    
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"{horario} - Depósito: R$ {valor:.2f}")
            transacoes.append("deposito")
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Operação falhou! Valor inválido.")
    
    return saldo, extrato, transacoes

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES, transacoes):
    """Realiza um saque da conta respeitando regras de saldo e limite."""
    if len(transacoes) >= 10:
        print("Você atingiu o limite de 10 transações diárias.")
        return saldo, extrato, numero_saques, transacoes
    
    try:
        valor = float(input("Informe o valor do saque: "))
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
        elif valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite diário.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            saldo -= valor
            horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato.append(f"{horario} - Saque: R$ {valor:.2f}")
            transacoes.append("saque")
            numero_saques += 1
            print("Saque realizado com sucesso!")
    except ValueError:
        print("Operação falhou! Valor inválido.")
    
    return saldo, extrato, numero_saques, transacoes

def exibir_extrato(saldo, extrato):
    """Exibe o extrato das movimentações da conta."""
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    transacoes = []  # Para contar o número de transações diárias
    
    while True:
        opcao = input(exibir_menu()).strip().lower()
        
        if opcao == "d":
            saldo, extrato, transacoes = depositar(saldo, extrato, transacoes)
        elif opcao == "s":
            saldo, extrato, numero_saques, transacoes = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES, transacoes)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            print("Obrigado por utilizar nosso sistema bancário. Até logo!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
