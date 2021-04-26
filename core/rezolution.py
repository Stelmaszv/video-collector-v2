from core.setings import screen_width,screen_height
class SetResolution:

    def __init__(self,AbstractBaseView):
        self.AbstractBaseView = AbstractBaseView
        self.menu_set=self.return_abstrat_view()

    def return_abstrat_view(self):
        return GetResolutionData(self.AbstractBaseView).show()

class Base:

    def __init__(self,GetResolutionData):
        self.width    = screen_width
        self.height   = screen_height
        self.GetResolutionData=GetResolutionData

    def base_menu(self):
        return {
            "left": self.GetResolutionData.set_rezulution(0, 'with'),
            "top": self.GetResolutionData.set_rezulution(2, 'height'),
            "width": self.GetResolutionData.set_rezulution(25, 'with'),
            "height": self.GetResolutionData.set_rezulution(100, 'height')
        }

    def base_navbar(self):
        return [
            self.GetResolutionData.set_rezulution(0, 'with'),
            self.GetResolutionData.set_rezulution(0, 'height'),
            self.GetResolutionData.set_rezulution(80, 'with'),
            self.GetResolutionData.set_rezulution(5, 'height')
        ]

    def base_window(self):
        return {
                "left":   self.GetResolutionData.set_rezulution(25, 'with'),
                "top":    self.GetResolutionData.set_rezulution(2, 'height'),
                "width":  self.GetResolutionData.set_rezulution(75, 'with'),
                "height": self.GetResolutionData.set_rezulution(100, 'height')
        }

class GetResolutionData:

    def __init__(self, AbstractBaseView):
        self.AbstractBaseView = AbstractBaseView
        self.Base=Base(self)

    def base_menu(self):
        return self.Base.base_menu()

    def base_navbar(self):
        return self.Base.base_navbar()

    def base_window(self):
        return self.Base.base_window()

    def set_rezulution(self, procent, var_type):
        if var_type == 'with':
            new_procent = int(procent * self.Base.width / 100)
        else:
            new_procent = int(procent * self.Base.height / 100)
        return new_procent

    def show(self):
        return {
            "Loading"        :{
                "position": {
                    "left": 2562 + 400,
                    "top": 400,
                    "width": 250,
                    "height": 250
                },
                "window": {
                    "title_size": [0, 0, 250, 250],
                }
            },
            "EditMovieGalery":{
                "position": {
                    "left": 2562 + 400,
                    "top": 400,
                    "width": 1280,
                    "height": 985
                },
                'dialog': {
                    "position": [2562 + 600, 600, 500, 100],
                    "label": [50, 10],
                    "acept": [50, 50],
                    "cancel": [250, 50]
                },
                "window": {
                    "navbar": [0, 10, 1280, 100],
                    "list_view_size": [200, 70, 700, 900],
                    "title_size": [300, -25, 580, 100],
                    "form_section": [150, 100, 1050, 300]
                }
             },
            "EditGalery":{
                 "position": {
                    "left": 2562 + 400,
                    "top": 400,
                    "width": 1280,
                    "height": 985
                },
                "window": {
                    #"navbar": [0, -10, 1280, 100],#
                    "list_view_size": [200, 40, 700, 900],
                    "title_size": [300, -25, 580, 100],
                    "form_section": [150, 100, 1050, 300]
                }
            },
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
                "position": self.base_window(),
                "window": {
                    "tags_name" : [
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(45, 'height'),
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(5, 'height')
                    ],
                    "tags"      : [
                        self.set_rezulution(15, 'with'),
                        self.set_rezulution(48, 'height'),
                        self.set_rezulution(15, 'with'),
                        self.set_rezulution(5, 'height')
                    ],
                    "tags_limit" :1000,
                    "star_name": [
                        self.set_rezulution(35, 'with'),
                        self.set_rezulution(45, 'height'),
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(5, 'height')
                    ],
                    "stars_limit": 1000,
                    "stars": [
                        self.set_rezulution(40, 'with'),
                        self.set_rezulution(48, 'height'),
                        self.set_rezulution(15, 'with'),
                        self.set_rezulution(5, 'height')
                    ],
                    "title_size": [
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(0, 'height'),
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(5, 'height')
                    ],
                    "form_section": [
                        self.set_rezulution(15, 'with'),
                        self.set_rezulution(7, 'height'),
                        self.set_rezulution(40, 'with'),
                        self.set_rezulution(40, 'height')
                    ],
                }
            },
            "Menu": {
                "position": self.base_menu(),
                "window": {
                    "title_size"       :   [
                        self.set_rezulution(0, 'with'),
                        self.set_rezulution(2, 'height'),
                        self.set_rezulution(21, 'with'),
                        self.set_rezulution(5, 'height')
                    ],
                    "form_section": [
                        self.set_rezulution(2, 'with'),
                        self.set_rezulution(7, 'height'),
                        self.set_rezulution(20, 'with'),
                        self.set_rezulution(10, 'height')
                    ],
                    "list_view_size"   :   [
                        self.set_rezulution(2, 'with'),
                        self.set_rezulution(20, 'height'),
                        self.set_rezulution(20, 'with'),
                        self.set_rezulution(65, 'height')
                    ],
                    "pagination_form"  :   [
                        self.set_rezulution(2, 'with'),
                        self.set_rezulution(85, 'height'),
                        self.set_rezulution(20, 'with'),
                        self.set_rezulution(10, 'height')
                    ]
                }
            },
            "add_tag": { #model_cryteria
                "position": self.base_window(),
                'dialog': {
                    "position" : [
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(10, 'height'),
                        self.set_rezulution(20, 'with'),
                        self.set_rezulution(5, 'height')],
                    "label"    : [self.set_rezulution(1, 'with'),self.set_rezulution(0, 'height')],
                    "acept"    : [self.set_rezulution(1, 'with'),self.set_rezulution(3, 'height')],
                    "cancel"   : [self.set_rezulution(10, 'with'),self.set_rezulution(3, 'height')],
                },
                "window": {
                    "title_size": [
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(0, 'height'),
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(5, 'height')
                    ],
                    "form_section": [
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(-15, 'height'),
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(40, 'height')
                    ],
                    "list_view_size": [
                        self.set_rezulution(15, 'with'),
                        self.set_rezulution(10, 'height'),
                        self.set_rezulution(50, 'with'),
                        self.set_rezulution(85, 'height')
                    ],
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
                "position":self.base_window(),
                "window":{
                    "stars_galery":[
                        self.set_rezulution(55, 'with'),
                        self.set_rezulution(6, 'height'),
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(10, 'height')
                    ],
                    "stars_galery_size": [
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(10, 'height'),
                    ],
                    "stars_row": 2,
                    "star_title": [
                        self.set_rezulution(50, 'with'),
                        self.set_rezulution(0, 'height'),
                        self.set_rezulution(20, 'with'),
                        self.set_rezulution(10, 'height')
                    ],
                    "description" :[
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(20, 'height'),
                        self.set_rezulution(20, 'with'),
                        self.set_rezulution(28, 'height')
                    ],
                    "description_limit": 500,
                    "avatar_size": [
                        self.set_rezulution(4, 'with'),
                        self.set_rezulution(8, 'height'),
                        self.set_rezulution(12, 'with'),
                        self.set_rezulution(28, 'height')
                    ],
                    "title_size": [
                        self.set_rezulution(-10, 'with'),
                        self.set_rezulution(0, 'height'),
                        self.set_rezulution(90, 'with'),
                        self.set_rezulution(10, 'height')
                    ],
                    "info_size": [
                        self.set_rezulution(30, 'with'),
                        self.set_rezulution(5, 'height'),
                        self.set_rezulution(12, 'with'),
                        self.set_rezulution(28, 'height')
                    ],
                    "navbar": self.base_navbar(),
                    "galery_size": [
                        self.set_rezulution(3, 'with'),
                        self.set_rezulution(40, 'height'),
                        self.set_rezulution(70, 'with'),
                        self.set_rezulution(50, 'height')
                    ],
                    "galery_photo_size": [
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(25, 'height'),
                    ],
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
