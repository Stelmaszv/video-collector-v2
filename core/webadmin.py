import os
import json
from abc import ABC, abstractmethod
from pathlib import Path
from app.db.models import Producent, session, Series,Tags

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

    def add_tags(self,Item):
        tags=[]
        for Tag in Item.tags:
            tags.append(Tag.name)
        return tags

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
                "description": item.description,
                "tags": self.add_tags(item)
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
                "producent":   item.producent[0].name,
                "tags": self.add_tags(item)
            }
            self.objects.append(jason_row)
        self.generate_file()

class WebAdminTags(AbstractWebAdmin):

    Model=Tags
    file_name='Tags.json'

    def generate(self):
        query=session.query(self.Model).all()
        self.objects=[]
        for item in query:
            jason_row = {
                "name":item.name
            }
            self.objects.append(jason_row)
        self.generate_file()