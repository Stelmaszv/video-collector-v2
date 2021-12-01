import time

from PyQt5.QtCore import QEventLoop, QTimer

from core.dir import LoadFilesFromJson
from core.setings import data_JSON
from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.model_view import ConfigAddDataModel
from app.info import MovieScanInfoSection

class MovieScanInfo(QWidget, AbstractBaseView):
    ModelView = ConfigAddDataModel
    Info = MovieScanInfoSection
    resolution_index = 'VCSCAN'
    show_elemnts = ['Title', 'Galery', 'Nav', 'Avatar', 'List', 'Form']
    adding=False
    reset_view = 'MovieScanInfo'
    data_array=[]
    info_data_index=0
    info_data_array=0

    def after_init(self):
        if self.info_data_array:
            self.window_title = "Found " + str(self.info_data_array) + " items to add!";
        else:
            self.window_title = "No found items to add !"
        self.title()
        if self.adding is False:

            data = {
                "click_btm_info": "Star Scan!",
                "res":self.WindowSize['custum_button'],
                "click_method":self.start_scan,
                "font": ['Times',50]
            }

            self.BaseView.Form.custum_button(data)

        else:

            data_scroler = {
                "res": self.WindowSize['scroler'],
                "objects": self.data_array
            }
            self.BaseView.Form.custum_scroll_bar(data_scroler)

            data = {
                "click_btm_info": "Go to config!",
                "res":self.WindowSize['go_to_config'],
                "click_method":self.start_scan,
                "font": ['Times',50]
            }

            self.BaseView.Form.custum_button(data)

    def load_config_view(self):
        print('ok')

    def start_scan(self):
        self.data_array = []
        LFFJ = LoadFilesFromJson(data_JSON['dirs'], self)
        LFFJ.add_files()
        self.close()
        MSI=MovieScanInfo()
        MSI.data_array=self.data_array
        MSI.adding=True
        MSI.run_window()





