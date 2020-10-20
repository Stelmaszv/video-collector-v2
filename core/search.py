from __future__ import annotations
from abc import ABC, abstractmethod
from app.db.models import movies
from app.db.models import session

class AbstractFactory(ABC):
    @abstractmethod
    def getQuery(self) -> AbstractFactory:
        pass

    def returnAll(self) -> session.query(movies).all():
        session.query(self.model).all()
