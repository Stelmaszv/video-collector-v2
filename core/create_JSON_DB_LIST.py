import json
import math
import os
import os.path
from abc import ABC
from pathlib import Path

from app.db.models import Movies, Producent, Series, Stars, session
from core.custum_errors import Error
from core.setings import data_JSON, photo_ext

producent_fields_defult = ['country', "baner", "year"]
producent_fields_defult2 = ['country', 'series', "baner", "year", "top_stars", "short_series"]
series_fields_defults = ["years", "country", "number_of_sezons", "producent", "baner", "short_stars"]
movies_fields_defults = ["src", "short_stars", "sezon", "date_relesed", "country", "short_series", "producent",
                         "poster"]
stars_fields_defults = ['weight', 'height', 'ethnicity', 'hair_color', 'short_series', 'nationality', 'birth_place',
                        'date_of_birth']
defult_producents_pages = 1
defult_movis = 10
defult_stars = 10
defult_series = 10

class CreateJSONDBLIST:
    Sesion = session
    series_fields = series_fields_defults
    stars_fields = stars_fields_defults
    movies_fields = movies_fields_defults
    producent_fields = producent_fields_defult2

    def base_get(self, Model, atters):

        if hasattr(Model, "__len__"):
            loop_all = Model
        else:
            loop = self.loop(Model)
            loop_all = loop.all()
        array_return = []
        for item_db in loop_all:
            item = self.add_defults(item_db)
            for atter in atters:
                if atter != "series" or atter != "stars" or atter != "top stars" or atter != "src" or atter != "producent":
                    if hasattr(item_db, atter):
                        item[atter] = str(getattr(item_db, self.escepe_string(atter)))
                if atter == "producent":
                    item["producent"] = self.return_producent(item_db)
                if atter == "src":
                    item[atter] = self.escepe_string(getattr(item_db, self.escepe_string(atter)))
                if atter == "series":
                    item["series"] = self.return_series(item_db)
                if atter == "movies":
                    item["movies"] = self.return_movies(item_db)
                if atter == "stars":
                    item["stars"] = self.return_stars(item_db)
                if atter == "top_stars":
                    item["top_stars"] = self.return_top_stars(item_db)
                if atter == "short_series":
                    item["short_series"] = self.return_short_series(item_db)
                if atter == "short_stars":
                    item["short_stars"] = self.return_short_stars(item_db)
            array_return.append(item)
        return array_return

    def return_producent(self, item_db):
        if hasattr(item_db, "producent"):
            if len(item_db.producent):
                return {
                    "name": item_db.producent[0].show_name,
                    "dir": self.escepe_string(item_db.producent[0].dir),
                    "avatar": item_db.producent[0].avatar,
                }
        if hasattr(item_db, "series"):
            if len(item_db.series):
                if hasattr(item_db.series[0], "producent"):
                    if len(item_db.series[0].producent):
                        return {
                            "name": item_db.series[0].producent[0].show_name,
                            "dir": self.escepe_string(item_db.series[0].producent[0].dir),
                            "avatar": item_db.series[0].producent[0].avatar,
                        }
        return {}

    def return_short_stars(self, item_db):
        array = []
        for item_db in item_db.stars:
            tag_json = {
                "id": item_db.id,
                "name": item_db.name,
                "dir": self.escepe_string(item_db.dir),
                "avatar": item_db.avatar,
            }
            array.append(tag_json)
        return array

    def return_short_series(self, item_db):
        if len(item_db.series):
            return {
                "id": item_db.series[0].id,
                "name": item_db.series[0].show_name,
                "dir": self.escepe_string(item_db.series[0].dir),
                "avatar": item_db.series[0].avatar,
                "tag": self.return_tags(item_db.tags),
                "short_stars": self.return_short_stars(item_db.series[0])
            }
        return {} 
    
    def return_short_producent(self, item_db):
        if len(item_db.series):
            if len(item_db.series[0].producent):
                producent = item_db.series[0].producent[0]
                return {
                    "id": producent.id,
                    "show_name": producent.show_name,
                    "dir": producent.dir,
                    "avatar": producent.avatar
                }
            return {}
        return {}   

    def return_top_stars(self, item):
        top_stars = []
        dir = item.dir + '/stars_counter.JSON'
        if os.path.isfile(dir) is False:
            dir = item.series[0].dir + '/stars_counter.JSON'
        with open(dir) as json_file:
            data = json.load(json_file)
            for star in data:
                if star['Count'] >= 3:
                    top_stars.append(star["StarObj"])
        return top_stars

    def return_stars(self, item):
        return self.base_get(item.stars, self.stars_fields)

    def return_movies(self, item):
        return self.base_get(item.movies, self.movies_fields)

    def return_series(self, item):
        return self.base_get(item.series, self.series_fields)

    def return_tags(self, tags):
        tags_array = []
        for tag in tags:
            tag_json = {
                "id": tag.id,
                "name": tag.name,
            }
            tags_array.append(tag_json)
        return tags_array

    def add_defults(self, item):
        data_JSON = {
            "id": item.id,
            "name": item.name,
            "show_name": item.show_name,
            "dir": self.escepe_string(item.dir),
            "description": item.description,
            "avatar": item.avatar,
            "rating": item.rating,
            "likes": item.likes,
            "views": item.likes,
            "favourite": str(getattr(item, self.escepe_string("favourite"))),
            "tags": self.return_tags(item.tags)
        }
        return data_JSON

    def escepe_string(self, string):
        return string.replace('\\', '/')

    def loop(self, Model):
        return self.Sesion.query(Model)

    def get_producnets(self):
        return self.base_get(Producent, self.producent_fields)

    def get_movies(self):
        return self.base_get(Movies, self.movies_fields)

    def get_series(self):
        return self.base_get(Series, self.series_fields)

    def get_stars(self):
        return self.base_get(Stars, self.stars_fields)

    def create_pagination(self, data, per_page):
        count = len(data)
        pages = math.ceil(count / per_page)
        new_array = []
        index = 0
        for el in range(1, pages + 1):
            movies = []
            elments = 0
            for item in data:
                if elments < per_page and index < count:
                    movies.append(data[index])
                    index = index + 1
                elments = elments + 1

            new_array.append({"page": el, "Objets": movies})
        return new_array

    def generate_movies_output(self,limit):

        def clear_pages():
            dir_list = os.listdir('OUTPUT/movies')
            for dir in dir_list:
                os.remove('OUTPUT/movies/'+dir)

        def create_movie_list(pages):

            def valid_page(page):
                if page<10:
                    return '0'+str(page)
                return str(page)

            for page in pages:
                name = 'OUTPUT/movies/' + valid_page(page['page']) + '.js'
                if Path(name).is_file() is True:
                    os.remove(name)
                f = open(name, "x")
                string = 'movies = '+str(json.dumps(page['Objets']))+''
                f.write(string)
                f.close()
        clear_pages()
        pages=self.create_pagination(self.get_movies(),limit)
        if os.path.isdir('OUTPUT/movies') is False:
            os.mkdir('OUTPUT/movies')
        create_movie_list(pages)

    def generate_movies_list(self):
        def generete_dir_list():
            file_list=[]
            dir_name='OUTPUT/movies'
            dir_list = os.listdir(dir_name)
            for dir in dir_list:
                file=data_JSON['html_output']+'/HTML Generator/js/movies/'+dir
                file_list.append(file)
            return file_list

        file_name='HTML_Genarator/js/movies_list.js'
        if Path(file_name).is_file() is True:
            os.remove(file_name)
        f = open(file_name, "x")
        string =     'var data = ' + str(generete_dir_list())+' \n'
        data_count = 'var data_count = ' + str(len(self.get_movies()))
        string=string+str(data_count)
        f.write(string)
        f.close()

    def create_js_counter(self):
        file_name = 'HTML_Genarator/js/counter_data.js'
        if Path(file_name).is_file() is True:
            os.remove(file_name)
        f = open(file_name, "x")
        movies_count  = 'const movies_count = ' + str(len(self.get_movies()))+' \n'
        series_count = 'const series_count = ' + str(len(self.get_series()))+' \n'
        stars_count = 'const stars_count = ' + str(len(self.get_stars())) + ' \n'
        producents_count = 'const producents_count = ' + str(len(self.get_producnets())) + ' \n'
        string = movies_count + series_count+ stars_count + producents_count
        f.write(string)
        f.close()

    def create(self):
        list = [
            {"OBJ": self.get_producnets(),
             'name': 'OUTPUT/json/producents.JSON', 'js': 'OUTPUT/js/producents.js', 'var_name': 'producents'},
            {"OBJ": self.get_series(),
             'name': 'OUTPUT/json/series.JSON',
             'js': 'OUTPUT/js/series.js', 'var_name': 'series'},
            {"OBJ": self.get_movies(), 'name': 'OUTPUT/json/movies.JSON',
             'js': 'OUTPUT/js/movies.js', 'var_name': 'movies'},
            {"OBJ": self.get_stars(), 'name': 'OUTPUT/json/stars.JSON',
             'js': 'OUTPUT/js/stars.js', 'var_name': 'stars'},
        ]

        if os.path.isdir('OUTPUT') is False:
            os.mkdir('OUTPUT')
            if os.path.isdir('OUTPUT/json') is False:
                os.mkdir('OUTPUT/json')
            if os.path.isdir('OUTPUT/js') is False:
                os.mkdir('OUTPUT/js')
        self.generate_movies_output(10)
        self.generate_movies_list()
        self.create_js_counter()

        for el in list:
            if Path(el['name']).is_file() is True:
                os.remove(el['name'])
            f = open(el['name'], "x")
            f.write(json.dumps(el['OBJ']))
            f.close()
            if Path(el['js']).is_file() is True:
                os.remove(el['js'])
            f = open(el['js'], "x")
            string = 'var ' + el['var_name'] + ' = ' + str(el['OBJ'])
            f.write(string)
            f.close()

class AbstratJSONOtpus(ABC):
    input = ""
    Model = None
    fields = []
    CreateJSONDBLISTObj = CreateJSONDBLIST()

    def defult_add(self, Movie):
        data_JSON = {
            "id": Movie["id"],
            "name": Movie["name"],
            "show_name": Movie["show_name"],
            "dir": Movie["dir"],
            "description": Movie["description"],
            "avatar": Movie["avatar"],
            "tags": Movie['tags'],
            "rating": Movie['rating'],
            "likes": Movie['likes'],
            "views": Movie['views'],
        }
        return self.add_fields(data_JSON, Movie)

    def add_fields(self, data_JSON, Movie):
        return data_JSON

    def create(self):
        Error.throw_error_bool("input not exist", self.input != "")
        with open(self.input) as json_file:
            data = json.load(json_file)
            for movie in data:
                if Path(movie["dir"] + '\db.js').is_file() is True:
                    os.remove(movie["dir"] + '\db.js')
                f = open(movie["dir"] + '\db.js', "x")
                string = 'var data = ' + str(self.defult_add(movie))
                f.write(string)
                f.close()

    def add_index(self, fields, data_JSON, Movie):
        for el in fields:
            if el != "producent":
                data_JSON[el] = Movie[el]


class GenerateJSONOtputsMovies(AbstratJSONOtpus):
    input = "OUTPUT/json/movies.JSON"
    fields = movies_fields_defults
    Model = Movies

    def add_fields(self, data_JSON, Movie):
        print("creating JSON OUTPUT for movie " + data_JSON['name'])
        self.add_index(self.fields, data_JSON, Movie)
        data = session.query(self.Model).filter(self.Model.name == data_JSON['name']).first()
        data_JSON['photos'] = self.return_galery(data_JSON)
        data_JSON['producent'] = self.CreateJSONDBLISTObj.return_short_producent(data)
        return data_JSON

    def set_movies_with_star(self, stars):
        movies = []
        for star in stars:
            for star_movie in star.movies:
                if star_movie not in movies:
                    movies.append(star_movie)
        return movies

    def return_galery(self, JSON):
        photos = []
        for item in os.listdir(JSON['dir']):
            with open(JSON['dir'] + '\\skip_galery.JSON') as json_file:
                data = json.load(json_file)
                if item.endswith(photo_ext) and item not in data:
                    photos.append({"photo": item, "name": JSON['name']})
        return photos


class GenerateJSONOtputsStars((AbstratJSONOtpus)):
    input = "OUTPUT/json/stars.JSON"
    fields = stars_fields_defults
    Model = Stars

    def add_fields(self, data_JSON, Movie):
        print("creating JSON OUTPUT for Star " + data_JSON['name'])
        self.add_index(self.fields, data_JSON, Movie)
        data = session.query(self.Model).filter(self.Model.name == data_JSON['name']).first()
        data_JSON['movies'] = self.CreateJSONDBLISTObj.base_get(data.movies, movies_fields_defults)
        data_JSON['photos'] = self.return_galery(data_JSON, Movie)
        return data_JSON

    def return_galery(self, JSON, Movie):
        name = JSON['name']
        photos = []
        dir = os.listdir(JSON['dir'] + '\\photo\DATA')

        for item in dir:

            with open(JSON['dir'] + '\\skip_galery.JSON') as json_file:
                data = json.load(json_file)

            if item.endswith(photo_ext) and item not in data:
                new_item = JSON['dir'] + '\\photo\DATA\\' + item
                photos.append({"photo": new_item, "name": JSON['name']})

        for movie in JSON['movies']:
            for star in movie['short_stars']:
                if star['name'] == JSON['name']:
                    for item in os.listdir(movie['dir']):
                        with open(movie['dir'] + '\\skip_galery.JSON') as json_file:
                            data = json.load(json_file)
                        if item.endswith(photo_ext) and item not in data:
                            new_item = movie['dir'] + '\\' + item
                            name = movie['short_series']['name'] + ' - ' + movie['name']
                            photos.append({"photo": new_item, "name": name})
        return photos


class GenerateJSONOtputsSeries(AbstratJSONOtpus):
    input = "OUTPUT/json/series.JSON"
    fields = series_fields_defults
    Model = Series

    def return_banners(self,data):
        dir=data.dir+'\\banners'
        ndir=[]
        if os.path.exists(dir):
            for dir_of_benners_item in os.listdir(dir):
                el=dir+'\\'+dir_of_benners_item
                ndir.append(el)
        return ndir

    def add_fields(self, data_JSON, Movie):
        print("creating JSON OUTPUT for Series " + data_JSON['name'])
        self.add_index(self.fields, data_JSON, Movie)
        data = session.query(self.Model).filter(self.Model.name == data_JSON['name']).first()
        data_JSON['movies'] = self.CreateJSONDBLISTObj.base_get(data.movies, movies_fields_defults)
        data_JSON['stars'] = self.CreateJSONDBLISTObj.return_top_stars(data)
        data_JSON['photos'] = self.return_galery(data_JSON, data)
        data_JSON['producent'] = self.CreateJSONDBLISTObj.return_producent(data_JSON)
        data_JSON['banner'] = self.return_banners(data)
        return data_JSON

    def return_galery(self, JSON, data):
        movies=data.movies
        photos = []
        dir = os.listdir(JSON['dir'] + '\\photo\DATA')
        for item in dir:

            with open(JSON['dir'] + '\\skip_galery.JSON') as json_file:
                data = json.load(json_file)

            if item.endswith(photo_ext) and item not in data:
                new_item = JSON['dir'] + '\\photo\DATA\\' + item
                photos.append({"photo": new_item, "name": JSON['name']})

        for movie in movies:
            for item in os.listdir(movie.dir):

                with open(movie.dir + '\\skip_galery.JSON') as json_file:
                    data = json.load(json_file)

                if item.endswith(photo_ext) and item not in data:
                    new_item = movie.dir + '\\' + item
                    name = JSON['name'] + ' - ' + movie.name
                    photos.append({"photo": new_item, "name": name})
        return photos


class GenerateJSONOtputsProducent(AbstratJSONOtpus):
    input = "OUTPUT/json/producents.JSON"
    fields = producent_fields_defult
    Model = Producent

    def return_galery(self, JSON, data):
        photos = []

        dir = os.listdir(JSON['dir'] + '\\photo\DATA')
        for item in dir:

            with open(JSON['dir'] + '\\skip_galery.JSON') as json_file:
                data = json.load(json_file)

            if item.endswith(photo_ext) and item not in data:
                new_item = JSON['dir'] + '\\photo\DATA\\' + item
                photos.append({"photo": new_item, "name": JSON['name']})

        for movie in JSON['movies']:
            for dir in os.listdir(movie['dir']):

                with open(movie['dir'] + '\\skip_galery.JSON') as json_file:
                    data = json.load(json_file)

                if dir.endswith(photo_ext) and movie not in data:
                    new_item = movie['dir'] + '\\' + dir
                    name = movie['short_series']['name'] + ' - ' + movie['name']
                    photos.append({"photo": new_item, "name": name})

        return photos

    def return_banners(self,data):
        dir=data.dir+'\\banners'
        ndir=[]
        if os.path.exists(dir):
            for dir_of_benners_item in os.listdir(dir):
                el=dir+'\\'+dir_of_benners_item
                ndir.append(el)
        return ndir

    def add_movies(self, data):
        movies = [];
        for series in data:
            for Movie in series.movies:
                data_JSON = self.CreateJSONDBLISTObj.add_defults(Movie)
                data_JSON['short_series'] = self.CreateJSONDBLISTObj.return_short_series(Movie)
                data_JSON['short_stars'] = self.CreateJSONDBLISTObj.return_short_stars(Movie)
                movies.append(data_JSON)
        return movies

    def add_fields(self, data_JSON, Movie):
        print("creating JSON OUTPUT for Producent " + data_JSON['name'])
        data = session.query(self.Model).filter(self.Model.name == data_JSON['name']).first()
        self.add_index(self.fields, data_JSON, Movie)
        data_JSON['series'] = self.CreateJSONDBLISTObj.base_get(data.series, series_fields_defults)
        data_JSON['movies'] = self.add_movies(data.series)
        data_JSON['stars'] = self.CreateJSONDBLISTObj.return_top_stars(data)
        data_JSON['photos'] = self.return_galery(data_JSON, data)
        data_JSON['banner'] = self.return_banners(data)
        return data_JSON
