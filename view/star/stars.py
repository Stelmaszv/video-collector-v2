from app.db.models import Stars
from core.view import BaseView
from core.datamanipulation import Data
from core.creator import SeriesCreator
from PyQt5.QtWidgets import QWidget
from core.rezolution import SetResolution
from core.strings import stringManipupations
from datetime import datetime

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
                "itemName2": str(13500)+ ' / ' +str(131)
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
        self.BaseView.description(stringManipupations.short('Thomas Sean Connery urodził się 25 sierpnia 1930 roku w Edynburgu. Jego ojciec Joe, był robotnikiem i kierowcą ciężarówki, matka Euphemia prowadziła dom. Pierwszej pracy (roznosiciela mleka) podjął się w wieku 9 lat. Jako 13-latek rzucił szkołę i rozpoczął pracę w hucie. Gdy miał lat 16 zaciągnął się do marynarki. Trzy lata później musiał z wojska zrezygnować z powodu kłopotów z układem pokarmowym.  Dla żartu zgłosił się na próbę do musicalu "South Pacific" i dostał w nim niewielką rolę. Zaczął grać epizodyczne role w telewizyjnych spektaklach. Uznanie przyniosła mu rola boksera w telewizyjnym spektaklu "Requiem for a Heavyweight". Po raz pierwszy na dużym ekranie pojawił się w 1954 roku w filmie "Lilacs in the Spring". Pierwszym znaczącym tytułem w jego filmografii był "Najdłuższy dzień". Z dużymi wątpliwościami wcielił się w postać Bonda. Zagrał w ponad 140 filmach, za rolę Jima Malone w filmie "Nietykalni" zdobył Oscara w kategorii najlepszy aktor drugoplanowy.',limit),data);

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

