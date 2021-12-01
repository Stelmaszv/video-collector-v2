from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.model_view import ConfigAddDataModel
from app.info import MovieScanInfoSection

class MovieScanInfo(QWidget, AbstractBaseView):
    ModelView = ConfigAddDataModel
    Info = MovieScanInfoSection
    window_title = 'Found Items to add!'
    resolution_index = 'VCSCAN'
    show_elemnts = ['Title', 'Galery', 'Nav', 'Avatar', 'List', 'Form']
    adding=False
    def after_init(self):
        if self.adding is False:
            data = {
                "click_btm_info": "Star Scan!",
                "res":self.WindowSize['custum_button'],
                "click_method":self.start_scan,
                "font": ['Times',50]
            }
            self.BaseView.Form.custum_button(data)

    def start_scan(self):
        self.close()
        Movie_scan=MovieScanInfo()
        Movie_scan.show_elemnts.append('Info')
        Movie_scan.window_title='Adding objects ... '
        Movie_scan.adding = True
        Movie_scan.run_window()



