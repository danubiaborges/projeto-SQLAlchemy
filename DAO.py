from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from mapeamento import Country
from mapeamento import City

class DAOCrud:
    def __init__(self, connection_string, echo=False):
        engine = create_engine(connection_string, echo=echo)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def adicionaCidade(self, city_name, country_id):
        try:
            addCidade = City(city=city_name, country_id=country_id)
            self.session.add(addCidade)
            self.session.commit()
            print("Cidade adicionada com sucesso!")
            self.atributosCidade(city_name)
        except Exception as e:
            print(f"Erro ao adicionar cidade: {str(e)}")


    def alteraCidade(self, city_id, atributo, novo_valor):
        cidade = self.session.query(City).filter_by(city_id=city_id).first()
        if cidade:
            setattr(cidade, atributo, novo_valor)
            self.session.commit()
            print("Cidade alterada com sucesso!")
        else:
            print("Cidade não encontrada!")


    def deletaCidade(self, city_name):
        cidade = self.session.query(City).filter_by(city=city_name).first()
        if cidade:
            self.session.delete(cidade)
            self.session.commit()
            print("Cidade deletada com sucesso!")
        else:
            print("Cidade não encontrada!")


    def atributosCidade(self, city_name):
        cidade = self.session.query(City).filter_by(city=city_name).first()
        if cidade:
            print(f"ID: {cidade.city_id}")
            print(f"Cidade: {cidade.city}")
            print(f"País ID: {cidade.country_id}")
            print(f"Última Atualização: {cidade.last_update}")
        else:
            print("Cidade não encontrada!")


    def cidadePorPais(self, country_name):
        pais = self.session.query(Country).filter_by(country=country_name).first()
        if pais:
            cidades = self.session.query(City).filter_by(country_id=pais.country_id).all()
            if cidades:
                for cidade in cidades:
                    print(cidade.city)
            else:
                print("Nenhuma cidade encontrada para este país.")
        else:
            print("País não encontrado!")

    
    def encerraAplicacao(self):
        self.session.close()
