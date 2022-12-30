import os
import time
from colorama import Fore, Style


class Banco:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.operaçoes = ""
        self.quantidade_saques = 0
        self.limite_saques = 3
        self.hud = "[d] Depositar [s] Sacar [e] Extrato [x] Sair\n"
    def menu(self):
        os.system('cls')
        operacao = input(self.hud)
        if operacao == "d":
            self.depositar()
        elif operacao == "s":
            self.sacar()
        elif operacao == "e":
            self.extrato()
        elif operacao == "x":
            exit()
        os.system('cls')
        print("operação não reconhecida!")
        time.sleep(1)
        self.menu()
    def depositar(self):
        try:
            valor = float(input("Valor do depósito: "))
        except:
            print("Valor inválido!")
            time.sleep(1)
            self.menu()

        if valor > 0:
                self.saldo += valor
                self.operaçoes += f"{Fore.GREEN}Sucesso, valor depositado: R$ {valor:.2f}\n{Style.RESET_ALL}"
                print(f"Novo saldo: R$ {self.saldo}")
        else:
            os.system('cls')
            print("Deposito inválido!")

        time.sleep(1)
        self.menu()
    def sacar(self):
        try:
            valor = float(input("Valor do saque: "))
        except:
            print("Valor inválido!")
            time.sleep(1)
            self.menu()

        saldo_excedido = valor > self.saldo
        limite_execedido = valor > self.limite
        saques_execedidos = self.quantidade_saques > self.limite_saques

        if saldo_excedido:
            print("Falha! Não possui saldo suficiente")
        elif limite_execedido:
            print("Falha! Limite excedido")
        elif saques_execedidos:
            print("Você não possui mais saques a disponibilidade.")
        elif valor > 0:
            self.saldo -= valor 
            self.quantidade_saques += 1
            self.operaçoes += f"{Fore.RED}Sucesso, valor sacado: R$ {valor:.2f}\n{Style.RESET_ALL}"
            print(f"Novo saldo: R$ {self.saldo}")
            
        else:
            print("Saque inválido!")

        time.sleep(1)
        self.menu()
    def extrato(self):
        print("\n==========EXTRATO==========")
        print("Nenhuma movimentação registrada." if not self.operaçoes else self.operaçoes)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("\n===========================")
        pause = input()
        self.menu()

banco = Banco()
banco.menu()
