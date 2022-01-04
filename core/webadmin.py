import os
import json
from abc import ABC, abstractmethod
from pathlib import Path


from app.db.models import Producent, session

class AbstractWebAdmin(ABC):

    Model=None
    objects = []

    @abstractmethod
    def generate(self):
        pass

class WebAdminProducents(AbstractWebAdmin):

    Model=Producent

    def generate(self):
        query=session.query(self.Model).all()
        for item in query:
            jason_row = {
                "name":item.name,
                "banner":item.baner,
                "year" :item.year,
                "show_name":item.show_name,
                "avatar":item.avatar,
                "dir"   :item.dir,
                "country":item.country,
                "description": item.description
            }
            self.objects.append(jason_row)
            if Path('Producent.json').is_file() is True:
                os.remove('Producent.json')
            f = open('Producent.json', "x")
            f.write(json.dumps(self.objects))
            f.close()