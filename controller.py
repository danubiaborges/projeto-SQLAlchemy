from view import View
from DAO import DAOCrud

class Controle:
    def __init__(self):
        self.view = View()
        self.dao = DAOCrud("postgresql+psycopg2://postgres:root@localhost:5432/dvdrental", echo=False)

    def main(self):

        while True:
            opcao = self.view.inicio()

            if opcao == 1:
                city_name = input("Nome da cidade: ")
                country_id = int(input("ID do país: "))
                self.dao.adicionaCidade(city_name, country_id)

            elif opcao == 2:
                city_id = int(input("ID da cidade: "))
                atributo = input("Atributo a ser alterado: ")
                novo_valor = input("Novo valor: ")
                self.dao.alteraCidade(city_id, atributo, novo_valor)

            elif opcao == 3:
                city_name = input("Nome da cidade a ser apagada: ")
                self.dao.deletaCidade(city_name)

            elif opcao == 4:
                city_name = input("Nome da cidade: ")
                self.dao.atributosCidade(city_name)

            elif opcao == 5:
                country_name = input("Nome do país: ")
                self.dao.cidadePorPais(country_name)

            elif opcao == 6:
                break

            else:
                print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    controle = Controle()
    controle.main()
