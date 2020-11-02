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

    def getItem(self,id):
        self.item=session.query(self.model).get(id)

    def addRelations(self,object,related,ids):
        for item in session.query(related).all():
            if item.id in ids:
                object.append(item)


