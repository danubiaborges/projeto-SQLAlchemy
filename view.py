from decimal import *
from mapeamento import City
from mapeamento import Country

class View():

    def inicio(self):
        return self.menu()
    
    def menu(self):
        print()
        print('M E N U')
        print('1. Cadastrar Cidade')
        print('2. Alterar Dados da Cidade')
        print('3. Deletar Cidade')
        print('4. Consultar Dados da Cidade')
        print('5. Consultar Cidades de um País')
        print('6. Sair')
        print()
        opcao = int(input('Digite a opção desejada: '))
        return opcao