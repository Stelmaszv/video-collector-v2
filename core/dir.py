import re
import json
import os
import random
from app.db.models import Stars,Movies,Series,Photos,Sezons,Tags,Producent
from app.db.models import session
from abc import ABC,abstractmethod
from core.custum_errors import Error
from core.setings import series_avatar_defult,stars_avatar_defult,none_movies_defult,singles_movies_defult
from pathlib import Path
from core.setings import data_JSON,photo_ext,movie_ext
from moviepy.editor import VideoFileClip
from core.strings import stringManipupations
from core.setings import series,producent,star

add: bool = False

def set_dir_for_producent(name: object) -> object:
    letter_of_movie = name[0]
    Error.throw_error_bool("First letter of star can not be 'space' (" + str(name) + ") !!", letter_of_movie != " ")
    letter = letter_of_movie.upper()
    dir = ''
    if letter == 'A' or letter == 'B' or letter == 'C' or letter == 'D':
        dir = data_JSON['dirs'][2]['dir'] + '\\A-D\\' + name
    if letter == 'E' or letter == 'F' or letter == 'G' or letter == 'H':
        dir = data_JSON['dirs'][2]['dir'] + '\\E-H\\' + name
    if letter == 'I' or letter == 'J' or letter == 'K' or letter == 'L':
        dir = data_JSON['dirs'][2]['dir'] + '\\I-L\\' + name
    if letter == 'M' or letter == 'N' or letter == 'O' or letter == 'P' or letter =='Q':
        dir = data_JSON['dirs'][2]['dir'] + '\\M-P\\' + name
    if letter == 'R' or letter == 'S' or letter == 'T' or letter == 'U':
        dir = data_JSON['dirs'][2]['dir'] + '\\R-U\\' + name
    if letter == 'W' or letter == 'V' or letter == 'X' or letter == 'Y' or letter == 'Z':
        dir = data_JSON['dirs'][2]['dir'] + '\\W-Z\\' + name
    return dir

def set_dir_for_star(name: object) -> object:
    letter_of_movie = name[0]
    Error.throw_error_bool("First letter of star can not be 'space' (" + str(name) + ") !!", letter_of_movie != " ")
    letter = letter_of_movie.upper()
    dir = ''
    if letter == 'A' or letter == 'B' or letter == 'C' or letter == 'D':
        dir = data_JSON['dirs'][0]['dir'] + '\\A-D\\' + name
    if letter == 'E' or letter == 'F' or letter == 'G' or letter == 'H':
        dir = data_JSON['dirs'][0]['dir'] + '\\E-H\\' + name
    if letter == 'I' or letter == 'J' or letter == 'K' or letter == 'L':
        dir = data_JSON['dirs'][0]['dir'] + '\\I-L\\' + name
    if letter == 'M' or letter == 'N' or letter == 'O' or letter == 'P' or letter =='Q':
        dir = data_JSON['dirs'][0]['dir'] + '\\M-P\\' + name
    if letter == 'R' or letter == 'S' or letter == 'T' or letter == 'U':
        dir = data_JSON['dirs'][0]['dir'] + '\\R-U\\' + name
    if letter == 'W' or letter == 'V' or letter == 'X' or letter == 'Y' or letter == 'Z':
        dir = data_JSON['dirs'][0]['dir'] + '\\W-Z\\' + name
    return dir

def if_star_exist(self,name):
    return self.if_exist(name, self.model, self.model(
        name=name,
        avatar=stars_avatar_defult,
        none=self.set_none(),
        singles=self.set_singles(),
        dir=self.set_dir_for_star(name)
    ))

def if_producent_exist(self,name):
    return self.if_exist(name, self.model, self.model(
        name=name,
        avatar=stars_avatar_defult,
        dir=self.set_dir_for_star(name)
    ))

def set_name(dir):
    name = dir.split('\\')
    last = len(name)-1
    return name[last]

class PhotoMeaker:

    dir=''
    limit = 12
    procent_limt=96
    add=False

    def __init__(self,Movie,data,AbstractBaseView=None):
        self.Movie=Movie
        self.data=data
        self.set_limit()
        self.AbstractBaseView=AbstractBaseView

    def set_limit(self):
        count=0

        for item in os.listdir(self.Movie.dir):
            if item.endswith(photo_ext):
                count=count+1

        with open(self.Movie.dir+'\\skip_galery.JSON') as sg:
            json_pars = json.load(sg)
            in_skip_galeruy=len(json_pars)

        count=count-in_skip_galeruy
        if count<self.limit:
            self.limit=self.limit-count;
            self.add=True

    def set_round_number(self,clip):
        duration=int(clip.duration)
        round_nomber = random.randint(0, int(clip.duration))
        procent=int(round_nomber/duration*100)
        if procent<=self.procent_limt:
            return round_nomber
        else:
            return self.set_round_number(clip)

    def replace(self,photo):
        os.remove(self.Movie.dir+'\\'+photo)
        self.make()

    def make(self):
        if self.add:
            star_mes="Dir "+self.Movie.src+" is scaning !"
            if self.AbstractBaseView:
                self.AbstractBaseView.setWindowTitle(star_mes)
                self.AbstractBaseView.update()
            else:
                print(star_mes)

            clip = VideoFileClip(self.Movie.src)
            for frame in range(0, self.limit):
                clip.save_frame(self.Movie.dir + '\\' + str(stringManipupations.random(20)) + '.png', t=self.set_round_number(clip))
                mess='creating photos for ' + self.Movie.name + ' ' + str(frame + 1) + '/' + str(self.limit)
                if self.AbstractBaseView:
                    self.AbstractBaseView.setWindowTitle(mess)
                    self.AbstractBaseView.update()
                else:
                    print(mess)

class PhotoMeakerViaView(PhotoMeaker):

    def __init__(self,Movie,data,array):
        super().__init__(Movie,data)
        self.array=array

    def make(self):
        if VideoFileClip(self.Movie.src):
            star_mes = "Dir " + self.Movie.src + " is scaning !"
            self.array.append(star_mes)

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
        self.starArray = str.split(' and ')
        return self.starArray

class IfStar:

    validValue = "[a-zA-Z0-9]+\s+\([a-zA-Z0-9\s]+\)";

    def faind_stars(self,file):
        FS = FaindStar(file)
        if re.search(self.validValue, file):
            string=FS.return_stars_in_string()
            return FS.create_star_list()
        return None

class AbstractAddViaDir(ABC):

    movie_model=Movies
    photo_model=Photos
    sezons_model=Sezons
    movie_dir = '\\movies'
    photo_dir = '\\photo'
    star=None
    name=''
    series=None
    shema_url=''
    defult_skip_galery=''

    def __init__(self, dir,Viev=None):
        self.dir = dir
        self.config = self.dir + '\\config.JSON'
        self.skip_galery = self.dir + '\\skip_galery.JSON'
        self.set_config()
        self.session = session
        self.IfStar = IfStar()
        self.set_movie_dir()
        self.set_photo_dir()
        self.Viev = Viev

    def set_dir(self,seazon=''):
        dir= self.movie_dir
        if seazon:
            dir = self.movie_dir+'\\'+str(seazon)
        return dir

    def set_config(self):

        if Path(self.config).is_file() is False:
            f = open(self.config, "x")
            f.write(Path(self.shema_url).read_text())
            f.close()

        if Path(self.skip_galery).is_file() is False:
            f = open(self.skip_galery, "x")
            f.write(json.dumps(self.defult_skip_galery))
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

        if str[len(str)-1]==' ':
            nstr=''
            for i in range(0, len(str)-1):
                if i < len(str)-1:
                    nstr=nstr+str[i]
            return nstr
        return str

    def set_movie_dir(self):
        self.movie_dir=self.dir + '' + str(self.movie_dir)
        if os.path.isdir(self.movie_dir) is False:
            os.mkdir(self.movie_dir)

    def set_photo_dir(self):
        self.photo_dir = self.dir + '' + str(self.photo_dir)
        if os.path.isdir(self.photo_dir) is False:
            os.mkdir(self.photo_dir)
            os.mkdir(self.photo_dir+'//DATA')

    def set_avatar(self):
        return  self.set_photo_from_json(series_avatar_defult,'avatar')

    def if_exist(self,name,Model,add):
        Obj=self.session.query(Model).filter(Model.name == name).first()
        if Obj is not None:
            self.star = Obj
        if Obj is None:
            self.session.add_all([
                add
            ])
            self.session.commit()
            print(name+' Has been added')
            if self.Viev is not None:
                self.Viev.data_array.append(str(self.Viev.info_data_index)+'/'+str(self.Viev.info_data_array)+' '+name+' Has been added')
                self.Viev.setWindowTitle(str(self.Viev.info_data_index)+'/'+str(self.Viev.info_data_array)+' '+name+' Has been added')
                self.Viev.info_data_index=self.Viev.info_data_index+1
                self.Viev.update()
            Obj = self.session.query(Model).filter(Model.name == name).first()
        return Obj

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

    def set_dir_for_star(self,name):
        dir=set_dir_for_star(name)
        if os.path.isdir(dir) is False:
            os.mkdir(dir)
            os.mkdir(dir+'\\none')
            os.mkdir(dir+'\\photo')
            f = open(dir+'\\config.JSON', "x")
            f.write("{}")
            f.close()
        if os.path.isdir(dir + '\\photo\DATA') is False:
            os.mkdir(dir + '\\photo\DATA')
        return self.dir

    def set_none(self):
        return self.set_photo_from_json(none_movies_defult, 'none')

    def set_singles(self):
        return self.set_photo_from_json(singles_movies_defult,'singles')

    @abstractmethod
    def add_files(self):
        pass

class AddSeriesViaDir(AbstractAddViaDir):

    model=Series
    name =''
    shema_url ="custum_json/series.JSON"
    defult_skip_galery = series

    def __init__(self,dir,View=None):
        super().__init__(dir,View)
        self.config = self.dir + '\\config.JSON'
        self.skip_galery = self.dir + '\\skip_galery.JSON'
        self.name=set_name(dir)
        print("Scaning Series " + str(self.name))
        item=session.query(self.model).filter(self.model.name == self.name).first()
        if item is None:
            self.series=self.if_series_exist(self.name)
        else:
            self.series=item

    def set_movie_name_is_star_name(self,dir):
        stop = False
        for i in range(0, len(dir)):
            if dir[i] == "[" :
                stop = True
        return stop

    def set_sezons(self):
        sezons=0
        for dir in os.listdir(self.movie_dir):
            if os.path.isdir(self.movie_dir+'\\'+dir):
                sezons=sezons+1
        if sezons==0:
            sezons=1
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

    def if_series_exist(self,name):
        sezons=self.create_sezons(self.set_sezons())
        return self.if_exist(name,self.model,self.model(
            name    =  name,
            show_name=name,
            number_of_sezons  =  self.set_sezons(),
            sezons  =  sezons,
            avatar  =  self.set_avatar(),
            dir     =  self.dir,
            config  =  self.config
        ))

    def set_sort_name(self,name,series):
        try:
            int(name)
            if isinstance(int(name), int):
                return series+' '+name
        except ValueError:
            return name;

    def if_star_exist(self,name):
        return self.if_exist(name,Stars,Stars(
            name      = name,
            show_name = name,
            avatar = stars_avatar_defult,
            none   = self.set_none(),
            singles= self.set_singles(),
            dir    = self.set_dir_for_star(name)
        ))

    def add_movie(self, movie, sezon, if_star):
        name = self.clear_name(movie)
        src = movie
        stars = []
        stars_array = self.IfStar.faind_stars(movie)
        if stars_array is not None:
            for item in stars_array:
                star_obj = self.if_star_exist(set_name(item))
                star_obj.series.append(self.series)
                stars.append(star_obj)
        if len(stars) == 0 and if_star:
            star_obj = self.if_star_exist(name)
            star_obj.series.append(self.series)
            stars.append(star_obj)
        series = [self.series]
        print('Movie '+str(name)+' has been added')
        if self.Viev is not None:
            self.Viev.setWindowTitle(str(self.Viev.info_data_index)+' '+name+' Has been added')
            self.Viev.scrol.addItem(str(self.Viev.info_data_index)+' '+name+' Has been added')
            self.Viev.scrol.update()
            self.Viev.info_data_index = self.Viev.info_data_index + 1
            self.Viev.update()
        show_name=self.set_sort_name(name,series[0].name)
        model=self.movie_model(
            name=name,
            show_name=show_name,
            search_name=series[0].name+' '+name,
            src=self.movie_dir + '\\' + sezon + '\\DATA\\' + src,
            stars=stars,
            series=series,
            sezon=sezon
        );
        return model

    def if_movie_exist(self,name,seazon):
        Obj = self.session.query(self.movie_model).filter(self.movie_model.search_name == name).first()
        if Obj:
            stan=True
            for item in Obj.series:
                if item.id == self.series.id:
                    stan=False
            return stan
        return True

    def if_movie_is_star_name(self, dir):
        if dir.find("[STAR]") > 0:
            return True
        return False

    def add_files(self):
        object = []
        movie_dir = os.listdir(self.movie_dir)
        for dir_element in movie_dir:
            nev_dir = self.movie_dir + '' + '\\' + str(dir_element) + '\\DATA'
            nev_dir_loop = []
            if os.path.isdir(nev_dir):
                nev_dir_loop = os.listdir(nev_dir)
            for movie in nev_dir_loop:
                if movie.endswith(movie_ext):
                    if_star = self.if_movie_is_star_name(dir_element)
                    if self.if_movie_exist(self.series.name+' '+self.clear_name(movie),dir_element):
                        object.append(self.add_movie(movie, dir_element, if_star))

class AddStarViaDir(AbstractAddViaDir):

    model=Stars
    movie_dir = '\\none'
    shema_url = "custum_json/stars.json"
    defult_skip_galery = star

    def __init__(self,dir,View=False):
        super().__init__(dir,View)
        self.star=self.if_star_exist(set_name(dir))

    def if_movie_exist(self,name,seazon):
        Obj = self.session.query(self.movie_model).filter(self.movie_model.name == name).first()
        if Obj:
            if self.star in Obj.stars:
                return True
        return True

    def if_star_exist(self,name):
        name=set_name(name)

        return self.if_exist(name, self.model, self.model(
            name=name,
            show_name=name,
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
            stars = self.IfStar.faind_stars(movie)
            new_stars = []
            if stars is not None:
                for star in stars:
                    new_stars.append(self.if_star_exist(star))
            new_stars.append(self.star)
            if self.if_movie_exist(self.clear_name(movie),1):
                name=self.clear_name(movie)
                name_new=name+' - '+self.star.name
                src = self.movie_dir + '\\' + movie
                movie= self.movie_model(
                    name=name_new,
                    show_name=name,
                    stars=new_stars,
                )
                movie.src=src
                object.append(movie)
                print('Movie ' + str(name) + ' has been added')

        self.session.add_all(object)
        self.session.commit()

class AddProducentViaDir(AbstractAddViaDir):

    model=Producent
    movie_dir = '\\movies'
    shema_url = "custum_json\\producent.json"
    defult_skip_galery = producent

    def __init__(self,dir,View=None):
        super().__init__(dir,View)
        self.star=self.if_producent_exist(set_name(dir))

    def if_producent_exist(self,name):
        name=set_name(name)
        return self.if_exist(name, self.model, self.model(
            name=name,
            show_name=name,
            avatar = self.set_avatar(),
            dir=self.dir
        ))

    def add_files(self):
        pass

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

    def __init__(self,dir,Viev=None):
        self.dir=dir
        self.Viev = Viev

    def add_files(self):
        loop_dir = os.listdir(self.dir+'\\')
        for item in loop_dir:
            dir = self.dir + '' + str('\\' + item)
            LC = self.LoopClass(dir,self.Viev)
            LC.add_files()

class AddStarViaDirLoop(AbstractLoopDir):

    LoopClass=AddStarViaDir

class AddSeriesViaDirLoop(AbstractLoopDir):

    LoopClass = AddSeriesViaDir

class AddProducentViaDirLoop(AbstractLoopDir):

    LoopClass = AddProducentViaDir

class LoadData(ABC):

    DirLoopClass=None

    def __init__(self,dir,Viev=None):
        self.dir=dir
        self.Viev = Viev

    def load(self):
        dir = os.listdir(self.dir)
        for item in dir:
            new_dir = self.dir + '' + str('\\' + item)
            if os.path.isdir(new_dir):
                LC = self.DirLoopClass(new_dir,self.Viev)
                LC.add_files()

class LoadSeriesFromJSON(LoadData):

    DirLoopClass = AddSeriesViaDirLoop

class LoadStarFromJSON(LoadData):

    DirLoopClass = AddStarViaDirLoop

class LoadProducentsFromJSON(LoadData):

    DirLoopClass = AddProducentViaDirLoop

class LoadFilesFromJson:

    objects={}

    def __init__(self,json_data,Viev=None):
        self.json_data=json_data
        self.Viev=Viev
        self.object={
            "series"     :  LoadSeriesFromJSON,
            "producents": LoadProducentsFromJSON,
            "stars": LoadStarFromJSON
        }

    def add_files(self):
        for item in self.json_data:
            LD=self.object[item['type']]
            LD=LD(item['dir'],self.Viev)
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














