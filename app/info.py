from core.datamanipulation import Data as Data
from core.strings import stringManipupations
from app.db.models import Movies, Stars, Series, Producent
from app.db.models import session
from core.setings import data_JSON, movie_ext
import os
import json

class BaseInfo:
    data_info=[]
    def __init__(self, Obj=None, methods=[]):
        if Obj is not None:
            self.BaseView=Obj.BaseView
            self.list=Obj.list

    def show_stars_in_string(self,stars):
        stars_str = ''
        count = 0
        if len(stars)>1:
            for el in stars:
                if count > 0:
                    stars_str = stars_str + ' , '
                if count % 4 == 0:
                    stars_str = stars_str + ' <br> '
                stars_str = stars_str + str(el.show_name)
                count = count + 1

            return stars_str
        else:
            if len(stars)==1:
                stars_str = stars[0].show_name
        return stars_str

class SingleSectionInfo(BaseInfo):

    def set_obj(self,Obj,item):
        self.Obj=Obj
        self.item=item

    def return_data(self):
        self.data_info = []
        info_item = None
        for el in self.Obj.sezons:
            if int(el.name)==int(self.item):
                info_item=el
        count = self.count_in_seazon(info_item)
        stars_in_seazom= self.show_stars_in_string(self.count_star(info_item))

        if info_item.year:
            self.data_info.append({
                "itemNmae": "Year",
                "itemName2": info_item.year
            })
        if count>1:
            self.data_info.append({
                "itemNmae": "Movies",
                "itemName2": str(count)
            })
            if info_item.sezon_name:
                self.data_info.append({
                    "itemNmae": "Name",
                    "itemName2": info_item.sezon_name
                })

        if stars_in_seazom:
            self.data_info.append({
                "itemNmae": stars_in_seazom,
                "itemName2": ""
            })
        return self.data_info

    def count_star(self,seazon):
        stars=[]
        def add_if_not_exist(Star):
            stan=False
            for item in stars:
                if item.id == Star.id:
                    stan=True

            if stan is False:
                stars.append(Star)

        for item in self.Obj.movies:
            if int(seazon.name) == item.sezon:
                for star in item.stars:
                    add_if_not_exist(star)

        return stars

    def count_in_seazon(self,seazon):
        count=0
        for item in self.Obj.movies:
            if int(seazon.name) == item.sezon:
                count=count+1
        return count

class MovisWithStar(BaseInfo):

    def return_data(self):
        return [
            {"itemNmae": "Movies", "itemName2": "anser1"},
        ]

class PrducentInfo(BaseInfo):
    tag_limit = 1000
    def return_data(self):
        self.data_info = []
        self.data_info.append({
            "itemNmae": "Views / Likes",
            "itemName2": str(self.BaseView.data.views) + ' / ' + str(self.BaseView.data.likes)
        })
        self.data_info.append({
            "itemNmae": "Favourite",
            "itemName2": str(self.BaseView.data.favourite)
        })
        self.data_info.append({
            "itemNmae": "Series",
            "itemName2": str(len(self.BaseView.data.series))
        })

        self.data_info.append({
            "itemNmae": "Movies",
            "itemName2": str(self.movies_count(self.BaseView.data.series))
        })

        if len(self.BaseView.data.tags) > 0:
            self.data_info.append({
                "itemNmae": "Tags",
                "itemName2": stringManipupations.short(
                    stringManipupations.array_to_string(
                        self.BaseView.data.tags
                    ),
                    self.tag_limit)
            })
        return self.data_info

    def movies_count(self, series):
        counter = 0
        for serie in series:
            counter = counter + len(serie.movies)
        return counter

class RaportInfo(BaseInfo):

    def return_data(self):
        return [
            {"itemNmae": "Movies", "itemName2": str(self.counter(Movies))},
            {"itemNmae": "Stars", "itemName2": str(self.counter(Stars))},
            {"itemNmae": "Series", "itemName2": str(self.counter(Series))},
            {"itemNmae": "Producents", "itemName2": str(self.counter(Producent))},
        ]

    def counter(self, Model):
        return session.query(Model).count()

class MovieScanInfoSection(BaseInfo):
    counter_object=0

    def return_counter(self):
        return self.counter_object

    def return_data(self):
        data= [
            {"itemNmae": "Movies", "itemName2": str(self.counter_movies(Movies))},
            {"itemNmae": "Stars", "itemName2": str(self.counter_stars(Stars))},
            {"itemNmae": "Series", "itemName2": str(self.counter_series(Series))},
            {"itemNmae": "Producents", "itemName2": str(self.counter_producent(Producent))},
        ]
        return data

    def counter(self, Model):
        return session.query(Model).count()

    def count_item_in_dir(self, Model,index):
        item = self.set_dir(index)
        dir = os.listdir(item['dir'])
        count = 0
        for el in dir:
            new_dir = item['dir'] + '' + str('\\' + el)
            list = os.listdir(new_dir)
            count = count + len(list)
        movies_in_db = session.query(Model).count()
        return_count=count - movies_in_db
        self.counter_object=self.counter_object+return_count
        return return_count

    def set_dir(self,index):
        item = []
        for type in data_JSON['dirs']:
            if type['type'] == index:
                item = type
        return item

    def counter_movies(self, Model):
        def count_movies(dir):
            movie_dir = dir+ '' + '\movies'
            listSeries=os.listdir(movie_dir)
            count=0
            for dir_element in listSeries:
                nev_dir = movie_dir + '' + '\\' + str(dir_element) + '\\DATA'
                nev_dir_loop = []
                if os.path.isdir(nev_dir):
                    nev_dir_loop = os.listdir(nev_dir)
                for movie in nev_dir_loop:
                    if movie.endswith(movie_ext):
                        count=count+1
            return count
        def movies_series_by_series():
            item = self.set_dir('series')
            count = 0
            dir= os.listdir(item['dir'])
            for el in dir:
                new_dir = item['dir'] + '' + str('\\' + el)
                list = os.listdir(new_dir)
                for dir_element in list:
                    count=count + count_movies(new_dir + '' + str('\\' + dir_element))
            return count
        movies_in_db = session.query(Model).count()
        movies_series = movies_series_by_series()
        return_count=movies_series - movies_in_db
        self.counter_object = self.counter_object + return_count
        return return_count

    def counter_stars(self,Model):
        return self.count_item_in_dir(Model,'stars')

    def counter_series(self,Model):
        return self.count_item_in_dir(Model,'series')

    def counter_producent(self,Model):
        return self.count_item_in_dir(Model,'producents')

class ConfigInfoSection(MovieScanInfoSection):

    def count_config_items(self,index,Model):
        item = self.set_dir(index)
        count = 0
        dir = os.listdir(item['dir'])
        for el in dir:
            new_dir = item['dir'] + '' + str('\\' + el)
            list = os.listdir(new_dir)
            for dir_element in list:
                count = count + self.count_series(dir_element, Model)
        return count

    def count_series(self,dir,Model):
        count = 0
        Model = session.query(Model).filter(Model.name == dir).first()
        if Model is not None:
            with open(Model.config) as json_file:
                data = json.load(json_file)
                if 'fields' in data:
                    for item in data['fields']:
                        if hasattr(Model, item['db']):
                            if getattr(Model, item['db']) != item['value']:
                                count = count + 1
        return count

    def counter_movies(self,Model):
        def config_movie(dir):
            sezons=os.listdir(dir)
            count = 0
            for movies_dir in sezons:
                movies_sezons=os.listdir(dir+'\\\\\\\\'+movies_dir)
                for movie_sezons in movies_sezons:
                    Model = session.query(Movies).filter(Movies.name == dir).first()
                    if Model is not None:
                        with open(Model.config) as json_file:
                            data = json.load(json_file)
                            print(data)
                            if 'fields' in data:
                                for item in data['fields']:
                                    if hasattr(Model, item['db']):
                                        if getattr(Model, item['db']) != item['value']:
                                            count = count + 1
            return count
        count = 0
        movies_dir=data_JSON['movies_photos']
        series_dir=movies_dir+'\\\\\\\\series'
        list = os.listdir(series_dir)
        for main_dir in list:
            for sorted_dir in os.listdir(series_dir+'\\\\\\\\'+main_dir):
                count=config_movie(series_dir+'\\\\\\\\'+main_dir+'\\\\\\\\'+sorted_dir)
                count = count + 1

        return count

    def counter_series(self, Model):
        return self.count_config_items('series',Model)

    def counter_stars(self,Model):
        return self.count_config_items('stars', Model)

    def counter_producent(self,Model):
        return self.count_config_items('producents', Model)

class InfoForMovie(BaseInfo):

    tag_limit=1000
    
    def return_data(self):
        self.data_info = []
        self.data_info.append({
            "itemNmae": "Views / Likes",
            "itemName2": str(self.BaseView.data.views) + ' / ' + str(self.BaseView.data.likes)
        })

        self.data_info.append({
            "itemNmae": "Favourite",
            "itemName2": str(self.BaseView.data.favourite)
        })
        stars=self.BaseView.data.stars
        if stars:
            self.data_info.append({
                "itemNmae": "Stars",
                "itemName2": self.show_stars_in_string(stars)
            })

        if self.BaseView.data.country:
            self.data_info.append({
                "itemNmae": "Country",
                "itemName2": self.BaseView.data.country
            })

        if self.BaseView.data.year:
            self.data_info.append({
                "itemNmae": "Year",
                "itemName2":self.BaseView.data.year
            })

        if len(self.BaseView.data.tags)>0:
            self.data_info.append({
                "itemNmae": "Tags",
                "itemName2": stringManipupations.short(
                    stringManipupations.array_to_string(
                        self.BaseView.data.tags
                    ),
                    self.tag_limit)
            })

        return  self.data_info

class InfoSection(BaseInfo):

    tag_limit=1000
    description_limit=30

    def return_data(self):
        self.data_info=[]

        if self.BaseView.data.years:
            self.data_info.append({
                "itemNmae": "Year",
                "itemName2": self.BaseView.data.years
            })

        if self.BaseView.data.country:
            self.data_info.append({
                "itemNmae": "Country",
                "itemName2": self.BaseView.data.country
            })

        if len(self.BaseView.data.sezons) != len(self.BaseView.data.movies):
            self.data_info.append({
                "itemNmae": "Sezons",
                "itemName2": str(len(self.BaseView.data.sezons))
            })

        self.data_info.append({
            "itemNmae": "Movies",
            "itemName2": str(len(self.BaseView.data.movies))
        })

        self.data_info.append({
            "itemNmae": "Views / Likes",
            "itemName2": str(self.BaseView.data.views)+' / '+str(self.BaseView.data.likes)
        })

        self.data_info.append({
            "itemNmae": "Favourite",
            "itemName2": str(self.BaseView.data.favourite)
        })
        if len(self.BaseView.data.tags)>0:
            self.data_info.append({
                "itemNmae": "Tags",
                "itemName2": stringManipupations.short(
                    stringManipupations.array_to_string(
                        self.BaseView.data.tags
                    ),
                    self.tag_limit)
            })

        return  self.data_info

class StarInfoSection(BaseInfo):

    tag_limit=1000

    def return_data(self):
        self.data_info=[]
        self.add_date_of_birth()
        self.add_height_and_weight()
        self.if_data(self.BaseView.data.ethnicity, 'Ethnicity')
        self.if_data(self.BaseView.data.hair_color, 'Hair color')
        self.add_series_and_movies()
        self.add_views_and_likes()
        self.if_data(str(self.BaseView.data.favourite), 'Favourite')
        self.add_tags()
        return  self.data_info

    def add_tags(self):
        if len(self.BaseView.data.tags) > 0:
            self.data_info.append({
                "itemNmae": "Tags",
                "itemName2": stringManipupations.short(
                    stringManipupations.array_to_string(
                        self.BaseView.data.tags
                    ),
                    self.tag_limit)
            })

    def add_date_of_birth(self):
        DataObj=None
        if self.BaseView.data.date_of_birth:
            DataObj = Data(self.BaseView.data.date_of_birth)

        if DataObj is not None:
            self.data_info.append({
                "itemNmae": "Date of birth / Age",
                "itemName2": DataObj.show() + ' / ' + DataObj.get_age()
            })

    def add_height_and_weight(self):

        if self.BaseView.data.height and self.BaseView.data.weight:
            self.data_info.append({
                "itemNmae": "Height / Weight",
                "itemName2": str(self.BaseView.data.height) + ' cm  / ' + str(self.BaseView.data.weight) + ' kg'
            })

    def add_series_and_movies(self):

        self.data_info.append({
            "itemNmae": "Movies / Series",
            "itemName2": self.count_series() + ' / ' + self.count_movies()
        })

    def is_method(self, method):
        return callable(getattr(self.BaseView, method, None))

    def add_views_and_likes(self):
        self.data_info.append({
            "itemNmae": "Views / Likes",
            "itemName2": str(self.BaseView.data.views) + ' / ' + str(self.BaseView.data.likes)
        })

    def if_data(self,data,name):

        if data:
            self.data_info.append({
                "itemNmae":  name,
                "itemName2": data
            })

    def count_series(self):
        return str(len(self.BaseView.data.series))

    def count_movies(self):
        return str(len(self.BaseView.data.movies))







