from abc import ABC, abstractmethod
from core.dir import set_name, if_star_exist, AddStarViaDir, set_dir_for_star, AddSeriesViaDir, set_dir_for_producent, \
    if_producent_exist, AddProducentViaDir
from app.db.models import session
from app.db.models import Tags, Series, Stars, Movies, Producent
from datetime import datetime
from core.setings import singles_movies_defult, none_movies_defult
from pathlib import Path
import os
import json
import xlsxwriter


class MovieListForStars:

    def __init__(self, star_list, dirs_list, AbstractConfigItem_data):
        self.list = star_list
        self.dirs_list = dirs_list
        self.AbstractConfigItem_data = AbstractConfigItem_data

    def add_list(self):
        for el in self.list:
            el['Movies'] = self.get_movies_list(el['Star'])
        return self.list

    def get_movies_list(self, star_name):
        movies_list = []

        for Star in self.dirs_list:
            if star_name == Star['Star']:
                movies_list.append(Star['dir'])
        return movies_list


class StarList:

    def __init__(self, star_list, AbstractConfigItem_data):
        self.list = star_list
        self.AbstractConfigItem_data = AbstractConfigItem_data
        self.is_producent = True

    def create_list(self, JSON):
        if Path(self.AbstractConfigItem_data.dir + '\\stars_counter.JSON').is_file() is True:
            os.remove(self.AbstractConfigItem_data.dir + '\\stars_counter.JSON')
        f = open(self.AbstractConfigItem_data.dir + '\\stars_counter.JSON', "x")
        f.write(json.dumps(JSON))
        f.close()

    def escepe_string(self, string):
        return string.replace('\\', '/')

    def star_do_JSON(self, Star):
        JSON = {
            "dir": self.escepe_string(Star.dir),
            "avatar": Star.avatar,
            "name": Star.show_name
        }
        return JSON

    def create_star_list(self):
        def star_count(id, stars_list):
            count = 0
            for Star in stars_list:
                if Star.id == id:
                    count = count + 1
            return count

        stars_list = []
        added = []
        for Star in self.list:
            if Star.id not in added:
                stars_list.append({
                    'Star': Star.show_name,
                    'Count': star_count(Star.id, self.list),
                    'StarObj': self.star_do_JSON(Star)
                })
                added.append(Star.id)
        return stars_list


class AbstractConfigItem(ABC):
    Model = None

    def __init__(self, dir):
        self.dir = dir
        self.session = session
        self.name = set_name(dir)
        print("Config " + str(self.name))
        self.data = session.query(self.Model).filter(self.Model.name == self.name).first()
        self.config = self.dir + '\\config.JSON'
        self.name = set_name(dir)

    def set_avatar(self, Item):
        for logo in os.listdir(Item.dir + '\photo'):
            dir = Item.dir + "\photo\\" + logo;
            if Path(dir).stem == 'avatar':
                Item.avatar = dir

    def set_baner(self, Item):
        for logo in os.listdir(Item.dir + '\photo\DATA\\'):
            dir = Item.dir + "\photo\DATA\\" + logo;
            if Path(dir).stem == 'banner':
                Item.baner = dir

    def add_stars(self, stars, Obj):
        for star in stars:
            StarObj = if_star_exist(AddStarViaDir(set_dir_for_star(star)), star)
            Obj.stars.append(StarObj)
            if hasattr(self, 'data'):
                StarObj.movies.append(self.data)
            session.commit()

    def add_tags(self, tags, Obj=None):
        if Obj is not None:
            self.data = Obj
        for tag in tags:
            query = session.query(Tags).filter(Tags.name == tag).first()
            if query is None:
                TagObj = Tags(name=tag)
                session.add_all([TagObj])
                session.commit()
                query = TagObj
            self.data.tags.append(query)
            session.commit()

    def set_data_form_json(self, el, Obj):
        def add_item(item):
            if 'data' in item:
                item['value'] = datetime(
                    item['value'][0],
                    item['value'][1],
                    item['value'][2]
                )
            setattr(Obj, item['db'], item['value'])
            session.commit()

        for item in el:
            if 'db' in item and 'value' in item:
                if hasattr(Obj, item['db']):
                    if 'available' in item:
                        if item['value'] in item['available']:
                            add_item(item)
                    else:
                        add_item(item)

    def add_list(self, Obj, atter_for_list, atter_for_literator):
        if Path(Obj.dir + '\\list.JSON').is_file() is True:
            os.remove(Obj.dir + '\\list.JSON')
        ObjectsList = [];
        for ObjInObjects in getattr(Obj, atter_for_list):
            ObjectsList.append(getattr(ObjInObjects, atter_for_literator))
        f = open(Obj.dir + '\\list.JSON', "x")
        f.write(json.dumps(ObjectsList))
        f.close()

    def dir_for_stars(self):
        if os.path.isdir(self.dir + '/stars') is False:
            os.mkdir(self.dir + '/stars')

        with open(self.dir + '/stars_counter.JSON') as json_file:
            data = json.load(json_file)
            new_array = []
            for item in data:
                if item['Count'] > 2:
                    new_array.append(item)
        self.create_star_dir(new_array)

    def create_star_dir(self, array):
        for item in array:
            new_dir = self.dir + '/stars/' + item['Star']
            if os.path.isdir(new_dir) is False:
                os.mkdir(new_dir)
            if Path(new_dir + '\\list.JSON').is_file() is True:
                os.remove(new_dir + '\\list.JSON')
            f = open(new_dir + '\\list.JSON', "x")
            f.write(json.dumps(item['Movies']))
            f.close()

    def counter(self, stars_list, movies_dir):
        def order_by_count(el):
            return el['Count']

        StarListObj = StarList(stars_list, self.data)
        list_for_JSON = StarListObj.create_star_list()
        MLFS = MovieListForStars(list_for_JSON, movies_dir, self.data)
        MLFS.add_list().sort(key=order_by_count, reverse=True)
        StarListObj.create_list(list_for_JSON)

    @abstractmethod
    def load(self):
        pass


class SeriesConfigData(AbstractConfigItem):
    Model = Series

    def stars_counter(self):

        movies_dir = []
        model_star_list = []
        for Movie in self.data.movies:
            for StarModel in Movie.stars:
                model_star_list.append(StarModel)
                movies_dir.append({"Star": StarModel.show_name, "dir": Movie.src})

        self.counter(model_star_list, movies_dir)

    def add_star_to_seazon(self, item):
        def add_star_to_movie(Star, name):
            for movie in self.data.movies:
                if movie.sezon == int(name):
                    movie.stars.append(Star)

        def add_star_to_series(Star, Series):
            Series.stars.append(Star)
            session.commit()

        sezon_name = item['name']
        for star in item['stars']:
            StarObj = if_star_exist(AddStarViaDir(set_dir_for_star(star)), star)
            add_star_to_movie(StarObj, sezon_name)
            add_star_to_series(StarObj, self.data)

    def config_sezons(self, sezons):
        for item in sezons:
            stars = "stars" in item
            if stars:
                self.add_star_to_seazon(item)

    def set_for_sezon(self, data):
        for sezon in self.data.sezons:
            for sezon_item in data:
                if sezon.name == str(sezon_item['name']):
                    if 'fields' in sezon_item:
                        self.set_data_form_json(sezon_item['fields'], sezon)

    def add_producent(self, producent, Series):
        if os.path.isdir(set_dir_for_producent(producent[0])) is False:
            os.mkdir(set_dir_for_producent(producent[0]))
            ProducentObj = if_producent_exist(AddProducentViaDir(set_dir_for_producent(producent[0])), producent[0])
            Series.producent.append(ProducentObj)

    def movies_list(self):
        def convert_to_src(movies):
            new_movies = []
            for item in movies:
                new_movies.append(item.src)
            return new_movies

        if Path(self.dir + '\\movies_list.JSON').is_file() is True:
            os.remove(self.dir + '\\movies_list.JSON')
        f = open(self.dir + '\\movies_list.JSON', "x")
        new_movies = convert_to_src(self.data.movies)
        f.write(json.dumps(new_movies))
        f.close()

    def load(self):
        self.stars_counter()
        self.dir_for_stars()
        self.movies_list()

        with open(self.config) as json_file:
            data = json.load(json_file)

            if 'fields' in data:
                self.set_data_form_json(data['fields'], self.data)

            if "tags" in data:
                self.add_tags(data['tags'], self.data)

            if "stars" in data:
                self.add_stars(data['stars'], self.data)

            if "producent" in data:
                self.add_producent(data['producent'], self.data)

            if "sezons" in data:
                self.config_sezons(data['sezons'])
                self.set_for_sezon(data['sezons'])

            self.set_avatar(self.data)
            self.set_baner(self.data)


class CreateXML(AbstractConfigItem):

    def __init__(self, json_data):
        self.dir = json_data
        self.movies = []
        self.workbook = xlsxwriter.Workbook('movies.xlsx')
        self.worksheet = self.workbook.add_worksheet()

    def add_row(self, Movie):
        def set_series(Movie):
            if len(Movie.series):
                return Movie.series[0].name
            return ''

        def set_producent(Movie):
            if len(Movie.series):
                Series = Movie.series[0]
                if len(Series.producent):
                    return Series.producent[0].name
                return ''
            return ''

        def set_object(Movie, atter_for_str, atter_for_list):
            stars_str = ''
            counter = 1
            for Star in getattr(Movie, atter_for_list):
                stars_str += str(getattr(Star, atter_for_str));
                if counter > 0 and len(getattr(Movie, atter_for_list)) > counter:
                    stars_str += str(' , ');
                counter = counter + 1
            return stars_str

        def full_name(Movie):
            return Movie.set_full_for_xlsx()

        self.worksheet.write(self.row, self.col, Movie.name)
        self.worksheet.write(self.row, self.col + 1, Movie.description)
        self.worksheet.write(self.row, self.col + 2, Movie.date_relesed)
        self.worksheet.write(self.row, self.col + 3, Movie.src)
        self.worksheet.write(self.row, self.col + 4, full_name(Movie))
        self.worksheet.write(self.row, self.col + 5, Movie.country)
        self.worksheet.write(self.row, self.col + 6, set_series(Movie))
        self.worksheet.write(self.row, self.col + 7, set_producent(Movie))
        self.worksheet.write(self.row, self.col + 8, set_object(Movie, 'show_name', 'stars'))
        self.worksheet.write(self.row, self.col + 9, set_object(Movie, 'name', 'tags'))

    def load(self):
        self.row = 0
        self.col = 0
        for Movie in session.query(Movies).all():
            self.movies.append(Movie)
        for Movie in self.movies:
            self.add_row(Movie)
            self.col = 0
            self.row += 1
        self.workbook.close()


class StarConfigData(AbstractConfigItem):
    Model = Stars

    def set_singles(self, Star):
        if Star.singles == singles_movies_defult:
            for logo in os.listdir(Star.dir + '\photo'):
                dir = Star.dir + "\photo\\" + logo;
                if Path(dir).stem == 'singles':
                    Star.singles = dir

    def set_none(self, Star):
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

    def create_list(self, Star):
        self.add_list(Star, 'movies', 'src')

    def load(self):
        for Star in session.query(Stars).all():
            self.create_list(Star)


class ProducentConfigData(AbstractConfigItem):
    Model = Producent

    def create_series_list(self):
        self.add_list(self.data, 'series', 'dir')

    def stars_in_producent(self):
        stars = []
        movies_dir = []
        for Serie in self.data.series:
            for Movie in Serie.movies:
                for Star in Movie.stars:
                    stars.append(Star)
                    movies_dir.append({"Star": Star.show_name, "dir": Movie.src})

        self.counter(stars, movies_dir)

    def add_series_list(self, series, Obj):
        for serie in series:
            ASVD = AddSeriesViaDir(set_dir_for_star(serie))
            SeriesObj = ASVD.if_series_exist(ASVD.name)
            Obj.series.append(SeriesObj)
            session.commit()

    def movies_list(self):
        def convert_to_src(movies):
            new_movies = []
            for item in movies:
                new_movies.append(item.src)
            return new_movies

        movies = []
        for el in self.data.series:
            movies.extend(el.movies)
        if Path(self.dir + '\\movies_list.JSON').is_file() is True:
            os.remove(self.dir + '\\movies_list.JSON')
        f = open(self.dir + '\\movies_list.JSON', "x")
        new_movies = convert_to_src(movies)
        f.write(json.dumps(new_movies))
        f.close()

    def load(self):
        self.stars_in_producent()
        self.create_series_list()
        self.dir_for_stars()
        self.movies_list()
        with open(self.config) as json_file:
            data = json.load(json_file)

            if 'fields' in data:
                self.set_data_form_json(data['fields'], self.data)

            if "series" in data:
                self.add_series(data['series'], self.data)

            if "tags" in data:
                self.add_tags(data['tags'], self.data)

            self.set_baner(self.data)
            self.set_avatar(self.data)


class ConfigMovies(AbstractConfigItem):
    Movies = Movies
    dir_DB = ''

    def __init__(self, json_data):
        self.dir = json_data

    def set_cover(self, Movie):
        for logo in os.listdir(Movie.dir):
            dir = Movie.dir + '\\' + logo;
            if Path(dir).stem == 'cover':
                Movie.avatar = dir

    def set_poster(self, Item):
        for logo in os.listdir(Item.dir):
            dir = Item.dir + '\\' + logo;
            if Path(dir).stem == 'poster':
                Item.poster = dir

    def config(self, Movie, dir):
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
            self.set_poster(Movie)

    def make_dir(self, Movie):
        if len(Movie.series):
            series = self.dir + '\\series'
            series_name = series + '\\' + Movie.series[0].name
            sezon_dir = series_name + '\\' + str(Movie.sezon)
            movie_dir = sezon_dir + '\\' + Movie.name

            if os.path.isdir(series) is False:
                os.mkdir(series)
            letter_of_movie = Movie.series[0].name[0]
            letter = letter_of_movie.upper()
            dir = ''

            if letter == 'A' or letter == 'B' or letter == 'C' or letter == 'D':
                dir = series + '\\A-D'
            if letter == 'E' or letter == 'F' or letter == 'G' or letter == 'H':
                dir = series + '\\E-H'
            if letter == 'I' or letter == 'J' or letter == 'K' or letter == 'L':
                dir = series + '\\I-L'
            if letter == 'M' or letter == 'N' or letter == 'O' or letter == 'P' or letter == 'Q':
                dir = series + '\\M-P'
            if letter == 'R' or letter == 'S' or letter == 'T' or letter == 'U':
                dir = series + '\\R-U'
            if letter == 'W' or letter == 'V' or letter == 'X' or letter == 'Y' or letter == 'Z':
                dir = series + '\\W-Z'

            if os.path.isdir(dir) is False:
                os.mkdir(dir)
            sereis_dir = dir + '\\' + Movie.series[0].name
            if os.path.isdir(sereis_dir) is False:
                os.mkdir(sereis_dir)

            sezon_dir = sereis_dir + '\\' + str(Movie.sezon)
            if os.path.isdir(sezon_dir) is False:
                os.mkdir(sezon_dir)
            movie_dir = sezon_dir + '\\' + Movie.name
            if os.path.isdir(movie_dir) is False:
                os.mkdir(movie_dir)
        else:
            movies = self.dir + '\\movies'
            if os.path.isdir(movies) is False:
                os.mkdir(movies)

            movie_dir = movies + '\\' + Movie.name
            if os.path.isdir(movie_dir) is False:
                os.mkdir(movie_dir)
        Movie.dir = movie_dir
        self.config(Movie, movie_dir)

    def add_config_json(self, dir):
        config = dir + '\\config.JSON'
        galery = dir + '\\skip_galery.JSON'

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
            print('Config for ' + str(Movie))
            self.make_dir(Movie)


class SetTags(AbstractConfigItem):

    def __init__(self, json_data):
        self.dir = json_data

    def set_tags(self, Movie):
        def set_tag_from_series(Movie):
            series = Movie.series[0]
            for tag in series.tags:
                Movie.tags.append(tag)

        def set_tag_from_star(Movie):
            for star in Movie.stars:
                for tag in star.tags:
                    Movie.tags.append(tag)

        if len(Movie.series) > 0:
            set_tag_from_series(Movie)
        set_tag_from_star(Movie)

    def set(self):
        for Movie in session.query(Movies).all():
            print('Adding tag for ' + str(Movie))
            self.set_tags(Movie)

    def load(self):
        pass


class AbstractConfig(ABC):
    LoadSetingsClass = None

    def __init__(self, dir):
        self.dir = dir

    def set(self):
        loop_dir = os.listdir(self.dir)
        for item in loop_dir:
            dir = self.dir + '' + str('\\' + item)
            OBJ = self.LoadSetingsClass(dir)
            OBJ.load_dir()


class AbstractLoadSetings(ABC):
    ItemClass = None

    def __init__(self, dir):
        self.dir = dir

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
    LoadSetingsClass = LoadSetingsStars


class ConfigSeries(AbstractConfig):
    LoadSetingsClass = LoadSetingsSeries


class ConfigProducent(AbstractConfig):
    LoadSetingsClass = LoadSetingsProducent


class ConfigLoop:

    def __init__(self, json_data):
        self.json_data = json_data
        self.object = {
            "series": ConfigSeries,
            "producents": ConfigProducent,
            "stars": ConfigStars
        }

    def load(self):
        for item in self.json_data:
            if item['type'] != 'photos':
                LD = self.object[item['type']]
                LD = LD(item['dir'])
                LD.set()
