import sys
from PyQt5.QtWidgets import QApplication
from pathlib import Path
from app.db.models import session, Movies,Stars,Series,Sezons,Photos
from core.config import ConfigLoop, ConfigMovies
from core.dir import LoadFilesFromJson, PhotoMeaker
from core.setings import data_JSON,scan_photos,run_start_view,clean_db
from view.menu.menu import Menu
from view.config.config_data_json import JSONConfigView

class DBCleaner:

    models=[Movies,Stars,Series,Sezons,Photos]

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

            JSON = LoadFilesFromJson(data_JSON['dirs'])
            JSON.add_files()

            Config = ConfigLoop(data_JSON['dirs'])
            Config.load()

            Config = ConfigMovies(data_JSON['movies_photos'])
            Config.load()

            if self.scan_photos:
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
    Run=Run(Menu(),JSONConfigView(),DBCleaner())
    Run.start()
    if Run.config:
        Run.show_start_view()
    sys.exit(app.exec_())