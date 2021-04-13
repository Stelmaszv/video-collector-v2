from __future__ import annotations
from abc import ABC, abstractmethod
from app.db.models import Movies,Series,Stars,Movies_Tags,Tags
from app.db.models import session
from sqlalchemy import desc
from sqlalchemy import or_
class AbstractFactory(ABC):
    model=None

    def __init__(self,Menu):
        self.Menu=Menu

    def get_query(self) -> session:
        return self.return_all()

    def add_tags(self,query):
        if len(self.Menu.tags):
            query = query.filter(self.model.tags.any(Tags.name.in_(self.Menu.tags)))
        return query

    def add_stars(self,query):
        if len(self.Menu.stars):
            query = query.filter(self.model.stars.any(Stars.name.in_(self.Menu.stars)))
        return query

    def add_favourite(self,query):
        if self.Menu.favourite is not None:
            query=query.filter(self.model.favourite == self.Menu.favourite)
        return query

    def set_query(self):
        if self.Menu.search_faze:
            return session.query(self.model).filter(self.model.name.like(str(self.Menu.search_faze) + '%'))
        return session.query(self.model)

    def add_year(self,query):
        if self.Menu.year:
            query=query.filter(self.model.year == self.Menu.year)
        return query

    def return_all(self) -> session:
        query=self.set_query()
        query=self.add_tags(query)
        query=self.add_stars(query)
        query=self.add_favourite(query)
        query=self.add_year(query)
        return query.order_by(desc(self.Menu.order_by)).all()


    def if_isset_search_faze(self) -> session:
        if self.Menu.search_faze is None:
            return session.query(self.model).all()
        else:
            return self.search_faze_normal()

    def search_faze_normal(self):
        return session.query(self.model).filter(self.model.name.like(str(self.Menu.search_faze) + '%'))

class SetFactory:

    def __init__(self,obj):
        self.obj=obj

    def get_factory(self,name):
        switcher = {
            'movies' : GetMovies,
            'series' : GetSeries,
            'stars'  : GetStar
        }
        classObj = switcher.get(name, "Invalid data");
        return classObj(self.obj).get_query()

class GetMovies(AbstractFactory):
    model=Movies

class GetSeries(AbstractFactory):
    model=Series

class GetStar(AbstractFactory):
    model=Stars



