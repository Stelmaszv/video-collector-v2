from abc import ABC,abstractmethod
from core.setings import window_type

class SetResolution:
    windows_type=window_type

    def __init__(self):
        self.menu_set=self.set_menu_type()

    def set_menu_type(self):
        switcher = {
            'half-smal': MenuHalfSmall(),
            'half-big': MenuHalfbig()
        }
        obj=switcher.get(self.windows_type, "Invalid data");
        return obj.show()

class MenuType(ABC):

    @abstractmethod
    def show(self):
        pass

class MenuHalfbig(MenuType):

    def show(self):
        return {
            "Menu": {
                "position":{
                    "left"            : -2,
                    "top"             : 25,
                    "width"           : 400,
                    "height"          : 1400
                }
            },

            "EditStars":{
                "position": {
                    "left": 400,
                    "top": 25,
                    "width": 2155,
                    "height": 1400
                },
            },

            "Stars": {
                "position": {
                    "left"              : 400,
                    "top"               : 25,
                    "width"             : 2155,
                    "height"            : 1400
                },
                "window": {
                    "avatar_size"       : [150, 80, 300, 300],
                    "title_size"        : [700, 0, 300, 100],
                    "info_size"         : [700, 50, 800, 400],
                    "galery_size"       : [1250, 70, 700, 361],
                    "list_view_size"    : [150, 430, 1800, 920],
                    "galery_photo_size" : [250, 250],
                    "description": [330, 150, 450, 200],
                    'galery_item_show'  : 3,
                    "section": {
                        "left"          : 50,
                        "left_add"      : 220,
                        "top"           : 0,
                        "top_add"       : 250,
                        "per_row"       : 8,
                        "per_page"      : 32
                    }
                }
            }
        }

class MenuHalfSmall(MenuType):

    def show(self):
        return {
            "SetPhotoToSeries": {
                "position": {
                    "left": 2562 + 400,
                    "top": 400,
                    "width": 1280,
                    "height": 985
                },
                "window": {
                    "title_size": [0, 0, 1280, 50],
                    "form_section": [150, 100, 1050, 300]
                }
            },
            "EditSeries":{
                "position": {
                    "left": 2562 + 400,
                    "top": 400,
                    "width": 1280,
                    "height": 985
                },
                "window":{
                    "title_size": [0, 0, 1280, 50],
                    "form_section": [300, 100, 680, 300]
                }
            },
            "Series":{
                "position": {
                    "left": 2562 + 400,
                    "top": 400,
                    "width": 1280,
                    "height": 985
                },
                "window":{
                    "description": [30,675, 325, 200],
                    "description_limit": 500,
                    "navbar": [450, -180, 480, 480],
                    "title_size": [0, 0, 1280,50],
                    "list_view_size": [375,75,871,881],
                    "avatar_size": [50, 50, 250, 250],
                    "info_size": [100,300,300,200],
                    "galery_size": [30, 525, 300, 200],
                    "galery_photo_size": [125, 125],
                    "galery_item_show": 2,
                    "section_scroller":[300, 10, 540,830],
                    "section_avatar": [20, 50, 250, 250],
                    "section_avatar_single_movie" :[120, 100, 250, 300],
                    "section_info"  : [70, 300, 300, 200],
                    "section_info_single_info"  : [500, 100, 300, 200],
                    "single_title"  : [-200, -50, 1280, 200],
                    "single_play_button":[150,420,250,50],
                    "single_info_button":[450,420,250,50]
                }
            },
            "MovieListView": {
                "position": {
                    "left"    : 2562+400,
                    "top"     : 400,
                    "width"   : 1280,
                    "height"  : 985
                },
                "window":{
                    "info_size"       : [0,10,10,10],
                    "title_size"      : [0, 0, 1280, 100],
                    "list_view_size"  : [450,80,671,881],
                    "avatar_size"     : [100, 250, 250, 350],
                    "button_series"   : [100,600,250,50],
                    "button_star"     : [100,650,250,50]

                }
            },
            "advande_search":{
                "position": {
                    "left": 2562 + 400,
                    "top": 400,
                    "width": 1280,
                    "height": 985
                },
                "window": {
                    "tags_name" : [400,200,480,50],
                    "tags"      : [400, 250, 480, 500],
                    "star_name": [400, 300, 480, 50],
                    "stars": [400, 350, 480, 50],
                    "title_size": [0, 0, 1280, 100],
                    "form_section": [400, 100, 480, 250],
                }
            },
            "Menu": {
                "position": {
                    "left"             : 2562,
                    "top"              : 400,
                    "width"            : 400,
                    "height"           : 985
                },
                "window": {
                    "title_size": [0, 0, 400, 50],
                    "list_view_size": [0, 300, 380, 250],
                    "form_section" :   [50,40,300,150]
                }
            },
            "add_tag": {
                "position": {
                    "left": 2562+400,
                    "top": 400,
                    "width": 1280,
                    "height": 985
                },
                'dialog': {
                    "position" : [2562+600,600,500,100],
                    "label"    : [50,10],
                    "acept"    : [50,50],
                    "cancel"   : [250, 50]
                },
                "window": {
                    "dialog"        : [77,0,100,100],
                    "title_size"    : [0, 0 ,1280 ,100],
                    "form_section"  : [400, 0 ,480 ,250],
                    "list_view_size": [300, 150, 680, 250],
                }
            },
            "EditStars": {
                "position": {
                    "left": 2562 + 400,
                    "top": 400,
                    "width": 1280,
                    "height": 985
                },
                "window": {
                    "title_size": [0, 0, 1280, 100],
                    "form_section": [300, 100, 680, 600]
                }
            },
            "Movie": {
                "position":{
                    "left": 2562 + 400,
                    "top": 400,
                    "width": 1280,
                    "height": 985
                },
                "window":{
                    "description" :[450,350, 400, 200],
                    "description_limit": 500,
                    "tags": [600, 200, 375, 220],
                    "tags_limit":1000,
                    "avatar_size": [50, 100, 250, 300],
                    "title_size": [300, 35, 580, 100],
                    "info_size": [400, 100, 375, 350],
                    "navbar": [0, -10, 1280, 100],
                    "galery_size": [0, 500, 1280, 361],
                    "galery_photo_size": [200, 200],
                    "galery_item_show": 5,
                }
            },
            "Stars": {
                "position":  {
                    "left"              : 2562+400,
                    "top"               : 400,
                    "width"             : 1280,
                    "height"            : 985
                },
                "window":{
                    "navbar"            : [0,-220,1280,480],
                    "avatar_size"       : [50, 80, 250, 300],
                    "title_size"        : [350, 0, 300, 100],
                    "info_size"         : [330, 80, 375, 220],
                    "galery_size"       : [700, 50, 500, 361],
                    "list_view_size"    : [50, 390, 1200, 550],
                    "galery_photo_size" : [150, 150],
                    "galery_item_show"  : 2,
                    "description"       : [325,200,375,270],
                    "description_limit" : 500,
                    "section": {
                        "left"         : 15,
                        "left_add"     : 250,
                        "top"          : 0,
                        "top_add"      : 250,
                        "per_row"      : 6,
                        "per_page"     : 12
                    }
                }

            }
        }
