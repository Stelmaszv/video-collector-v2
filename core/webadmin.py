import os
import json
from abc import ABC, abstractmethod
from pathlib import Path
from app.db.models import Producent, session, Series

class AbstractWebAdmin(ABC):

    Model=None
    file_name=''
    objects = []

    def generate_file(self):
        if Path(self.file_name).is_file() is True:
            os.remove(self.file_name)
        f = open(self.file_name, "x")
        f.write(json.dumps(self.objects))
        f.close()

    @abstractmethod
    def generate(self):
        pass

class WebAdminProducents(AbstractWebAdmin):

    Model=Producent
    file_name='Producent.json'

    def generate(self):
        query=session.query(self.Model).all()
        self.objects = []
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
        self.generate_file()

class WebAdminSeries(AbstractWebAdmin):

    Model=Series
    file_name='Series.json'

    def generate(self):
        query=session.query(self.Model).all()
        self.objects=[]
        for item in query:
            jason_row = {
                "name":item.name,
                "banner":item.baner,
                "show_name":item.show_name,
                "avatar":item.avatar,
                "dir"   :item.dir,
                "country":item.country,
                "number_of_sezons":item.number_of_sezons,
                "years":item.years,
                "description": item.description,
                "producent":   item.producent[0].name
            }
            self.objects.append(jason_row)
        self.generate_file()