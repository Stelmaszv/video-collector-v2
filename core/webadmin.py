import os
import json
from abc import ABC, abstractmethod
from pathlib import Path
from app.db.models import Producent, session, Series,Tags,Stars,Movies
from core.setings import data_JSON

class CleanWebAdmin:
    def clean(self):
        for file in os.listdir(data_JSON['web_admin_url']+'/jsondb'):
            os.remove(data_JSON['web_admin_url']+'/jsondb/'+file)

class AbstractWebAdmin(ABC):

    Model=None
    file_name=''
    no_photo_url=''
    objects = []

    def generate_file(self):
        if Path(data_JSON['web_admin_url']+'/jsondb/'+self.file_name).is_file() is True:
            os.remove(self.file_name)
        f = open(data_JSON['web_admin_url']+'/jsondb/'+self.file_name, "x")
        f.write(json.dumps(self.objects))
        f.close()

    @abstractmethod
    def generate(self):
        pass

    def add_date(self,data):
        if data is not None:
            return str(data.year)+'-'+str(data.month)+'-'+str(data.day)
        return ''

    def add_many_to_many_as_array(self,Item,atter):
        objects=[]
        for Obj in getattr(Item,atter):
            objects.append(Obj.name)
        return objects

    def ger_producent(self,item):
        if len(item.producent)>0:
            return item.producent[0].name
        return []

    def set_assset(self,string):
        count = 0
        for astet in string:
            if astet=='web':
                return count
            count = count + 1
        return 0

    def set_icon(self,string):
        count = 0
        for astet in string:
            if astet=='icon':
                return count
            count = count + 1
        return 0


    def set_dir(self,dir):
        if dir is not None:
            string = dir.split('\\')
            assert_index=self.set_assset(string)
            count=0
            str=''
            for dir_strin in string:
                if count>=assert_index:
                    str=str+string[count]
                    if count!=len(string)-1:
                        str=str+'\\'
                count = count + 1
            return str
        return ''

    def set_img(self,dir):
        if dir is not None:
            string = dir.split('\\')
            icon=self.set_icon(string)
            src=''
            if icon>0:
                src=self.no_photo_url
                src = self.set_dir(src)
            else:
                src=self.set_dir(dir)
            return self.add_server_url(src)
        else:
            return ''

    def add_server_url(self,src):
        return 'http://127.0.0.1:8000/'+src


class WebAdminProducents(AbstractWebAdmin):

    Model=Producent
    file_name='Producent.json'
    no_photo_url = 'web\\no_img\\series.jpg'

    def generate(self):
        query=session.query(self.Model).all()
        self.objects = []
        for item in query:
            jason_row = {
                "name":item.name,
                "banner":self.set_dir(item.baner),
                "year" :item.year,
                "show_name":item.show_name,
                "avatar":self.set_img(item.avatar),
                "dir"   :self.set_dir(item.dir),
                "country":item.country,
                "description": item.description,
                "tags": self.add_many_to_many_as_array(item,'tags')
            }
            self.objects.append(jason_row)
        self.generate_file()

class WebAdminSeries(AbstractWebAdmin):

    Model=Series
    file_name='Series.json'
    no_photo_url = 'web\\no_img\\series.jpg'

    def generate(self):
        query=session.query(self.Model).all()
        self.objects=[]
        for item in query:
            jason_row = {
                "name":item.name,
                "banner":self.set_img(item.baner),
                "show_name":item.show_name,
                "avatar":self.set_img(item.avatar),
                "dir"   :self.set_dir(item.dir),
                "country":item.country,
                "number_of_sezons":item.number_of_sezons,
                "years":item.years,
                "description": item.description,
                "producent":   self.ger_producent(item),
                "movies": self.add_many_to_many_as_array(item, 'movies'),
                "tags": self.add_many_to_many_as_array(item,'tags'),
                "stars": self.add_many_to_many_as_array(item, 'stars')
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

class WebAdminStars(AbstractWebAdmin):

    Model=Stars
    file_name='Stars.json'
    no_photo_url = 'web\\no_img\\star_no_photo.png'

    def generate(self):
        query=session.query(self.Model).all()
        self.objects=[]
        for item in query:
            jason_row = {
                "name":item.name,
                "show_name": item.show_name,
                "description": item.description,
                "weight": item.weight,
                "avatar": self.set_img(item.avatar),
                "height": item.height,
                "ethnicity": item.height,
                "hair_color": item.height,
                "birth_place": item.height,
                "nationality": item.nationality,
                "dir": self.set_dir(item.dir),
                "date_of_birth": self.add_date(item.date_of_birth),
                "movies": self.add_many_to_many_as_array(item, 'movies'),
                "tags": self.add_many_to_many_as_array(item, 'tags'),
                "series": self.add_many_to_many_as_array(item, 'series'),
            }
            self.objects.append(jason_row)
        self.generate_file()

class WebAdminMovies(AbstractWebAdmin):

    Model=Movies
    file_name='Movies.json'
    no_photo_url='web\\no_img\\movie.jpg'

    def generate(self):
        query=session.query(self.Model).all()
        self.objects=[]
        for item in query:
            jason_row = {
                "name": item.name,
                "show_name": item.show_name,
                "description": item.description,
                "src": self.set_img(item.src),
                "avatar": self.set_img(item.avatar),
                "date_relesed": self.add_date(item.date_relesed),
                "dir": self.set_dir(item.dir),
                "country": item.country,
                "poster": self.set_img(item.poster),
                "tags": self.add_many_to_many_as_array(item, 'tags'),
                "series": self.add_many_to_many_as_array(item, 'series'),
                "stars": self.add_many_to_many_as_array(item, 'stars')
            }
            self.objects.append(jason_row)
        self.generate_file()