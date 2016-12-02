from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/mydb', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,

                                         autoflush=False,

                                         bind=engine))

base = declarative_base()
base.query = db_session.query_property()



def init_db():
    base.metadata.create_all(bind=engine)