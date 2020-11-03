from abc import ABC,abstractmethod
from app.db.models import session
from core.strings import stringManipupations
class abstractSeader(ABC):
    objects=[]

    def __init__(self):
        self.series=session

    @abstractmethod
    def run(self):
        pass

    def addItems(self):
        self.series.add_all(self.objects)
        self.series.commit()

    def generateObjects(self,model,items):
        for x in range(items):
            self.objects.append(model(name=stringManipupations.random(20)))

    def getItem(self,id):
        self.item=self.series.query(self.model).get(id)

    def addRelations(self,object,related,ids):
        for item in self.series.query(related).all():
            if item.id in ids:
                object.append(item)


