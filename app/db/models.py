from core.db.config import Base,engine
from sqlalchemy import Column,Integer, String,Table,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

association_table = Table('association', Base.metadata,
    Column('stars_id', Integer, ForeignKey('stars.id')),
    Column('movies_id', Integer, ForeignKey('movies.id'))
)

photos_star = Table('photos_star', Base.metadata,
    Column('stars_id', Integer, ForeignKey('stars.id')),
    Column('photos_id', Integer, ForeignKey('photos.id'))
)

class Series(Base):
    __tablename__ ='series'
    id= Column('id',Integer,primary_key=True)
    name = Column('name',String)

    def __str__(self):
        return  self.name

class Photos(Base):
    __tablename__ ='photos'
    id= Column('id',Integer,primary_key=True)
    src = Column('src',String)
    stars_id = Column(Integer, ForeignKey('stars.id'))
    stars = relationship(
        "Stars",
        secondary=photos_star,
        back_populates="photos"
    )

    def __str__(self):
        return  self.src

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

    photos = relationship(
        "Photos",
        secondary=photos_star,
        back_populates="stars"
    )

    def __str__(self):
        return  self.name

class Movies(Base):
    __tablename__ ='movies'
    id= Column('id',Integer,primary_key=True)
    name = Column('name',String)
    stars = relationship(
        "Stars",
        secondary=association_table,
        back_populates="movies"
    )

    def __str__(self):
        return  self.name

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

