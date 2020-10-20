from __future__ import annotations
from abc import ABC, abstractmethod
from app.db.models import movies,series,stars
from app.db.models import session

class AbstractFactory(ABC):
    @abstractmethod
    def getQuery(self) -> AbstractFactory:
        pass

    def returnAll(self) -> session.query(movies).all():
        return session.query(self.model).all()

class setFactory:

    def __init__(self,className):
        self.className=className

    def getFactory(self):
        switcher = {
            'movies' : getMovies,
            'series' : getSeries,
            'stars'  : getStar
        }
        classObj = switcher.get(self.className, "Invalid month");
        return classObj().getQuery()

class getMovies(AbstractFactory):
    model=movies

    def getQuery(self) -> AbstractFactory:
        return self.returnAll()

class getSeries(AbstractFactory):
    model=series

    def getQuery(self) -> AbstractFactory:
        return self.returnAll()

class getStar(AbstractFactory):
    model=stars

    def getQuery(self) -> AbstractFactory:
        return self.returnAll()