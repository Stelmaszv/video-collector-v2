from __future__ import annotations
from abc import ABC, abstractmethod
from app.db.models import Movies,Series,Stars
from app.db.models import session

class AbstractFactory(ABC):
    model=None

    def __init__(self,obj):
        self.obj=obj

    def get_query(self) -> session:
        return self.return_all()

    def return_all(self) -> session:
        return self.if_isset_search_faze()

    def if_isset_search_faze(self) -> session:
        if self.obj.search_faze is None:
            return session.query(self.model).all()
        else:
            return self.search_faze_normal()

    def search_faze_normal(self):
        return session.query(self.model).filter(self.model.name.like(str(self.obj.search_faze)+'%'))

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



