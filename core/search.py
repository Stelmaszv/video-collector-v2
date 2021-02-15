from __future__ import annotations
from abc import ABC, abstractmethod
from app.db.models import Movies,Series,Stars
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
        if self.obj.deepSearch and \
                self.obj.searchFaze is not None \
                and self.deepSearchMode is True :
            return self.deepSearch()
        if self.obj.searchFaze is None:
            return session.query(self.model).all()
        else:
            return self.searchFazeNormal()

    def searchFazeNormal(self):
        return session.query(self.model).filter(self.model.name.like(str(self.obj.searchFaze)+'%'))

class setFactory:

    def __init__(self,obj):
        self.obj=obj

    def getFactory(self,name):
        switcher = {
            'movies' : getMovies,
            'series' : getSeries,
            'stars'  : getStar
        }
        print(name)
        classObj = switcher.get(name, "Invalid data");
        return classObj(self.obj).getQuery()

class getMovies(AbstractFactory):
    model=Movies
    deepSearchMode = True

    def getQuery(self) ->  session:
        return self.returnAll()

    def deepSearch(self) -> session:
        starAr=[]
        for item in session.query(self.model).all():
            if len(session.query(self.model).get(item.id).stars) > 0:
                for star in session.query(self.model).get(item.id).stars:
                    if self.obj.searchFaze == star.name:
                        starAr.append(item)
        return starAr

class getSeries(AbstractFactory):
    model=Series
    deepSearchMode=False

    def getQuery(self) -> session:
        print('dqwd')
        return self.returnAll()

    def deepSearch(self) -> session:
        pass

class getStar(AbstractFactory):
    model=Stars
    deepSearchMode=False

    def getQuery(self) -> session:
        return self.returnAll()

    def deepSearch(self):
        pass



