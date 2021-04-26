from core.setings import screen_width,screen_height
class SetResolution:

    def __init__(self,AbstractBaseView):
        self.AbstractBaseView = AbstractBaseView
        self.menu_set=self.return_abstrat_view()

    def return_abstrat_view(self):
        return GetResolutionData(self.AbstractBaseView).show()

class GetResolutionData:

    def __init__(self, AbstractBaseView):
        self.AbstractBaseView = AbstractBaseView
        self.width    = screen_width
        self.height   = screen_height

    def base_var(self,index,item_index):
        data = {
            "menu" :{
                "left"             : self.set_rezulution(0,'with'),
                "top"              : self.set_rezulution(2,'height'),
                "width"            : self.set_rezulution(25,'with'),
                "height"           : self.set_rezulution(100,'height')
            },

            "window":{
                "left":   self.set_rezulution(25, 'with'),
                "top":    self.set_rezulution(2, 'height'),
                "width":  self.set_rezulution(75, 'with'),
                "height": self.set_rezulution(100, 'height')
            }
        }
        return data[index][item_index]

    def set_rezulution(self,procent,var_type):
        if var_type=='with':
            new_procent = int(procent * self.width /100)
        else:
            new_procent  = int(procent * self.height / 100)
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
                "position": {
                    "left"             : self.base_var('window','left'),
                    "top"              : self.base_var('window','top'),
                    "width"            : self.base_var('window','width'),
                    "height"           : self.base_var('window','height')
                },
                "window": {
                    "tags_name" : [450,500,100,50],
                    "tags"      : [350,550,350, 50],
                    "tags_limit" :1000,
                    "star_name": [800, 500,100,50],
                    "stars_limit": 1000,
                    "stars": [750,550,350, 50],
                    "title_size": [0, 0, 1280, 100],
                    "form_section": [400, 100, 480, 400],
                }
            },
            "Menu": {
                "position": {
                    "left"             : self.base_var('menu','left'),
                    "top"              : self.base_var('menu','top'),
                    "width"            : self.base_var('menu','width'),
                    "height"           : self.base_var('menu','height')
                },
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
                    "title_size"    : [0, 0 ,1280 ,50],
                    "form_section"  : [400, 0 ,480 ,120],
                    "list_view_size": [300, 100, 680, 250],
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
