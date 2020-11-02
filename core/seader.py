from abc import ABC,abstractmethod
from app.db.models import session
class abstractSeader(ABC):
    objects=[]

    @abstractmethod
    def run(self):
        pass

    def addItems(self):
        session.add_all(self.objects)
        session.commit()

    def generateObjects(self,model,items):
        for x in range(items):
            self.objects.append(model(name=x))


class initSeader:

    def __init__(self,seaders):
        self.seaders=seaders

    def initNow(self):
        for item in self.seaders:
            item.run()
