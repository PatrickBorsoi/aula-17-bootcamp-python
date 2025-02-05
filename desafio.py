from sqlalchemy import create_engine, Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    # Estabelece a relação entre Produto e Fornecedor
    fornecedor = relationship('Fornecedor')


engine = create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Inserindo fornecedores
try:
    with Session() as session:
        fornecedores = [
            Fornecedor(nome='Fornecedor A', telefone='12345678', email='contato@a.com', endereco='endereço 1'),
            Fornecedor(nome='Fornecedor B', telefone='12345378', email='contato@b.com', endereco='endereço 2'),
            Fornecedor(nome='Fornecedor C', telefone='12345178', email='contato@c.com', endereco='endereço 3'),
            Fornecedor(nome='Fornecedor D', telefone='12335678', email='contato@d.com', endereco='endereço 4'),
            Fornecedor(nome='Fornecedor E', telefone='12375678', email='contato@e.com', endereco='endereço 5'),
        ]
    session.add_all(fornecedores)
    session.commit()
except SQLAlchemyError as e:
    print(f'Erro ao inserir fornecedores: {e}')
try:
    with Session() as session:
        produtos = [
            Produto(nome='Produto 1', descricao='Descrição do produto 1', preco=100, fornecedor_id=1),
            Produto(nome='Produto 2', descricao='Descrição do produto 2', preco=200, fornecedor_id=2),
            Produto(nome='Produto 3', descricao='Descrição do produto 3', preco=300, fornecedor_id=3),
            Produto(nome='Produto 4', descricao='Descrição do produto 4', preco=400, fornecedor_id=4),
            Produto(nome='Produto 5', descricao='Descrição do produto 5', preco=500, fornecedor_id=5),
        ]
    session.add_all(produtos)
    session.commit()
except SQLAlchemyError as e:
    print(f'Erro ao inserir fornecedores: {e}')