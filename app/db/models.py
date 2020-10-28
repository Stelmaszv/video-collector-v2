from core.db.config import Base,engine
from sqlalchemy import Column,Integer, String,Table,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

association_table = Table('association', Base.metadata,
    Column('stars_id', Integer, ForeignKey('stars.id')),
    Column('movies_id', Integer, ForeignKey('movies.id'))
)

class Series(Base):
    __tablename__ ='series'
    id= Column('id',Integer,primary_key=True)
    name = Column('name',String)

class Stars(Base):
    __tablename__ ='stars'
    id= Column('id',Integer,primary_key=True)
    name = Column('name',String)
    avatar = Column('avatar',String)
    movies = relationship(
        "Movies",
        secondary=association_table,
        back_populates="stars"
    )

class Movies(Base):
    __tablename__ ='movies'
    id= Column('id',Integer,primary_key=True)
    name = Column('name',String)
    stars = relationship(
        "Stars",
        secondary=association_table,
        back_populates="movies"
    )






Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

