from sqlalchemy import create_engine

# Conectar ao SQLite em memória

engine = create_engine('sqlite:///meubanco.db', echo=True)

print('Conexão com SQLite estabelecida.')
#Dialetos
#
# dialect+driver://username:password@host:port/database



from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
# Adicionando usuario

# try:
#     novo_usuario = Usuario(nome="Alirio", idade=26)
#     session.add(novo_usuario)
#     session.commit()
# except:
#     session.rollback()
#     raise
# finally:
#     session.close()

# Quando utilizamos o WITH ele explicitamente ja faz COMMIT, ROLLBACK e CLOSE
# Sempre que for fazer uma trasação em SQL utilizar o WITH
with Session() as session:
    novo_usuario = Usuario(nome='Joana', idade=29)
    session.add(novo_usuario)
# O commit é feito automaticamente aqui, se não houver exceções
# O rollback é automaticamente chamado se uma exceção ocorrer
# A sessão é fechada automaticamente ao sair do bloco with

# usuario = session.query(Usuario).filter_by(nome='João').first()
# print(f'Usuário encontrado: {usuario.nome}, Idade:{usuario.idade}')