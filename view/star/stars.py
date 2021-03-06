from app.db.models import Stars
from core.view import BaseView
from core.datamanipulation import Data
from core.creator import SeriesCreator
from PyQt5.QtWidgets import QWidget
from core.rezolution import SetResolution
from core.strings import stringManipupations
from  core.BaseActions import ViewBaseAction

class StarView(QWidget):

    model        = Stars
    window_type  = 'star'

    def __init__(self):
        super().__init__()
        self.BaseView= BaseView([], self)
        self.BaseActions=ViewBaseAction(self)
        self.SetResolution = SetResolution()
        self.left =   self.SetResolution.menu_set['Stars']['position']['left']
        self.top =    self.SetResolution.menu_set['Stars']['position']['top']
        self.width =  self.SetResolution.menu_set['Stars']['position']['width']
        self.height = self.SetResolution.menu_set['Stars']['position']['height']
        self.WindowSize=self.SetResolution.menu_set['Stars']['window']

    def run_window(self):
        self.BaseView.set_data(self.id)
        self.data = self.BaseView.data
        self.Data = Data(self.data.date_of_birth)
        self.seriesResult()
        self.initUI()
        self.window_title = self.data.name
        self.show()
        self.setWindowTitle(self.window_title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.BaseActions.update_view();
        return True

    def closeEvent(self, event):
        self.list=[]

    def get_nav(self):

        self.BaseView.get_nav_star(
            [650, -145, 480, 400],
            [
                {
                    "name": "Add to favorits",
                    "item_name": "add_to_favorits",
                    "button": self.add_favorits
                },
                {
                    "name": "Add like",
                    "item_name": "add_like",
                    "button": self.add_like
                },
                {
                    "name": "Edit",
                    "item_name": "edit",
                    "button": self.edit
                },
                {
                    "name": "Reset",
                    "item_name": "reset",
                    "button":self.reset
                },
            ]
        )

    def add_favorits(self):
        self.BaseActions.add_favourite()

    def add_like(self):
        self.BaseActions.add_like()

    def edit(self):
        self.BaseActions.edit()

    def reset(self):
        self.BaseActions.reset()

    def title(self):
        data = [
            self.WindowSize['title_size'][0],
            self.WindowSize['title_size'][1],
            self.WindowSize['title_size'][2],
            self.WindowSize['title_size'][3]
        ]
        text = "<html><head/><body>" \
               "<p align=\"center\">" \
               "<span style=\" font-size:18pt;font-weight:600; " \
               "text-decoration: underline;\">" + self.data.name + \
               "</span></p></body></html>"
        self.BaseView.title(data, text)


    def galery(self):
        data= [
            self.WindowSize['galery_size'][0],
            self.WindowSize['galery_size'][1],
            self.WindowSize['galery_size'][2],
            self.WindowSize['galery_size'][3]
        ]
        size=[
            self.WindowSize['galery_photo_size'][0],
            self.WindowSize['galery_photo_size'][1]
        ]
        self.BaseView.galery(data, size, self.WindowSize['galery_item_show'])


    def info(self):

        data   = [
            self.WindowSize['info_size'][0],
            self.WindowSize['info_size'][1],
            self.WindowSize['info_size'][2],
            self.WindowSize['info_size'][3]
        ]

        rows = ['itemNmae','itemName2']
        data_info=[];
        if self.data.date_of_birth:
            data_info.append( {
                 "itemNmae"  :  "Date of birth / Age",
                 "itemName2" : self.Data.show()+' / '+self.Data.get_age()
            })

        if self.data.height and self.data.weight:
            data_info.append({
                "itemNmae": "Height / Weight",
                "itemName2": str(self.data.height) + ' cm  / ' + str(self.data.weight) + ' kg'
            })

        if self.data.ethnicity:
            data_info.append({
                "itemNmae": "Ethnicity",
                "itemName2": self.data.ethnicity
            })

        if self.data.hair_color:
            data_info.append({
                "itemNmae": "Hair color",
                "itemName2": self.data.hair_color
            })

        data_info.append({
             "itemNmae"  : "Movies / Series",
             "itemName2" : self.count_series()+' / '+self.count_movies()
            })

        data_info.append({
                "itemNmae": "Views / Likes",
                "itemName2": str(self.data.views)+ ' / ' +str(self.data.likes)
        })

        data_info.append({
                "itemNmae": "Favourite",
                "itemName2": str(self.data.favourite)
        })

        data_info.append({
            "itemNmae": "Tags",
            "itemName2": 'Bond, dead, Action'
        })

        self.BaseView.info(data_info, data, rows)
        data=[
            self.WindowSize['description'][0],
            self.WindowSize['description'][1],
            self.WindowSize['description'][2],
            self.WindowSize['description'][3],
        ]

        limit=self.WindowSize['description'][4]
        self.BaseView.description(stringManipupations.short(self.data.description,limit),data);
        

    def count_series(self):
        return str(len(self.list))

    def count_movies(self):
        count=0;
        for item in self.list:
            count=count+len(item['movies'])
        return str(count)

    def seriesResult(self):
        self.list=[]
        self.list = SeriesCreator(self.data).return_obj()
        self.BaseView.listView([
            self.WindowSize['list_view_size'][0],
            self.WindowSize['list_view_size'][1],
            self.WindowSize['list_view_size'][2],
            self.WindowSize['list_view_size'][3]
        ], self.list , 'Stars',self)

    def avatar(self):
        self.BaseView.avatar([
            self.WindowSize['avatar_size'][0],
            self.WindowSize['avatar_size'][1],
            self.WindowSize['avatar_size'][2],
            self.WindowSize['avatar_size'][3]
        ])

    def initUI(self):
        self.avatar();
        self.title()
        self.galery()
        self.info()
        self.get_nav()

    def closeEvent(self, QCloseEvent):
        self.Router.close_window()

