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

    def dialog(self):
        return {
            "position": [
                self.GetResolutionData.set_rezulution(25, 'with'),
                self.GetResolutionData.set_rezulution(10, 'height'),
                self.GetResolutionData.set_rezulution(20, 'with'),
                self.GetResolutionData.set_rezulution(5, 'height')],
            "label": [self.GetResolutionData.set_rezulution(1, 'with'), self.GetResolutionData.set_rezulution(0, 'height')],
            "acept": [self.GetResolutionData.set_rezulution(1, 'with'), self.GetResolutionData.set_rezulution(3, 'height')],
            "cancel": [self.GetResolutionData.set_rezulution(10, 'with'), self.GetResolutionData.set_rezulution(3, 'height')],
        }

    def menu(self):
        return {
            "left": self.GetResolutionData.set_rezulution(0, 'with'),
            "top": self.GetResolutionData.set_rezulution(2, 'height'),
            "width": self.GetResolutionData.set_rezulution(25, 'with'),
            "height": self.GetResolutionData.set_rezulution(100, 'height')
        }

    def navbar(self):
        return [
            self.GetResolutionData.set_rezulution(0, 'with'),
            self.GetResolutionData.set_rezulution(0, 'height'),
            self.GetResolutionData.set_rezulution(80, 'with'),
            self.GetResolutionData.set_rezulution(5, 'height')
        ]

    def window(self):
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

    def base_dialog(self):
        return self.Base.dialog()

    def base_menu(self):
        return self.Base.menu()

    def base_navbar(self):
        return self.Base.navbar()

    def base_window(self):
        return self.Base.window()

    def set_rezulution(self, procent, var_type):
        if var_type == 'with':
            new_procent = int(procent * self.Base.width / 100)
        else:
            new_procent = int(procent * self.Base.height / 100)
        return new_procent

    def show(self):
        return {
            "EditMovieGalery":{
                "position": self.base_window(),
                'dialog': self.base_dialog(),
                "window": {
                    "navbar": self.base_navbar(),
                    "list_view_size": [
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(5, 'height'),
                        self.set_rezulution(50, 'with'),
                        self.set_rezulution(80, 'height')
                    ],
                    "title_size": [
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(2, 'height'),
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(5, 'height')
                    ]
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
            "EditSeries":{ #edit_view
                "position": self.base_window(),
                "window":{
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
            "Series":{
                "position": self.base_window(),
                "window":{
                    "navbar": self.base_navbar(),

                    "title_size": [
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(2, 'height'),
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(5, 'height')
                    ],

                    "avatar_size": [
                        self.set_rezulution(5, 'with'),
                        self.set_rezulution(10, 'height'),
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(25, 'height')
                    ],

                    "info_size": [
                        self.set_rezulution(8, 'with'),
                        self.set_rezulution(25, 'height'),
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(25, 'height')
                    ],

                    "galery_size": [
                        self.set_rezulution(1, 'with'),
                        self.set_rezulution(40, 'height'),
                        self.set_rezulution(20, 'with'),
                        self.set_rezulution(30, 'height')
                    ],

                    "galery_photo_size": [
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(8, 'height')
                    ],
                    "galery_item_show": 2,

                    "description": [
                        self.set_rezulution(1, 'with'),
                        self.set_rezulution(60, 'height'),
                        self.set_rezulution(20, 'with'),
                        self.set_rezulution(30, 'height')
                    ],

                    "description_limit": self.set_rezulution(25, 'with'),

                    "list_view_size": [
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(8, 'height'),
                        self.set_rezulution(45, 'with'),
                        self.set_rezulution(80, 'height')
                    ],

                    "section_avatar": [
                        self.set_rezulution(2, 'with'),
                        self.set_rezulution(2, 'height'),
                        self.set_rezulution(12, 'with'),
                        self.set_rezulution(25, 'height')
                    ],

                    "section_info": [
                        self.set_rezulution(5, 'with'),
                        self.set_rezulution(30, 'height'),
                        self.set_rezulution(12, 'with'),
                        self.set_rezulution(25, 'height')
                    ],

                    "section_scroller":[
                        self.set_rezulution(15, 'with'),
                        self.set_rezulution(5, 'height'),
                        self.set_rezulution(28, 'with'),
                        self.set_rezulution(70, 'height')
                    ],

                    #single

                    "section_avatar_single_movie" :[
                        self.set_rezulution(2, 'with'),
                        self.set_rezulution(5, 'height'),
                        self.set_rezulution(12, 'with'),
                        self.set_rezulution(25, 'height')
                    ],
                    "section_info_single_info"  : [
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(5, 'height'),
                        self.set_rezulution(12, 'with'),
                        self.set_rezulution(10, 'height')
                    ],
                    "single_title"  : [
                        self.set_rezulution(-10, 'with'),
                        self.set_rezulution(-10, 'height'),
                        self.set_rezulution(70, 'with'),
                        self.set_rezulution(25, 'height')
                    ],
                    "single_play_button":[
                        self.set_rezulution(18, 'with'),
                        self.set_rezulution(20, 'height'),
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(5, 'height')
                    ],
                    "single_info_button":[
                        self.set_rezulution(32, 'with'),
                        self.set_rezulution(20, 'height'),
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(5, 'height')
                    ]
                }
            },
            "MovieListView": {
                "position": self.base_window(),
                "window":{
                    "info_size"       : [
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(25, 'height'),
                        self.set_rezulution(20, 'with'),
                        self.set_rezulution(25, 'height')
                    ],
                    "title_size": [
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(0, 'height'),
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(5, 'height')
                    ],
                    "list_view_size"  : [
                        self.set_rezulution(25, 'with'),
                        self.set_rezulution(5, 'height'),
                        self.set_rezulution(40, 'with'),
                        self.set_rezulution(80, 'height')
                    ],
                    "avatar_size"     : [
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(10, 'height'),
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(15, 'height')],
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

            "Producent" : {
                "position": self.base_window(),
                "window": {
                    "navbar": self.base_navbar(),

                    "title_size": [
                        self.set_rezulution(-10, 'with'),
                        self.set_rezulution(0, 'height'),
                        self.set_rezulution(90, 'with'),
                        self.set_rezulution(10, 'height')
                    ],

                    "avatar_size": [
                        self.set_rezulution(5, 'with'),
                        self.set_rezulution(8, 'height'),
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(20, 'height')
                    ],

                    "galery_size": [
                        self.set_rezulution(40, 'with'),
                        self.set_rezulution(8, 'height'),
                        self.set_rezulution(30, 'with'),
                        self.set_rezulution(30, 'height')
                    ],

                    "galery_item_show" :2,

                    "galery_photo_size": [self.set_rezulution(10, 'with'), self.set_rezulution(15, 'height')],

                    "info_size": [
                        self.set_rezulution(20, 'with'),
                        self.set_rezulution(10, 'height'),
                        self.set_rezulution(30, 'with'),
                        self.set_rezulution(15, 'height')
                    ],

                    "description": [
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(12, 'height'),
                        self.set_rezulution(30, 'with'),
                        self.set_rezulution(30, 'height')
                    ],

                    "list_view_size": [
                        self.set_rezulution(5, 'with'),
                        self.set_rezulution(40, 'height'),
                        self.set_rezulution(65, 'with'),
                        self.set_rezulution(50, 'height')
                    ],

                    "description_limit": 500,

                    "section": {
                        "avatar_with": self.set_rezulution(7, 'with'),
                        "avatar_height": self.set_rezulution(12, 'height'),
                        "button_with": self.set_rezulution(6, 'with'),
                        "button_height": self.set_rezulution(2, 'height'),
                        "left": self.set_rezulution(2, 'with'),
                        "left_add": self.set_rezulution(10, 'with'),
                        "strings_in_title": self.set_rezulution(5, 'with'),
                        "font": "10",
                        "top": 0,
                        "top_add": 250,
                        "per_row": 6,
                        "per_page": 12
                    }
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
                'dialog': self.base_dialog(),
                "window": {
                    "title_size": [
                        self.set_rezulution(-10, 'with'),
                        self.set_rezulution(0, 'height'),
                        self.set_rezulution(90, 'with'),
                        self.set_rezulution(10, 'height')
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
                "position": self.base_window(),
                "window":{
                    "navbar": self.base_navbar(),
                    "title_size": [
                        self.set_rezulution(-10, 'with'),
                        self.set_rezulution(0, 'height'),
                        self.set_rezulution(90, 'with'),
                        self.set_rezulution(10, 'height')
                    ],
                    "avatar_size": [
                        self.set_rezulution(5, 'with'),
                        self.set_rezulution(8, 'height'),
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(20, 'height')
                    ],
                    "info_size"         : [
                        self.set_rezulution(20, 'with'),
                        self.set_rezulution(10, 'height'),
                        self.set_rezulution(30, 'with'),
                        self.set_rezulution(15, 'height')
                    ],
                    "galery_size"       : [
                        self.set_rezulution(40, 'with'),
                        self.set_rezulution(8, 'height'),
                        self.set_rezulution(30, 'with'),
                        self.set_rezulution(30, 'height')
                    ],
                    "description": [
                        self.set_rezulution(10, 'with'),
                        self.set_rezulution(12, 'height'),
                        self.set_rezulution(30, 'with'),
                        self.set_rezulution(30, 'height')
                    ],
                    "description_limit": 500,
                    "galery_item_show": 2,
                    "galery_photo_size": [self.set_rezulution(10, 'with'),self.set_rezulution(15, 'height')],
                    "list_view_size"    : [
                        self.set_rezulution(5, 'with'),
                        self.set_rezulution(40, 'height'),
                        self.set_rezulution(65, 'with'),
                        self.set_rezulution(50, 'height')
                    ],
                    "section": {
                        "avatar_with"  : self.set_rezulution(7, 'with'),
                        "avatar_height": self.set_rezulution(12, 'height'),
                        "button_with"  :self.set_rezulution(6, 'with'),
                        "button_height":self.set_rezulution(2, 'height'),
                        "left"         : self.set_rezulution(2, 'with'),
                        "left_add"     : self.set_rezulution(10, 'with'),
                        "strings_in_title" :self.set_rezulution(5, 'with'),
                        "font"         : 10,
                        "top"          : 0,
                        "top_add"      : 250,
                        "per_row"      : 6,
                        "per_page"     : 12
                    }
                }

            }
        }
