from core.db.config import Base,engine
from sqlalchemy import Column,Integer, String
from sqlalchemy.orm import sessionmaker

class movies(Base):
    __tablename__ ='movies'
    id= Column('id',Integer,primary_key=True)
    name = Column('name',String)

class series(Base):
    __tablename__ ='series'
    id= Column('id',Integer,primary_key=True)
    name = Column('name',String)

class stars(Base):
    __tablename__ ='stars'
    id= Column('id',Integer,primary_key=True)
    name = Column('name',String)



Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
objects = [movies(name="u1"), movies(name="u2"), movies(name="u3")]
session.add_all(objects)
session.commit()
print(session.query(movies).all())
