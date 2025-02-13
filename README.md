# Sistema Bancário em Python

## Descrição
Este projeto consiste em um sistema bancário simples desenvolvido em Python. Ele permite ao usuário realizar operações básicas como depósito, saque e exibição de extrato. O objetivo deste projeto é oferecer uma experiência prática no desenvolvimento de software financeiro, consolidando conceitos fundamentais da linguagem Python.

## Funcionalidades
- **Depósito**: Permite adicionar saldo à conta, registrando a transação no extrato.
- **Saque**: Permite retirar dinheiro da conta, respeitando o saldo disponível, o limite por saque e o número máximo de saques diários.
- **Extrato**: Exibe todas as transações realizadas na conta, bem como o saldo atual.
- **Limite de Transações**: O usuário pode realizar até 10 transações diárias (somando depósitos e saques). Caso atinja esse limite, o sistema impedirá novas transações no dia.

## Como Usar
1. Execute o programa no terminal.
2. Escolha uma opção do menu exibido:
   - `[d]` para Depositar
   - `[s]` para Sacar
   - `[e]` para visualizar o Extrato
   - `[q]` para Sair
3. Siga as instruções para cada operação.

## Código-Fonte
```python
from datetime import datetime

def exibir_menu():
    return """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

def depositar(saldo, extrato, transacoes):
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

# As funções sacar() e exibir_extrato() seguem o mesmo formato atualizado.

def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES = 3
    transacoes = []
    
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
```

## Requisitos
- Python 3.x instalado
- Terminal para executar o programa

## Autor
Este projeto foi desenvolvido para fins educacionais e pode ser aprimorado com novas funcionalidades no futuro.



