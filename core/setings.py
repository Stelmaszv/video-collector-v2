import json
import os
from core.custum_errors import Error

class ConfiGData:

  def __init__(self,json):
    for dir in json['dirs']:
      self.valid_drive(dir['dir'])

  def valid_drive(self,dir):
    name = dir.split('\\')
    dir_error = os.path.isdir(name[0])
    Error.throw_error_bool('Drive '+name[0]+' not exist please if is crypt ! ',dir_error)

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
search_faze_defult = ''
