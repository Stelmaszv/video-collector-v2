import sys
from PyQt5.QtWidgets import QApplication
from pathlib import Path
from app.db.models import session, Movies,Stars,Series,Sezons,Photos,Producent
from core.config import ConfigLoop, ConfigMovies,SetTags,CreateXML,CreateMovieList
from core.dir import LoadFilesFromJson, PhotoMeaker
from core.setings import data_JSON,scan_photos,run_start_view,clean_db,start_page
from view.menu.menu import Menu
from view.config.config_data_json import JSONConfigView
from core.create_JSON_DB_LIST import CreateJSONDBLIST, GenerateJSONOtputsMovies, GenerateJSONOtputsStars, \
    GenerateJSONOtputsSeries, GenerateJSONOtputsProducent

class DBCleaner:

    models=[Movies,Stars,Series,Sezons,Photos,Producent]

    def clean(self):

        for Model in self.models:
            session.query(Model).delete()
            session.commit()

        print('DB is erased !')

class Run:

    scan_photos=scan_photos
    run_start_view=run_start_view
    config=True
    clean_db=clean_db

    def __init__(self,StartView,JSONConfigView,DBCleaner):
        self.StartView=StartView
        self.JSONConfigView = JSONConfigView
        self.DBCleaner=DBCleaner

    def start(self):
        if self.clean_db:
            self.DBCleaner.clean()

        if Path('data.json').is_file():
            print("Scaning Dir in progres")
            JSON = LoadFilesFromJson(data_JSON['dirs'])
            JSON.add_files()
            print("Config in progres")
            Config = ConfigLoop(data_JSON['dirs'])
            Config.load()
            print("Config Movies in progres")
            Config = ConfigMovies(data_JSON['movies_photos'])
            Config.load()
            print("Set Tags in progres")
            SetTAgs=SetTags(data_JSON['dirs'])
            SetTAgs.set();
            print("Createing XML in progres")
            CreateXMLOBJ=CreateXML(data_JSON['dirs'])
            CreateXMLOBJ.load();
            print("Createing Movies List in progres")
            CreateXMLOBJ = CreateMovieList(data_JSON['dirs'])
            CreateXMLOBJ.load();

            """
            print("Config JSON Outputs in progres")
            CreateJSONDBLISTOBJ = CreateJSONDBLIST()
            CreateJSONDBLISTOBJ.create();
            """

            print("Config JSON Outputs for movies in progres")
            GenerateJSONOtputsMoviesOBJ = GenerateJSONOtputsMovies()
            GenerateJSONOtputsMoviesOBJ.create();

            print("Config JSON Outputs for stars in progres")
            GenerateJSONOtputsStarsOBJ = GenerateJSONOtputsStars()
            GenerateJSONOtputsStarsOBJ.create()

            print("Config JSON Outputs for producent in progres")
            GenerateJSONOtputsProducentOBJ = GenerateJSONOtputsProducent()
            GenerateJSONOtputsProducentOBJ.create()

            if self.scan_photos:
                print("Createing screen shots in progres")
                for Movie in session.query(Movies).all():
                    PM = PhotoMeaker(Movie, data_JSON['movies_photos'])
                    PM.make()

        else:
            self.config=False
            self.JSONConfigView.run_window()

    def show_start_view(self):
        if self.run_start_view:
            self.StartView.run_window()
        else:
            exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Run=Run(Menu(start_page),JSONConfigView(),DBCleaner())
    Run.start()
    if Run.config:
        Run.show_start_view()
    sys.exit(app.exec_())