from abc import ABC,abstractmethod
from core.dir import set_name,if_star_exist,AddStarViaDir,set_dir_for_star
from app.db.models import session
from app.db.models import Tags,Series,Stars,Movies
from datetime import datetime
import os
import json

class AbstractConfigItem(ABC):

    Model= None

    def __init__(self,dir):
        self.dir=dir
        self.name = set_name(dir)
        self.data = session.query(self.Model).filter(self.Model.name == self.name).first()
        self.config = self.dir+'/config.JSON'
        self.name=set_name(dir)

    def add_stars(self,stars,Obj):
        for star in stars:
            StarObj = if_star_exist(AddStarViaDir(set_dir_for_star(star)), star)
            Obj.stars.append(StarObj)

    def add_tags(self,tags,Obj=None):
        if Obj is not None:
            self.data=Obj
        for tag in tags:
            query = session.query(Tags).filter(Tags.name == tag).first()
            if query is None:
                TagObj=Tags(name=tag)
                session.add_all([TagObj])
                session.commit()
                query=TagObj
            self.data.tags.append(query)
            session.commit()

    def set_data_form_json(self,el,Obj):
        def add_item(item):
            if 'data' in item:
                item['value']= datetime(
                    item['value'][0],
                    item['value'][1],
                    item['value'][2]
                )
            setattr(Obj, item['db'], item['value'])
            session.commit()

        for item in el:
            if 'db' in item and 'value' in item:
                if hasattr(Obj,item['db']):
                    if 'available' in item:
                        if item['value'] in item['available']:
                            add_item(item)
                    else:
                        add_item(item)

    @abstractmethod
    def load(self):
        pass

class SeriesConfigData(AbstractConfigItem):

    Model = Series

    def add_star_to_seazon(self,item):
        def add_star_to_movie(Star,name):
            for movie in self.data.movies:
                if movie.sezon == int(name):
                    movie.stars.append(Star)

        def add_star_to_series(Star,Series):
            Series.stars.append(Star)
            session.commit()

        sezon_name=item['name']
        for star in item['stars']:
            StarObj=if_star_exist(AddStarViaDir(set_dir_for_star(star)),star)
            add_star_to_movie(StarObj,sezon_name)
            add_star_to_series(StarObj,self.data)

    def config_sezons(self,sezons):
        for item in sezons:
            stars = "stars" in item
            if stars:
                self.add_star_to_seazon(item)

    def set_for_sezon(self,data):
        for sezon in self.data.sezons:
            for sezon_item in data:

                if "avatar" in sezon_item:
                    if sezon.name == str(sezon_item['name']):
                        sezon.src=sezon_item['avatar']
                        session.commit()

                if "sezon_name" in sezon_item:
                    if sezon.name == str(sezon_item['name']):
                        sezon.sezon_name=sezon_item['sezon_name']
                        session.commit()

                if "year" in sezon_item:
                    if sezon.name == str(sezon_item['name']):
                        sezon.year=sezon_item['year']
                        session.commit()

    def load(self):
        with open(self.config) as json_file:
            data = json.load(json_file)

            if "year" in data:
                self.data.years=data['year']
                session.commit()

            if "description" in data:
                self.data.description = data['description']
                session.commit()

            if "tags" in data:
                self.add_tags(data['tags'])

            if "country" in data:
                self.data.country=data['country']
                session.commit()

            if "sezons" in data:
                self.config_sezons(data['sezons'])
                self.set_for_sezon(data['sezons'])

class StarConfigData(AbstractConfigItem):

    Model = Stars

    def load(self):
        with open(self.config) as json_file:
            data = json.load(json_file)
            if 'fields' in data:
                self.set_data_form_json(data['fields'], self.data)

            if "date_of_birth" in data:
                self.data.date_of_birth = datetime(
                    data['date_of_birth'][0],
                    data['date_of_birth'][1],
                    data['date_of_birth'][2])
                session.commit()



class ConfigMovies(AbstractConfigItem):

    Movies=Movies
    dir_DB=''

    def __init__(self,json_data):
        self.dir=json_data

    def config(self,Movie):

        with open(self.dir + '/config.JSON') as f:
            data = json.load(f)

            for el in data:
                if 'id' in el:
                    if el['id']==Movie.id:
                        if 'fields' in el:
                            self.set_data_form_json(el['fields'],Movie)
                        if "tags" in el:
                            self.add_tags(el['tags'], Movie)
                        if "stars" in el:
                            self.add_stars(el['stars'],Movie)

    def make_dir(self,Movie):
        dir=self.dir+'/'+str(Movie.id)
        is_dir=os.path.isdir(self.dir+'/'+str(Movie.id))
        if is_dir is False:
            os.mkdir(dir)
        self.config(Movie)
        self.dir_DB=dir

    def add_config_json(self):
        if os.path.isfile(self.dir + '/config.JSON') is False:
            f = open(self.dir + '/config.JSON', "x")
            f.write('[]')
            f.close()

    def load(self):
        self.add_config_json()
        for Movie in session.query(Movies).all():
            self.make_dir(Movie)
            Movie.dir=self.dir_DB
            session.commit()

class AbstractConfig(ABC):

    LoadSetingsClass=None

    def __init__(self,dir):
        self.dir=dir

    def set(self):
        loop_dir = os.listdir(self.dir)
        for item in loop_dir:
            dir = self.dir + '' + str('/' + item)
            OBJ = self.LoadSetingsClass(dir)
            OBJ.load_dir()

class AbstractLoadSetings(ABC):

    ItemClass=None

    def __init__(self,dir):
        self.dir=dir

    def load_dir(self):
        loop_dir = os.listdir(self.dir)
        for item in loop_dir:
            dir = self.dir + '' + str('/' + item)
            self.ItemClass(dir).load()

class LoadSetingsSeries(AbstractLoadSetings):

    ItemClass = SeriesConfigData

class LoadSetingsStars(AbstractLoadSetings):

    ItemClass = StarConfigData

class ConfigStars(AbstractConfig):

    LoadSetingsClass= LoadSetingsStars

class ConfigSeries(AbstractConfig):

    LoadSetingsClass = LoadSetingsSeries

class ConfigLoop:

    def __init__(self, json_data):
        self.json_data = json_data
        self.object = {
            "stars":  ConfigStars,
            "series": ConfigSeries
        }

    def load(self):
        for item in self.json_data:
            if item['type'] != 'photos':
                LD = self.object[item['type']]
                LD = LD(item['dir'])
                LD.set()