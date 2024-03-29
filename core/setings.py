import json
import os
import sys
from abc import ABC, abstractmethod
from json import JSONDecodeError
from pathlib import Path

from PyQt5 import QtWidgets

from core.custum_errors import Error


class AbstractMode(ABC):
    def __init__(self, setings):
        self.setings = setings

    @abstractmethod
    def return_setings(self):
        pass

class ResetMode(AbstractMode):

    def return_setings(self):
        if os.path.isfile("DB.db"):
            os.remove("DB.db")

        return {
            "run_start_view": False,
            "scan_photos": False,
            "scan_dir": True,
            "config": True,
            "create_xml": True,
            "create_movie_list": True,
            "generate_json": True,
            "generate_html": True,
            "web_admin":False
        }

class OffAll(AbstractMode):

    def return_setings(self):
        return {
            "run_start_view": False,
            "scan_photos": False,
            "scan_dir": False,
            "config": False,
            "create_xml": False,
            "create_movie_list": False,
            "generate_json": False,
            "web_admin": False,
            "generate_html": False
        }


class HTML(AbstractMode):

    def return_setings(self):
        return {
            "run_start_view": False,
            "scan_photos": False,
            "scan_dir": False,
            "config": False,
            "create_xml": False,
            "create_movie_list": False,
            "generate_json": False,
            "web_admin": False,
            "generate_html": True
        }

class Add(AbstractMode):

    def return_setings(self):
        if os.path.isfile("DB.db"):
            os.remove("DB.db")
        return {
            "run_start_view": False,
            "scan_photos": True,
            "scan_dir": False,
            "config": False,
            "create_xml": False,
            "create_movie_list": False,
            "generate_json": True,
            "web_admin": False,
            "generate_html": True
        }

class All(AbstractMode):

    def return_setings(self):
        if os.path.isfile("DB.db"):
            os.remove("DB.db")
        return {
            "run_start_view": True,
            "scan_photos": True,
            "scan_dir": True,
            "config": True,
            "create_xml": True,
            "create_movie_list": True,
            "generate_json": True,
            "web_admin": False,
            "generate_html": True
        }

class AllNoPhoto(AbstractMode):

    def return_setings(self):
        if os.path.isfile("DB.db"):
            os.remove("DB.db")
        return {
            "run_start_view": False,
            "scan_photos": False,
            "scan_dir": True,
            "config": True,
            "create_xml": True,
            "create_movie_list": True,
            "generate_json": True,
            "web_admin": True,
            "generate_html": True
        }

class Screenshot(AbstractMode):

    def return_setings(self):
        if os.path.isfile("DB.db"):
            os.remove("DB.db")
        return {
            "run_start_view": False,
            "scan_photos": True,
            "scan_dir": True,
            "config": True,
            "create_xml": False,
            "create_movie_list": False,
            "generate_json": False,
            "web_admin": False,
            "generate_html": False
        }

class HTMLJSOM(AbstractMode):
    def return_setings(self):
        return {
            "run_start_view": False,
            "scan_photos": False,
            "scan_dir": False,
            "config": False,
            "create_xml": False,
            "create_movie_list": False,
            "generate_json": True,
            "web_admin": False,
            "generate_html": True
        }

class Run(AbstractMode):
    def return_setings(self):
        return {
            "run_start_view": True,
            "scan_photos": False,
            "scan_dir": False,
            "config": False,
            "create_xml": False,
            "create_movie_list": False,
            "generate_json": False,
            "web_admin": False,
            "generate_html": False
        }

class SetMode:

    def __init__(self, setings_array, mode):
        self.setings = setings_array
        self.set_mode(mode)

    def set_mode(self, mode):
        modes = ["reset", "Off all", "HTML", "add", 'all', "screenshot", "HTML&JSOM", "Run","AllNoPhoto"]
        error = mode in modes
        mes = 'Invalid ' + mode + ' Mode available "normal","reset","Off all","HTML&JSOM", "add" ,"all","screenshot",Run''AllNoPhoto'
        Error.throw_error_bool(mes, error)
        setings_array = {
            "reset": ResetMode(self.setings),
            "Off all": OffAll(self.setings),
            "HTML": HTML(self.setings),
            "add": Add(self.setings),
            "all": All(self.setings),
            "screenshot": Screenshot(self.setings),
            "HTML&JSOM": HTMLJSOM(self.setings),
            "Run": Run(self.setings),
            "AllNoPhoto":AllNoPhoto(self.setings)
        }
        self.Mode = setings_array[mode]

    def return_setings(self):
        return self.Mode.return_setings()

class GetRezolution:

  def __init__(self):
    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    self.size = screen.size()

  @property
  def set_width(self):
    return self.size.width()

  @property
  def set_height(self):
    return self.size.height()

class ConfiGData:

  def __init__(self,json):
    for dir in json['dirs']:
      self.valid_drive(dir['dir'])
      self.make_dirs(dir['dir'])
    Error.throw_error_bool(Error.get_error(1), "html_output" in json)
    Error.throw_error_bool(Error.get_error(1), "movies_photos" in json)
    if os.path.isdir(json["movies_photos"]) is False:
        os.mkdir(json["movies_photos"])
  def valid_drive(self,dir):
    name = dir.split('\\')
    dir_error = os.path.isdir(name[0])
    Error.throw_error_bool(Error.add_data_to_error(Error.get_error(2),'{{data}}',name[0]), dir_error)

  def make_dirs(self,dir):
    if os.path.isdir(dir) is False:
      name = dir.split('\\')
      dir=name[0]
      for el in range(1,len(name)):
          dir = dir + '\\' + name[el]
          if os.path.isdir(dir) is False:
            os.mkdir(dir)

    if os.path.isdir(dir+'\\A-D') is False:
      os.mkdir(dir+'\\A-D')

    if os.path.isdir(dir+'\\E-H') is False:
      os.mkdir(dir+'\\E-H')

    if os.path.isdir(dir+'\\I-L') is False:
      os.mkdir(dir+'\\I-L')

    if os.path.isdir(dir+'\\M-P') is False:
      os.mkdir(dir+'\\M-P')

    if os.path.isdir(dir+'\\R-U') is False:
      os.mkdir(dir+'\\R-U')

    if os.path.isdir(dir+'\\W-Z') is False:
      os.mkdir(dir+'\\W-Z')

GR=GetRezolution()
#Screen
screen_width=GR.set_width
screen_height=GR.set_height
data_JSON={}
if Path('data.json').is_file():
  try:
      with open('data.json') as f:
        data = json.load(f)
        data_JSON = data
        ConfiGData(data_JSON)
  except JSONDecodeError:
      print(Error.get_error(1))
      exit()

#form button
with_size_defult = 25
height_size_defult = 25
#custum_json_galery
movies    = ["cover.jpg", "poster.jpg"]
series    = ["banner.jpg","avatar.jpg"]
producent = ["banner.jpg","avatar.jpg"]
star      = ["avatar.jpg"]
#menu
menu_per_page = 20
series_avatar_defult =''
stars_avatar_defult  =''
none_movies_defult   =''
singles_movies_defult   =''
movie_cover_defulut = ''
search_in_defult= 'movies';
start_page=0
photo_ext = ('.png', '.jpg', '.jpeg', '.jfif', ".JPG")
movie_ext= ('.avi','.mkv','.mp4','.wmv')
search_faze_defult = ''
#player
muted=False
auto_play=True
full_screen=True
# MODE available "normal","reset","Off all","HTML&JSOM", "add","all","screenshot","HTML","Run" ,"AllNoPhoto"
MODE = 'AllNoPhoto'
#run MODERUN "console","config"
MODERUN ="console"
# run_setings only when mode set to "normal"
setings_array = {
    "run_start_view": True,
    "scan_photos": False,
    "scan_dir": True,
    "config": True,
    "create_xml": False,
    "create_movie_list": False,
    "generate_json": False,
    "web_admin": False,
    "generate_html": False
}
if MODE != "normal":
    SetMode = SetMode(setings_array, MODE)
    setings_array = SetMode.return_setings()

#AdvanceSearchCriteria
tags_defult                       = ('')
stars_defult                      = ('')
show_limit                        = 10
order_by_defult                   = ''
favourite_defult                  = False
year_defult                       = None
max_defult                        = ['views',0]
min_defult                        = ['views',0]
series_defult                     = ('')
#list
show_list_defult = 'normal'
