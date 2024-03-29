from sqlalchemy import (Boolean, Column, Date, DateTime, ForeignKey, Integer,
                        String, Table, Text)
from sqlalchemy.orm import relationship, sessionmaker

from core.db.config import Base, engine
from core.setings import (movie_cover_defulut, none_movies_defult,
                          singles_movies_defult, stars_avatar_defult)

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

Stars_Tags = Table('tags_series', Base.metadata,
    Column('tags_id', Integer, ForeignKey('tags.id')),
    Column('stars_id', Integer, ForeignKey('stars.id'))
)

Series_sezons = Table('series_sezons', Base.metadata,
    Column('sezons_id', Integer, ForeignKey('sezons.id')),
    Column('series_id', Integer, ForeignKey('series.id'))
)

Series_Tags = Table('series_tags', Base.metadata,
    Column('series_id', Integer, ForeignKey('series.id')),
    Column('tags_id', Integer, ForeignKey('tags.id'))
)

Producent_Tags = Table('producent_tags', Base.metadata,
    Column('producent_id', Integer, ForeignKey('producent.id')),
    Column('tags_id', Integer, ForeignKey('tags.id'))
)

Producent_Series = Table('producent_series', Base.metadata,
    Column('producent_id', Integer, ForeignKey('producent.id')),
    Column('series_id', Integer, ForeignKey('series.id'))
)

Movies_Tags = Table('movies_tags', Base.metadata,
    Column('movies_id', Integer, ForeignKey('movies.id')),
    Column('tags_id', Integer, ForeignKey('tags.id'))
)

class Sezons(Base):
    __tablename__ = 'sezons'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    src = Column('src', String)
    sezon_name = Column('sezon_name', String, default='')
    year       = Column('year', String)

    series = relationship(
        "Series",
        secondary=Series_sezons,
        back_populates="sezons"
    )

    def __str__(self):
        return  self.sezon_name

class Producent(Base):
    __tablename__ = 'producent'
    id = Column('id', Integer, primary_key=True)
    views = Column('views', Integer, default=0)
    likes = Column('likes', Integer, default=0)
    favourite = Column('favourite', Boolean, default=False)
    name = Column('name', String)
    baner = Column('baner', String)
    year = Column('year', String)
    show_name = Column('show_name', String, default='')
    avatar = Column('avatar', String)
    dir = Column('dir', String, default='')
    config = Column('config', String, default='')
    country = Column('country', String, default='')
    description = Column('description', String, default='')
    rating = Column('rating', Integer, default=0)

    tags = relationship(
        "Tags",
        secondary=Producent_Tags,
        back_populates="producent"
    )

    series = relationship(
        "Series",
        secondary=Producent_Series,
        back_populates="producent"
    )

    def __str__(self):
        return  self.show_name

class Series(Base):
    __tablename__ ='series'
    id = Column('id', Integer, primary_key=True)
    views = Column('views', Integer, default=0)
    likes = Column('likes', Integer, default=0)
    favourite = Column('favourite', Boolean, default=False)
    name = Column('name', String)
    show_name = Column('show_name', String, default='')
    avatar = Column('avatar', String)
    baner = Column('baner', String)
    dir = Column('dir', String, default='')
    config = Column('config', String, default='')
    number_of_sezons = Column('sezons', Integer,default=1)
    years = Column('year', String, default='')
    country = Column('country', String, default='')
    description = Column('description', String, default='')
    rating = Column('rating', Integer, default=0)

    producent = relationship(
        "Producent",
        secondary=Producent_Series,
        back_populates="series"
    )

    tags = relationship(
        "Tags",
        secondary=Series_Tags,
        back_populates="series"
    )

    sezons = relationship(
        "Sezons",
        secondary=Series_sezons,
        back_populates="series"
    )

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
    id = Column('id', Integer, primary_key=True)
    src = Column('src', String)
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

class Tags(Base):
    __tablename__ = 'tags'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)

    stars = relationship(
        "Stars",
        secondary=Stars_Tags,
        back_populates="tags"
    )

    movies = relationship(
        "Movies",
        secondary=Movies_Tags,
        back_populates="tags"
    )

    series = relationship(
        "Series",
        secondary=Series_Tags,
        back_populates="tags"
    )

    producent = relationship(
        "Producent",
        secondary=Producent_Tags,
        back_populates="tags"
    )

    def __str__(self):
        return self.name

class Stars(Base):
    __tablename__ ='stars'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    show_name = Column('show_name', String, default='')
    avatar = Column('avatar', String, default=stars_avatar_defult)
    description = Column('description', Text, default="")
    views = Column('views', Integer, default=0)
    likes = Column('likes', Integer, default=0)
    favourite = Column('favourite', Boolean, default=False)
    weight = Column('weight ', Integer, default=0)
    height = Column('height', Integer, default=0)
    ethnicity = Column('ethnicity', String, default='')
    hair_color = Column('hair_color', String, default='')
    birth_place = Column('birth_place', String, default='')
    nationality = Column('nationality', String, default='')
    dir = Column('dir', String, default='')
    none = Column('none', String, default=none_movies_defult)
    singles = Column('singles', String, default=singles_movies_defult)
    config = Column('config', String, default='')
    date_of_birth = Column(Date)
    rating = Column('rating', Integer, default=0)

    tags = relationship(
        "Tags",
        secondary=Stars_Tags,
        back_populates="stars"
    )

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
        return self.show_name

class Movies(Base):
    __tablename__ ='movies'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    src = Column('src', String)
    sezon = Column('sezon', Integer)
    search_name = Column('search_name', String)
    avatar = Column('avatar', String, default=movie_cover_defulut)
    date_relesed = Column(Date)
    dir = Column('dir', String, default='')
    likes = Column('likes', Integer, default=0)
    views = Column('views', Integer, default=0)
    favourite = Column('favourite', Boolean, default=False)
    country = Column('country', String, default='')
    show_name = Column('show_name', String, default='')
    description = Column('description', String, default='')
    rating = Column('rating', Integer, default=0)
    poster = Column('poster', String, default='')

    tags = relationship(
        "Tags",
        secondary=Movies_Tags,
        back_populates="movies"
    )

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

    def _get_stars(self):
        if len(self.stars) == 1:
            return self.stars[0].show_name
        return ''

    def return_stars(self):
        stars=self._get_stars()
        if len(stars)>30:
            return '<i>'+self.stars[0].show_name+'</i>'
        return '<li>'+stars+'</i>'

    def return_full_name(self):
        name=self.set_full_name()
        if len(name)>70:
            name='<b>'+self.show_name+'</b>'
        return name

    def set_full_for_xlsx(self):
        def get_series(series):
            if len(series):
                return series[0].name+' '
            return ''
        def get_producent(series):
            if len(series):
                if len(series[0].producent):
                    return series[0].producent[0].name;

        def return_full_name():
            str=''
            series    = get_series(self.series)
            producent = get_producent(self.series)
            if producent:
                str += producent+'-'
                if series:
                    str += series+'-'
            str +=self.show_name

            return str;
        return return_full_name()

    def set_full_name(self):
        def get_year(year):
            if year is None:
                return ''
            return year+' '
        def get_series(series):
            if len(series):
                return series[0].name+' '
            return ''
        return get_series(self.series)+'<b>'+get_year(self.year)+' '+self.show_name+'</b>'

    def __str__(self):
        return  self.show_name

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
