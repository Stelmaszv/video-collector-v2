import json
import os
from core.custum_errors import Error

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

with open('data.json') as f:
  data = json.load(f)

data_JSON = data
ConfiGData(data_JSON)
window_type="half-smal" # half-smal, half-big
series_avatar_defult ='D:/project/video-collector-v2/data/avatar.png'
stars_avatar_defult  ='D:/project/video-collector-v2/data/no-avatar.png'
none_movies_defult   ='D:/project/video-collector-v2/data/none.png'
singles_movies_defult   ='D:/project/video-collector-v2/data/none.png'
movie_cover_defulut = 'D:/project/video-collector-v2/data/none.png'
search_in_defult= 'movies';
photo_ext= ('.png', '.jpg', '.jpeg','.jfif')
search_faze_defult = ''
#player
muted=False
auto_play=True
full_screen=True

