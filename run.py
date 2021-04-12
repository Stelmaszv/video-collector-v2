import sys
from PyQt5.QtWidgets import QApplication
from pathlib import Path
from app.db.models import session, Movies
from core.config import ConfigLoop, ConfigMovies
from core.dir import LoadFilesFromJson, PhotoMeaker
from core.setings import data_JSON,scan_photos,run_start_view
from view.menu.menu import Menu
from view.config.config_data_json import JSONConfigView

class Run:

    scan_photos=scan_photos
    run_start_view=run_start_view
    config=True

    def __init__(self,StartView,JSONConfigView):
        self.StartView=StartView
        self.JSONConfigView = JSONConfigView

    def start(self):
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
    Run=Run(Menu(),JSONConfigView())
    Run.start()
    if Run.config:
        Run.show_start_view()
    sys.exit(app.exec_())