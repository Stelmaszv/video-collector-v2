from core.db.config import Base,engine
from sqlalchemy import Column,Integer, String,Table,ForeignKey,DateTime,Boolean
from sqlalchemy.orm import sessionmaker,relationship

association_table = Table('association', Base.metadata,
    Column('stars_id', Integer, ForeignKey('stars.id')),
    Column('movies_id', Integer, ForeignKey('movies.id'))
)

photos_star = Table('photos_star', Base.metadata,
    Column('stars_id', Integer, ForeignKey('stars.id')),
    Column('photos_id', Integer, ForeignKey('photos.id'))
)

photos_series = Table('photos_series', Base.metadata,
    Column('series_id', Integer, ForeignKey('series.id')),
    Column('photos_id', Integer, ForeignKey('photos.id'))
)

stars_series = Table('stars_series', Base.metadata,
    Column('stars_id', Integer, ForeignKey('stars.id')),
    Column('series_id', Integer, ForeignKey('series.id'))
)

movies_Series = Table('movies_Series', Base.metadata,
    Column('movies_id', Integer, ForeignKey('movies.id')),
    Column('series_id', Integer, ForeignKey('series.id'))
)

class Series(Base):
    __tablename__ ='series'
    id= Column('id',Integer,primary_key=True)
    name = Column('name',String)
    avatar = Column('avatar', String)
    sezons= Column('sezons',Integer)

    stars = relationship(
        "Stars",
        secondary=stars_series,
        back_populates="series"
    )

    movies = relationship(
        "Movies",
        secondary=movies_Series,
        back_populates="series"
    )

    photos = relationship(
        "Photos",
        secondary=photos_series,
        back_populates="series"
    )

    def returmNmae(self):
        return type(self).__name__


    def __str__(self):
        return  self.name

class Photos(Base):
    __tablename__ ='photos'
    id= Column('id',Integer,primary_key=True)
    src = Column('src',String)
    stars = relationship(
        "Stars",
        secondary=photos_star,
        back_populates="photos"
    )

    series = relationship(
        "Series",
        secondary=photos_series,
        back_populates="photos"
    )

    def __str__(self):
        return  self.src

class Stars(Base):
    __tablename__ ='stars'
    id= Column('id',Integer,primary_key=True)
    name = Column('name',String)
    avatar = Column('avatar',String)
    description = Column('description', String,default="")
    views =      Column('views', Integer,default=0)
    likes = Column('likes', Integer,default=0)
    favourite = Column('favourite', Boolean,default=False)
    weight   = Column('weight ', Integer,default=0)
    height = Column('height', Integer, default=0)
    ethnicity = Column('ethnicity', String, default='')
    hair_color =  Column('hair_color', String, default='')
    date_of_birth = Column(DateTime)
    series = relationship(
        "Series",
        secondary=stars_series,
        back_populates="stars"
    )

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
    id=    Column('id',Integer,primary_key=True)
    name = Column('name',String)
    src=   Column('src',String)
    sezon = Column('sezon',Integer)
    stars = relationship(
        "Stars",
        secondary=association_table,
        back_populates="movies"
    )

    series = relationship(
        "Series",
        secondary=movies_Series,
        back_populates="movies"
    )

    def __str__(self):
        return  self.name

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

