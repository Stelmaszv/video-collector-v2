from __future__ import annotations
from abc import ABC, abstractmethod
from app.db.models import movies,series,stars
from app.db.models import session

class AbstractFactory(ABC):

    def __init__(self,obj):
        self.obj=obj

    @abstractmethod
    def getQuery(self) -> session:
        pass

    @abstractmethod
    def deepSearch(self) -> session:
        pass


    def returnAll(self) -> session:
        return self.ifIssearchFaze()

    def ifIssearchFaze(self) -> session:
        if self.obj.deepSearch:
            return self.deepSearch()
        if self.obj.searchFaze is None:
            return session.query(self.model).all()
        else:
            return self.searchFazeNormal()

    def searchFazeNormal(self):
        return session.query(self.model).filter(self.model.name.like(str(self.obj.searchFaze)+'%'))

class setFactory:

    def __init__(self,className,obj):
        self.className=className
        self.obj=obj

    def getFactory(self):
        switcher = {
            'movies' : getMovies,
            'series' : getSeries,
            'stars'  : getStar
        }

        classObj = switcher.get(self.className, "Invalid data");
        return classObj(self.obj).getQuery()

class getMovies(AbstractFactory):
    model=movies

    def getQuery(self) ->  session:
        return self.returnAll()

    def deepSearch(self) -> session:
        return session.query(self.model).all()


class getSeries(AbstractFactory):
    model=series

    def getQuery(self) -> session:
        return self.returnAll()

    def deepSearch(self) -> session:
        pass

class getStar(AbstractFactory):
    model=stars

    def getQuery(self) -> session:
        return self.returnAll()

    def deepSearch(self) -> session:
        pass


