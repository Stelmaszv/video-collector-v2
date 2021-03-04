import re
from app.db.models import Stars,Movies,Series,Photos,Sezons
from app.db.models import session
from abc import ABC,abstractmethod
from core.setings import series_avatar_defult,stars_avatar_defult,none_movies_defult,singles_movies_defult
from pathlib import Path
from core.setings import data_JSON
import json
from time import sleep
import os

add= False

class FaindStar:

    str = ''
    starArray=[]

    def __init__(self,dir):
        self.dir=dir
        self.start = self.dir.find("(")
        self.end = self.dir.find(")")

    def return_stars_in_string(self):
        str=''
        for i in range(self.start+1,self.end):
            str=str+self.dir[i]
        return str
    def create_star_list(self):
        str=self.return_stars_in_string()
        self.starArray = str.split('and')
        return self.starArray

class IfStar:

    validValue = "[a-zA-Z0-9]+\s+\([a-zA-Z0-9\s]+\)";

    def faind_stars(self,file):
        FS = FaindStar(file)
        if re.search(self.validValue, file):
            return FS.create_star_list()
        return None

class AbstractAddViaDir(ABC):

    movie_model=Movies
    photo_model=Photos
    sezons_model=Sezons
    movie_dir='/movies'
    photo_dir='/photo'
    star=None
    name=''
    series=None

    def __init__(self, dir):
        self.dir = dir
        self.config = self.dir + '/config.JSON'
        self.set_config()
        self.session = session
        self.IfStar = IfStar()
        self.set_movie_dir()
        self.set_photo_dir()

    def set_config(self):
        if Path(self.config).is_file() is False:
            f = open(self.config, "x")
            f.write("{}\n")
            f.close()

    def clear_name(self, dir):
        str = ''
        stop = False
        for i in range(0, len(dir)):

            if dir[i] == "[":
                stop = True

            if dir[i] == "(" :
                stop = True

            if dir[i] == ".":
                stop = True

            if stop is False:
                str = str + dir[i]

        return str

    def set_name(self):
        name=self.dir.split('/')
        last=len(name)-1
        return name[last]

    def set_movie_dir(self):
        self.movie_dir=self.dir + '' + str(self.movie_dir)

    def set_photo_dir(self):
        self.photo_dir = self.dir + '' + str(self.photo_dir)

    def set_avatar(self):
        return  self.set_photo_from_json(series_avatar_defult,'avatar')

    def if_exist(self,name,Model,add):
        Obj=self.session.query(Model).filter(Model.name == name).first()
        if Obj:
            self.star = Obj
        else:
            self.session.add_all([
                add
            ])
            self.session.commit()
            Obj = self.session.query(Model).filter(Model.name == name).first()
        return Obj

    def if_movie_exist(self,name):
        Obj = self.session.query(self.movie_model).filter(self.movie_model.name == name).first()
        if Obj:
            return False
        return True

    def set_photo_from_json(self,defult,index):
        photo=defult
        with open(self.config) as json_file:
            data = json.load(json_file)
            index_exist = index in data
            if index_exist:
                if len(data[index])>0:
                    photo=data[index]
        return  photo

    def set_photo(self,defult,serch):
        photo_avatar=''
        photo_dir = os.listdir(self.photo_dir)
        for photo in  photo_dir:
            if self.clear_name(photo) == serch:
                    photo_avatar=photo;
            if photo_avatar:
                photo_avatar=self.photo_dir + '' + str('/'+photo_avatar)
            else:
                photo_avatar=defult
            return photo_avatar;

    def set_none(self):
        return self.set_photo_from_json(none_movies_defult, 'none')

    def set_singles(self):
        return self.set_photo_from_json(singles_movies_defult,'singles')

    @abstractmethod
    def add_files(self):
        pass

class AddSeriesViaDir(AbstractAddViaDir):

    model=Series

    def __init__(self,dir):
        super().__init__(dir)
        self.name=self.set_name()
        self.series=self.if_series_exist(self.name)

    def set_movie_name_is_star_name(self,dir):
        stop = False
        for i in range(0, len(dir)):
            if dir[i] == "[" :
                stop = True
        return stop

    def set_sezons(self):
        sezons=1
        for dir in os.listdir(self.movie_dir):
            if os.path.isdir(dir):
                sezons=sezons+1
        return sezons;

    def create_sezons(self,sezons):
        object=[]
        for sezon in range(1,sezons+1):
            object.append(
                self.sezons_model(
                    name = sezon,
                    src  = self.set_photo(series_avatar_defult,str(sezon))
                )
            )
        self.session.add_all(object)
        self.session.commit()
        return object

    def set_dir_for_star(self,name):
        letter=name[0]
        dir=''
        if letter == 'A' or letter == 'B' or letter == 'C' or letter == 'D':
            dir=data_JSON[0]['dir'] + '/A-D/' + name
        if letter == 'E' or letter == 'F' or letter == 'G' or letter == 'H':
            dir=data_JSON[0]['dir'] + '/E-H/' + name
        if letter == 'M' or letter == 'N' or letter == 'O' or letter == 'P':
            dir=data_JSON[0]['dir'] + '/M-P/' + name
        if letter == 'R' or letter == 'S' or letter == 'T' or letter == 'U':
            dir=data_JSON[0]['dir']+'/R-U/'+name
        if letter == 'W' or letter == 'X' or letter == 'Y' or letter == 'Z':
            dir=data_JSON[0]['dir'] + '/W-Z/' + name
        if os.path.isdir(dir) is False:
            os.mkdir(dir)
            os.mkdir(dir+'/none')
            os.mkdir(dir+'/photo')
            sleep(1)
            f = open(dir+'/config.JSON', "x")
            f.close()
            my_file = open(dir+'/config.JSON', "w")
            my_file.write('{}')
            f.close()
        return self.dir


    def if_series_exist(self,name):
        sezons=self.create_sezons(self.set_sezons())
        return self.if_exist(name,self.model,self.model(
            name    =  name,
            number_of_sezons  =  self.set_sezons(),
            sezons  =  sezons,
            avatar  =  self.set_avatar(),
            dir     =  self.dir,
            config  =  self.config
        ))

    def if_star_exist(self,name):
        return self.if_exist(name,Stars,Stars(
            name   = name,
            avatar = stars_avatar_defult,
            none   = self.set_none(),
            singles= self.set_singles(),
            dir    = self.set_dir_for_star(name)
        ))

    def add_movie(self,movie,sezon,movie_name_is_star=False):
        name = self.clear_name(movie)
        src = movie
        stars = []
        stars_array = self.IfStar.faind_stars(movie)
        if stars_array is not None:
            for item in stars_array:
                star_obj = self.if_star_exist(item)
                star_obj.series.append(self.series)
                stars.append(star_obj)
        else:
            if movie_name_is_star:
                star_obj = self.if_star_exist(name)
                star_obj.series.append(self.series)
                stars.append(star_obj)
        series = [self.series]
        print('Movie '+str(name)+' has been added')
        return self.movie_model(
            name=name,
            src=src,
            stars=stars,
            series=series,
            sezon=sezon
        );

    def add_files(self):
        object = []
        movie_dir = os.listdir(self.movie_dir)
        for dir_element in movie_dir:
            nev_dir = self.movie_dir + '' + '/' + str(dir_element)
            if os.path.isdir(nev_dir):
                nev_dir_loop = os.listdir(nev_dir)
                stan=self.set_movie_name_is_star_name(dir_element)
                for movie in nev_dir_loop:
                    if self.if_movie_exist(self.clear_name(movie)):
                        object.append(self.add_movie(movie, dir_element,stan))
            else:
                if self.if_movie_exist(self.clear_name(dir_element)):
                    object.append(self.add_movie(dir_element, 1))
        self.session.add_all(object)
        self.session.commit()

class AddStarViaDir(AbstractAddViaDir):

    model=Stars
    movie_dir = '/none'

    def __init__(self,dir):
        super().__init__(dir)
        self.star=self.if_star_exist(self.set_name())

    def set_config(self):
        if Path(self.config).is_file() is False:
            f = open(self.config, "x")
            f.close()

    def if_star_exist(self,name):
        return self.if_exist(name, self.model, self.model(
            name=name,
            avatar = self.set_avatar(),
            dir=self.dir,
            none = self.set_none(),
            singles=self.set_singles(),
            config=self.config
        ))

    def add_files(self):
        movie_dir = os.listdir(self.movie_dir)
        object = []

        for movie in movie_dir:
            name = self.clear_name(movie)
            print(name)
            stars = self.IfStar.faind_stars(movie)
            new_stars = []
            if stars is not None:
                for star in stars:
                    new_stars.append(self.if_star_exist(star))
            new_stars.append(self.star)
            if self.if_movie_exist(self.clear_name(movie)):
                object.append(self.movie_model(
                    name=self.clear_name(movie),
                    stars=new_stars,
                    src=movie
                ))
                print('Movie ' + str(name) + ' has been added')
        self.session.add_all(object)
        self.session.commit()

class LoadPhotoFromDirs:

    session=session
    photo_model = Photos

    def clear_photo(self,object):
        if object is not None:
            for item in object.photos:
               self.session.delete(item)
               self.session.commit()

    def add_photos(self,dir,model):
        self.clear_photo(model)
        object=[]
        if os.path.isdir(dir):
            photo_dir_loop = os.listdir(dir)
            for photo in photo_dir_loop:
                src=dir + '' + str('/'+photo)
                object.append(self.photo_model(src=src))

        self.session.add_all(object)
        self.session.commit()

        for photo_item in object:
            model.photos.append(photo_item)

    def add_elment(self,Model):
        all = self.session.query(Model).all()

        for series_item in all:
            photo_dir = series_item.dir + '' + str('/photo')
            self.add_photos(photo_dir, series_item)

    def add_files(self):
        self.add_elment(Series)
        self.add_elment(Stars)

class AbstractLoopDir(ABC):

    LoopClass=None

    def __init__(self,dir):
        self.dir=dir

    def add_files(self):
        loop_dir = os.listdir(self.dir)
        for item in loop_dir:
            dir = self.dir + '' + str('/' + item)
            LC = self.LoopClass(dir)
            LC.add_files()

class AddStarViaDirLoop(AbstractLoopDir):

    LoopClass=AddStarViaDir

class AddSeriesViaDirLoop(AbstractLoopDir):

    LoopClass = AddSeriesViaDir

class LoadData(ABC):

    DirLoopClass=None

    def __init__(self,dir):
        self.dir=dir

    def load(self):
        dir = os.listdir(self.dir)
        for item in dir:
            new_dir = self.dir + '' + str('/' + item)
            if os.path.isdir(new_dir):
                LC = self.DirLoopClass(new_dir)
                LC.add_files()

class LoadSeriesFromJSON(LoadData):

    DirLoopClass = AddSeriesViaDirLoop

class LoadStarFromJSON(LoadData):

    DirLoopClass = AddStarViaDirLoop

class LoadFilesFromJson:

    objects={}

    def __init__(self,json_data):
        self.json_data=json_data
        self.object={
            "stars"  :  LoadStarFromJSON,
            "series" :  LoadSeriesFromJSON
        }

    def add_files(self):
        for item in self.json_data:
            LD=self.object[item['type']]
            LD=LD(item['dir'])
            LD.load()

#old Versions#

class abstratValid:

    def __init__(self,dir):
        self.dir=dir

    def valid(self):
        if re.search(self.validValue, self.dir):
            return True
        return False

    def onValidPass(self):
        pass

    def faindElment(self):
        if self.valid():
            return self.onValidPass()
        return  False

    def validate(self):
        return self.faindElment()

class faindSeries:

    str = ''

    def __init__(self,dir):
        self.dir=dir
        self.start = self.dir.find("[")
        self.end = self.dir.find("]")
        self.returnSeriesInString()

    def returnSeriesInString(self):
        for i in range(self.start+1,self.end):
            self.str=self.str+self.dir[i]

class ifHasSeries(abstratValid):

    validValue = "\[[a-zA-Z0-9\s]+\]\s[a-zA-Z0-9]+";

    def __init__(self,dir):
        super(ifHasSeries, self).__init__(dir)
        self.faindSeriesObj = faindSeries(dir)

    def onValidPass(self):
        self.faindSereis()
        return True

    def faindSereis(self):
        print(self.faindSeriesObj.str)

class faindStar:

    str = ''
    starArray=[]

    def __init__(self,dir):
        self.dir=dir
        self.start = self.dir.find("(")
        self.end = self.dir.find(")")
        self.createStarList()

    def returnStarsInString(self):
        for i in range(self.start+1,self.end):
            self.str=self.str+self.dir[i]

    def createStarList(self):
        self.returnStarsInString()
        self.starArray = self.str.split('and')
        return self.str

class ifStar(abstratValid):

    validValue = "[a-zA-Z0-9]+\s+\([a-zA-Z0-9\s]+\)";
    model = Stars
    movies = Movies
    objects_stars=[]
    objects_movies=[]
    session= session

    def __init__(self,dir,name,series=False):
        super(ifStar, self).__init__(dir)
        self.series=series
        self.faindStarObj = faindStar(dir)
        self.name=name

    def onValidPass(self):
        self.faindStar()
        return True

    def faindStar(self):
        for star in self.faindStarObj.starArray:
            self.objects_stars.append(
                self.model(
                    name=star,
                    avatar="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"
                )
            )

        self.session.add_all(self.objects_stars)
        self.session.commit()

        self.objects_movies=[
            self.movies(name=self.name)
        ]

        if self.series:
            self.series.movies.append(self.objects_movies[0])
        self.session.add_all(self.objects_movies)
        self.session.commit()

        self.add_stars_to_movie()

    def add_stars_to_movie(self):

        for movie in self.objects_movies:
            for star in self.objects_stars:
                movie.stars.append(star)

class AbstractManageDir(ABC):

    objects_stars=[]
    objects_movies=[]
    objects_series=[]
    session = session

    def set_name(self,name):

        str=''
        stop=False

        for i in range(0,len(name)):

            if name[i] == "." or name[i] == "(":
                stop=True

            if stop is False:
                str=str+name[i]

        return str

    def add_item_to_model(self,Model,array,data):
        array.append(
            Model(
                name=data[0],
                avatar=data[1]
            )
        )
        self.session.add_all(array)
        self.session.commit()

        return array[0]

class ManageDir(AbstractManageDir):

    def __init__(self,dir,base_view,series=False):
        self.series=series
        self.dir = dir
        self.base_view_model=base_view.model
        self.ifStar = ifStar(dir,self.clear_name(dir),series)

    def clear_name(self,dir):
        str=''
        stop=False
        for i in range(0,len(dir)):

            if dir[i] == "(":
                stop=True

            if dir[i] == ".":
                stop=False

            if stop is False:
                str=str+dir[i]

        return str

    def set(self):
        self.runValidate()

    def runValidate(self):
        starstan = self.ifStar.validate()

        if starstan is False:
            name =self.set_name(self.dir)
            self.objects_movies = [
                Movies(name=name)
            ]

            if self.series:
                self.series.movies.append(self.objects_movies[0])

            self.session.add_all(self.objects_movies)
            self.session.commit()

class MovieNormalLoopDir(AbstractManageDir):

    def __init__(self,filenames,obj):
        for files in filenames:
            dir = ManageDir(files, obj, False)
            dir.set()

class MoviesIsStarNameDir(AbstractManageDir):

    def __init__(self,movies):
        index=0
        for movie in movies:
            name=self.set_name(movie)
            self.objects_stars.append(
                Stars(
                    name=name,
                    avatar="C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"
                )
            )

            self.objects_movies.append(
                Movies(
                    name=name,
                    stars=[]
                )
            )

            self.objects_movies[index].stars.append(self.objects_stars[index])

            index=index+1

        self.session.add_all(self.objects_stars)
        self.session.commit()
        self.session.add_all(self.objects_movies)
        self.session.commit()

class AddMovieToStarDir(AbstractManageDir):

    def __init__(self,movies,star,base_view):

        add_star= self.add_item_to_model(
            Stars,
            self.objects_stars,
            [star,"C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"]
        )

        index=0
        for files in movies:
            name = self.set_name(files)
            self.objects_movies.append(
                Movies(
                    name=name,
                    stars=[]
                )
            )

            self.objects_movies[index].stars.append(add_star)
            index=index+1

        self.session.add_all(self.objects_movies)
        self.session.commit()

class AddMovieToSeriesDir(AbstractManageDir):

    def __init__(self, movies, series, base_view):

        addseries = self.add_item_to_model(
            Series,
            self.objects_series,
            [series,"C:/Users/DeadlyComputer/Desktop/photo/otjbibjaAbiifyN9uVaZyL-1200-80.jpg"]
        )

        for files in movies:
            dir = ManageDir(files, base_view,addseries)
            dir.set()














