from core.db.config import Base,engine
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker,relationship

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
session = sessionmaker(bind=engine)