from core.config import ConfigLoop, ConfigMovies, SetTags, CreateXML, CreateMovieList
from core.create_JSON_DB_LIST import CreateJSONDBLIST, GenerateJSONOtputsSeries, GenerateJSONOtputsStars, \
    GenerateJSONOtputsProducent
from core.dir import LoadFilesFromJson
from core.html_gerator import HTMLGenaratorMain, GenerateHTMLMovies, GenerateHTMLProducents, GenerateHTMLSeries, \
    GenerateHTMLStars
from core.setings import data_JSON
from core.view import AbstractBaseView
from PyQt5.QtWidgets import QWidget
from app.model_view import ConfigAddDataModel

class MovieScanInfo(QWidget, AbstractBaseView):
    ModelView = ConfigAddDataModel
    resolution_index = 'VCSCAN'
    show_elemnts = ['Title', 'Galery', 'Nav', 'Avatar', 'List', 'Form','Info']
    adding=False
    reset_view = 'MovieScanInfo'
    window_title = "VC Scan"
    data_array=[]
    info_data_index=0
    info_data_array=0

    def after_init(self):

        data_scroler = {
            "res": self.WindowSize['scroler'],
            "objects": self.data_array
        }
        self.scrol = self.BaseView.Form.custum_scroll_bar(data_scroler)

        data = {
            "click_btm_info": "Star Scan!",
            "res": self.WindowSize['custum_button'],
            "click_method": self.start_scan,
            "font": ['Times', 50]
        }

        self.BaseView.Form.custum_button(data)

    def load_config_view(self):
        self.close()
        self.BaseView.load_view('ConfigScan')

    def start_scan(self):
        self.data_array = []
        LFFJ = LoadFilesFromJson(data_JSON['dirs'],self)
        LFFJ.add_files()

        CL=ConfigLoop(data_JSON['dirs'],self)
        CL.load()

        CM=ConfigMovies(data_JSON['movies_photos'],self)
        CM.load()

        ST=SetTags(data_JSON['dirs'],self)
        ST.set()

        CX=CreateXML(data_JSON['dirs'])
        CX.load()

        CML=CreateMovieList(data_JSON['dirs'])
        CML.load()

        CJB=CreateJSONDBLIST()
        CJB.create()

        OBJ=GenerateJSONOtputsSeries()
        OBJ.create()

        OBJ = GenerateJSONOtputsStars()
        OBJ.create()

        OBJ = GenerateJSONOtputsProducent()
        OBJ.create()

        OBJ = HTMLGenaratorMain()
        OBJ.generate()

        OBJ = GenerateHTMLMovies()
        OBJ.generate()

        OBJ = GenerateHTMLProducents()
        OBJ.generate()

        OBJ = GenerateHTMLSeries()
        OBJ.generate()

        OBJ = GenerateHTMLStars()
        OBJ.generate()

        self.close()
        MSI=MovieScanInfo()
        MSI.data_array=self.data_array
        MSI.adding=True
        MSI.run_window()





