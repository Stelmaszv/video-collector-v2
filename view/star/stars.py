from app.db.models import Stars
from core.view import BaseView
from core.datamanipulation import Data
from core.creator import SeriesCreator
from PyQt5.QtWidgets import QWidget
from core.rezolution import SetResolution
from core.strings import stringManipupations

class StarView(QWidget):

    model        = Stars
    window_type  = 'star'

    def __init__(self):
        super().__init__()
        self.BaseView= BaseView([], self)
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

    def closeEvent(self, event):
        self.list=[]

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

        infData=[
            {
             "itemNmae"  :  "Date of birth / Age",
             "itemName2" : self.Data.show()+' / '+self.Data.get_age()
            },
            {
             "itemNmae"  : "Movies / Series",
             "itemName2" : self.count_series()+' / '+self.count_movies()
            },
            {
                "itemNmae": "Views / Likes",
                "itemName2": str(self.data.views)+ ' / ' +str(self.data.likes)
            },
            {
                "itemNmae": "Favourite",
                "itemName2": str(self.data.favourite)
            },
            {
                "itemNmae": "Height / Weight",
                "itemName2": str(self.data.height)+' cm  / '+str(self.data.weight)+' kg'
            },
            {
                "itemNmae": "Ethnicity",
                "itemName2": self.data.ethnicity
            },
            {
                "itemNmae": "Hair color",
                "itemName2": self.data.hair_color
            },
            {
                "itemNmae": "Tags",
                "itemName2": 'Bond, dead, Action'
            },
        ]

        self.BaseView.info(infData, data, rows)
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


    def closeEvent(self, QCloseEvent):
        self.Router.close_window()

