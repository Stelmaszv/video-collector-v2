from PyQt5.QtWidgets import QWidget

from app.info import ConfigInfoSection
from app.model_view import ConfigAddDataModel
from core.config import ConfigLoop, ConfigMovies, SetTags
from core.setings import data_JSON
from core.view import AbstractBaseView


class ConfigScan(QWidget, AbstractBaseView):
    ModelView = ConfigAddDataModel
    Info = ConfigInfoSection
    resolution_index = 'VCSCAN'
    show_elemnts = ['Title', 'Galery', 'Nav', 'Avatar', 'List', 'Form']
    adding=False
    reset_view = 'MovieScanInfo'
    data_array=[]
    info_data_index=0
    info_data_array=0

    def after_init(self):
        if self.info_data_array:
            self.window_title = "Found " + str(self.info_data_array) + " items to config!";
            data = {
                "click_btm_info": "Star Config!",
                "res":self.WindowSize['custum_button'],
                "click_method":self.start_config,
                "font": ['Times',50]
            }
        else:
            self.window_title = "No found items to config !"
            data = {
                "click_btm_info": "Next",
                "res":self.WindowSize['go_to_config'],
                "click_method":self.load_config_view,
                "font": ['Times',50]
            }

        self.title()
        if self.adding is False:
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
                "click_method":self.load_config_view,
                "font": ['Times',50]
            }
            self.BaseView.Form.custum_button(data)

    def load_config_view(self):
        self.close()

    def start_config(self):
        self.close()
        CF=ConfigLoop(data_JSON['dirs'])
        CF.load()

        CM=ConfigMovies(data_JSON['movies_photos'])
        CM.load()

        ST=SetTags(data_JSON['dirs'])
        ST.load()