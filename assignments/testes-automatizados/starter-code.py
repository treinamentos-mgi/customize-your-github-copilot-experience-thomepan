# Código Inicial para a Atividade de Testes Automatizados
# Execute os testes com: python starter-code.py

import unittest


# Código a ser testado (não altere)
def calcular_media(notas):
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia")
    return sum(notas) / len(notas)


def classificar_nota(media):
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperação"
    return "Reprovado"


class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo")
        self.saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor


# Tarefa 1: Testar uma Função Simples
# Crie a classe de teste e os métodos de teste de calcular_media


# Tarefa 2: Testar Casos de Erro
# Teste ValueError em calcular_media e os limites de classificar_nota


# Tarefa 3: Testar uma Classe com setUp
# Teste depositar e sacar em ContaBancaria


if __name__ == "__main__":
    unittest.main()
