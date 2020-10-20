from __future__ import annotations
from abc import ABC, abstractmethod
from app.db.models import movies
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
        return self.switch()

    def switch(self):
        switcher = {
            'movies':getMovies
        }
        classObj=switcher.get(self.className, "Invalid month");
        return classObj().getQuery()


class getMovies(AbstractFactory):
    model=movies

    def getQuery(self) -> AbstractFactory:
        return self.returnAll()