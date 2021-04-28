import json
import os
import sys
from core.custum_errors import Error
from pathlib import Path
from PyQt5 import QtWidgets

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

  def valid_drive(self,dir):
    name = dir.split('\\')
    dir_error = os.path.isdir(name[0])
    Error.throw_error_bool('Drive '+name[0]+' not exist please if is crypt ! ',dir_error)

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
  with open('data.json') as f:
    data = json.load(f)
  data_JSON = data
  ConfiGData(data_JSON)

#form button
with_size_defult = 25
height_size_defult = 25
#menu
menu_per_page = 50

series_avatar_defult ='D:/project/video-collector-v2/data/avatar.png'
stars_avatar_defult  ='D:/project/video-collector-v2/data/no-avatar.png'
none_movies_defult   ='D:/project/video-collector-v2/data/none.png'
singles_movies_defult   ='D:/project/video-collector-v2/data/none.png'
movie_cover_defulut = 'D:/project/video-collector-v2/data/none.png'
search_in_defult= 'series';
start_page=0
photo_ext= ('.png', '.jpg', '.jpeg','.jfif')
search_faze_defult = ''
#player
muted=False
auto_play=True
full_screen=True
#run_setings
scan_photos=False
run_start_view=True
clean_db=False
#AdvanceSearchCriteria
tags_defult                       = ('')
stars_defult                      = ('')
show_limit                        = 10
order_by_defult                   = ''
favourite_defult                  = None
year_defult                       = None
max_defult                        = ['views',0]
min_defult                        = ['views',0]
series_defult                     = ''
#list
show_list_defult                  = 'full'
