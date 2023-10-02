# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()       # objeto que guarda todas as classes da aplicação
metadata = Base.metadata

# declaração das classes:
class Country(Base):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True, server_default=text("nextval('country_country_id_seq'::regclass)"))
    country = Column(String(50), nullable=False)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))


class City(Base):
    __tablename__ = 'city'

    city_id = Column(Integer, primary_key=True, server_default=text("nextval('city_city_id_seq'::regclass)"))
    city = Column(String(50), nullable=False)
    country_id = Column(ForeignKey('country.country_id'), nullable=False, index=True)
    last_update = Column(DateTime, nullable=False, server_default=text("now()"))

    country = relationship('Country')
