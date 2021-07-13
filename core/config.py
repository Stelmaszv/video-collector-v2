from abc import ABC,abstractmethod
from core.dir import set_name,if_star_exist,AddStarViaDir,set_dir_for_star,AddSeriesViaDir
from app.db.models import session
from app.db.models import Tags,Series,Stars,Movies,Producent
from datetime import datetime
from core.setings import singles_movies_defult,none_movies_defult
from pathlib import Path
import os
import json
import re
import xlsxwriter

class AbstractConfigItem(ABC):

    Model= None

    def __init__(self,dir):
        self.dir=dir
        self.name = set_name(dir)
        self.data = session.query(self.Model).filter(self.Model.name == self.name).first()
        self.config = self.dir+'\\config.JSON'
        self.name=set_name(dir)

    def set_avatar(self,Item):
        for logo in os.listdir(Item.dir+'\photo'):
            dir = Item.dir+"\photo\\"+logo;
            if Path(dir).stem == 'avatar':
                Item.avatar=dir

    def add_stars(self,stars,Obj):
        for star in stars:
            StarObj = if_star_exist(AddStarViaDir(set_dir_for_star(star)), star)
            Obj.stars.append(StarObj)
            StarObj.movies.append(self.data)
            session.commit()


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
                if sezon.name == str(sezon_item['name']):
                    if 'fields' in sezon_item:
                        self.set_data_form_json(sezon_item['fields'], sezon)

    def load(self):
        with open(self.config) as json_file:
            data = json.load(json_file)
            if 'fields' in data:
                self.set_data_form_json(data['fields'], self.data)
            if "tags" in data:
                self.add_tags(data['tags'], self.data)
            if "stars" in data:
                self.add_stars(data['stars'], self.data)

            if "sezons" in data:
                self.config_sezons(data['sezons'])
                self.set_for_sezon(data['sezons'])
            self.set_avatar(self.data)

class CreateXML(AbstractConfigItem):

    def __init__(self,json_data):
        self.dir=json_data
        self.movies = []
        self.workbook = xlsxwriter.Workbook('movies.xlsx')
        self.worksheet = self.workbook.add_worksheet()

    def add_row(self,Movie):
        def set_series(Movie):
            if len(Movie.series):
                return Movie.series[0].name
            return ''

        def set_producent(Movie):
            if len(Movie.series):
                Series=Movie.series[0]
                if len(Series.producent):
                    return Series.producent[0].name
                return ''
            return ''

        def set_stars(Movie):
            stars_str=''
            counter=1
            for star in Movie.stars:
                stars_str+=str(star.show_name);
                if counter>0 and len(Movie.stars)>counter:
                    stars_str+=str(' , ');
                counter=counter+1
            return stars_str

        def set_tags(Movie):
            tags_str=''
            counter=1
            for tag in Movie.tags:
                tags_str+=str(tag.name);
                if counter>0 and len(Movie.tags)>counter:
                    tags_str+=str(' , ');
                counter=counter+1
            return tags_str
        def full_name(Movie):
            return Movie.set_full_for_xlsx()


        self.worksheet.write(self.row, self.col, Movie.name)
        self.worksheet.write(self.row, self.col+1, Movie.description)
        self.worksheet.write(self.row, self.col+2, Movie.year)
        self.worksheet.write(self.row, self.col+3, Movie.src)
        self.worksheet.write(self.row, self.col+4, full_name(Movie))
        self.worksheet.write(self.row, self.col+5, Movie.country)
        self.worksheet.write(self.row, self.col+6, set_series(Movie))
        self.worksheet.write(self.row, self.col+7, set_producent(Movie))
        self.worksheet.write(self.row, self.col+8, set_stars(Movie))
        self.worksheet.write(self.row, self.col+9, set_tags(Movie))

    def load(self):
        self.row = 0
        self.col = 0
        for Movie in session.query(Movies).all():
            self.movies.append(Movie)
        for Movie in self.movies:
            self.add_row(Movie)
            self.col=0
            self.row += 1
        self.workbook.close()

class StarConfigData(AbstractConfigItem):

    Model = Stars

    def set_singles(self,Star):
        if Star.singles == singles_movies_defult:
            for logo in os.listdir(Star.dir + '\photo'):
                dir = Star.dir + "\photo\\" + logo;
                if Path(dir).stem == 'singles':
                    Star.singles = dir

    def set_none(self,Star):
        if Star.none == none_movies_defult:
            for logo in os.listdir(Star.dir + '\photo'):
                dir = Star.dir + "\photo\\" + logo;
                if Path(dir).stem == 'none':
                    Star.none = dir

    def load(self):
        with open(self.config) as json_file:

            data = json.load(json_file)
            if 'fields' in data:
                self.set_data_form_json(data['fields'], self.data)

            if "tags" in data:
                self.add_tags(data['tags'], self.data)

            self.set_avatar(self.data)
            self.set_singles(self.data)
            self.set_none(self.data)
class CreateMovieList(AbstractConfigItem):

    def __init__(self, json_data):
        self.dir = json_data

    def create_list(self,Star):
        if Path(Star.dir + '\\list.JSON').is_file() is True:
            os.remove(Star.dir + '\\list.JSON')
        Movies=[];
        for Movie in Star.movies:
            Movies.append(Movie.src)
        f = open(Star.dir + '\\list.JSON', "x")
        f.write(json.dumps(Movies))
        f.close()

    def load(self):
        for Star in session.query(Stars).all():
            self.create_list(Star)

class ProducentConfigData(AbstractConfigItem):

    Model = Producent

    def add_series(self,series,Obj):
        for serie in series:
            ASVD=AddSeriesViaDir(set_dir_for_star(serie))
            SeriesObj=ASVD.if_series_exist(ASVD.name)
            Obj.series.append(SeriesObj)
            session.commit()

    def load(self):
        with open(self.config) as json_file:
            data = json.load(json_file)

            if 'fields' in data:
                self.set_data_form_json(data['fields'], self.data)

            if "series" in data:
                self.add_series(data['series'], self.data)

class ConfigMovies(AbstractConfigItem):

    Movies=Movies
    dir_DB=''

    def __init__(self,json_data):
        self.dir=json_data

    def set_cover(self,Movie):
        for logo in os.listdir(Movie.dir):
            dir = Movie.dir+'\\'+logo;
            if Path(dir).stem == 'cover':
                Movie.avatar=dir

    def config(self,Movie,dir):
        self.add_config_json(dir)
        with open(dir + '/config.JSON') as f:
            data = json.load(f)
            if 'fields' in data:
                self.set_data_form_json(data['fields'], Movie)

            if "tags" in data:
                self.add_tags(data['tags'], Movie)

            if "stars" in data:
                self.add_stars(data['stars'], Movie)

            self.set_cover(Movie)

    def make_dir(self,Movie):
        if len(Movie.series):
            series = self.dir + '\\series'
            series_name = series + '\\'+Movie.series[0].name
            sezon_dir=series_name+'\\'+str(Movie.sezon)
            movie_dir=sezon_dir+'\\'+Movie.name

            if os.path.isdir(series) is False:
                os.mkdir(series)

            if os.path.isdir(series_name) is False:
                os.mkdir(series_name)

            if os.path.isdir(sezon_dir) is False:
                os.mkdir(sezon_dir)

            if os.path.isdir(sezon_dir) is False:
                os.mkdir(sezon_dir)

            if os.path.isdir(movie_dir) is False:
                os.mkdir(movie_dir)

        else:
            movies = self.dir+'\\movies'
            if os.path.isdir(movies) is False:
                os.mkdir(movies)

            movie_dir = movies+'\\'+Movie.name
            if os.path.isdir(movie_dir) is False:
                os.mkdir(movie_dir)

        self.config(Movie,movie_dir)

    def add_config_json(self,dir):
        config=dir+'\\config.JSON'
        galery=dir+'\\skip_galery.JSON'

        if os.path.isfile(config) is False:
            f = open(config, "x")
            f.write('{}')
            f.close()

        if os.path.isfile(galery) is False:
            f = open(galery, "x")
            f.write('[]')
            f.close()


    def load(self):
        for Movie in session.query(Movies).all():
            self.make_dir(Movie)

class SetTags(AbstractConfigItem):

    def __init__(self, json_data):
        self.dir = json_data

    def set_tags(self,Movie):
        def set_tag_from_series(Movie):
            series=Movie.series[0]
            for tag in series.tags:
                Movie.tags.append(tag)
        def set_tag_from_star(Movie):
            for star in Movie.stars:
                for tag in star.tags:
                    Movie.tags.append(tag)
        set_tag_from_series(Movie)
        set_tag_from_star(Movie)

    def set(self):
        for Movie in session.query(Movies).all():
            self.set_tags(Movie)

    def load(self):
        pass

class AbstractConfig(ABC):

    LoadSetingsClass=None

    def __init__(self,dir):
        self.dir=dir

    def set(self):
        loop_dir = os.listdir(self.dir)
        for item in loop_dir:
            dir = self.dir + '' + str('\\' + item)
            OBJ = self.LoadSetingsClass(dir)
            OBJ.load_dir()

class AbstractLoadSetings(ABC):

    ItemClass=None

    def __init__(self,dir):
        self.dir=dir

    def load_dir(self):
        loop_dir = os.listdir(self.dir)
        for item in loop_dir:
            dir = self.dir + '' + str('\\' + item)
            self.ItemClass(dir).load()

class LoadSetingsProducent(AbstractLoadSetings):

    ItemClass = ProducentConfigData

class LoadSetingsSeries(AbstractLoadSetings):

    ItemClass = SeriesConfigData

class LoadSetingsStars(AbstractLoadSetings):

    ItemClass = StarConfigData

class ConfigStars(AbstractConfig):

    LoadSetingsClass= LoadSetingsStars

class ConfigSeries(AbstractConfig):

    LoadSetingsClass = LoadSetingsSeries

class ConfigProducent(AbstractConfig):

    LoadSetingsClass = LoadSetingsProducent

class ConfigLoop:

    def __init__(self, json_data):
        self.json_data = json_data
        self.object = {
            "stars":  ConfigStars,
            "series": ConfigSeries,
            "producents":ConfigProducent
        }

    def load(self):
        for item in self.json_data:
            if item['type'] != 'photos':
                LD = self.object[item['type']]
                LD = LD(item['dir'])
                LD.set()