import sys
from PyQt5.QtWidgets import QApplication
from pathlib import Path
from app.db.models import session, Movies,Stars,Series,Sezons,Photos,Producent
from core.config import ConfigLoop, ConfigMovies,SetTags,CreateXML,CreateMovieList
from core.dir import LoadFilesFromJson, PhotoMeaker
from core.html_gerator import HTMLGenaratorMain, GenerateHTMLMovies
from core.setings import data_JSON, scan_photos, run_start_view, clean_db, start_page, scan_dir, config, config_movies \
    , set_tags, create_xml, create_movie_list, generate_json_otputs_movies, create_json_dblist, \
    generate_json_otputs_stars, generate_json_otputs_producents, generate_html_base, generate_html_movies, open_html
from view.menu.menu import Menu
from view.config.config_data_json import JSONConfigView
from core.create_JSON_DB_LIST import CreateJSONDBLIST, GenerateJSONOtputsMovies, GenerateJSONOtputsStars, \
    GenerateJSONOtputsSeries, GenerateJSONOtputsProducent

class DBCleaner:

    models=[Movies,Stars,Series,Sezons,Photos,Producent]

    def clean(self):
        for Model in self.models:
            print("DB is erasing ! - " + str(Model.__name__))
            session.query(Model).delete()
            session.commit()


class LoopRun:
    objets = []

    def run_object(self, Obj, method, run, start_string, end_string):
        if run:
            print(start_string)
            method = getattr(Obj, method)
            method()
            print(end_string)

    def loop(self):
        for objet in self.objets:
            self.run_object(objet['obj'], objet['method'], objet['stan'], objet['start_mes'], objet['end_mees'])

class Run:

    scan_photos=scan_photos
    run_start_view=run_start_view
    config=True

    def __init__(self, StartView, JSONConfigView):
        self.StartView=StartView
        self.JSONConfigView = JSONConfigView
        self.LoopRun = LoopRun()

    def start(self):

        self.LoopRun.objets = [
            {
                "obj": DBCleaner(), "method": 'clean',
                "stan": clean_db, "start_mes": 'Erasing is started !', "end_mees": 'DB is erased !'
            },
            {
                "obj": LoadFilesFromJson(data_JSON['dirs']), "method": 'add_files',
                "stan": scan_dir, "start_mes": 'Scaning Dir in progres', "end_mees": 'End of scaning'
            },
            {
                "obj": ConfigLoop(data_JSON['dirs']), "method": 'load',
                "stan": config, "start_mes": 'Config in progres', "end_mees": 'End of Config'
            },
            {
                "obj": ConfigMovies(data_JSON['movies_photos']), "method": 'load',
                "stan": config_movies, "start_mes": 'Config Movies in progres', "end_mees": 'End of Movies in progres'
            },
            {
                "obj": SetTags(data_JSON['dirs']), "method": 'set',
                "stan": set_tags, "start_mes": 'Set Tags in progres', "end_mees": 'End of Set Tags in progres'
            },
            {
                "obj": CreateXML(data_JSON['dirs']), "method": 'load',
                "stan": create_xml, "start_mes": 'Createing XML in progres',
                "end_mees": 'End of Createing XML in progres'
            },
            {
                "obj": CreateMovieList(data_JSON['dirs']), "method": 'load',
                "stan": create_movie_list, "start_mes": 'Createing Movies List in progres',
                "end_mees": 'End of Createing Movies List in progres'
            },
            {
                "obj": CreateJSONDBLIST(), "method": 'create',
                "stan": create_json_dblist, "start_mes": 'Config JSON Outputs in progres',
                "end_mees": 'End of Config JSON Outputs in progres'
            },
            {
                "obj": GenerateJSONOtputsMovies(), "method": 'create',
                "stan": generate_json_otputs_movies, "start_mes": 'Config JSON Outputs for movies in progres',
                "end_mees": 'End of Config JSON Outputs for movies in progres'
            },
            {
                "obj": GenerateJSONOtputsStars(), "method": 'create',
                "stan": generate_json_otputs_stars, "start_mes": 'Config JSON Outputs for stars in progres',
                "end_mees": 'End of Config JSON Outputs for stars in progres'
            },
            {
                "obj": GenerateJSONOtputsProducent(), "method": 'create',
                "stan": generate_json_otputs_producents, "start_mes": 'Config JSON Outputs for producent in progres',
                "end_mees": 'End of Config JSON Outputs for producent in progres'
            },
            {
                "obj": HTMLGenaratorMain(), "method": 'generate',
                "stan": generate_html_base, "start_mes": 'Genereting HTML Base',
                "end_mees": 'End of Genereting HTML Base'
            },
            {
                "obj": GenerateHTMLMovies(), "method": 'generate',
                "stan": generate_html_movies, "start_mes": 'Genereting HTML Movies',
                "end_mees": 'End of Genereting HTML Movies'
            },
        ]

        if Path('data.json').is_file():
            self.LoopRun.loop()

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
    Run = Run(Menu(start_page), JSONConfigView())
    Run.start()
    if Run.config:
        Run.show_start_view()
    sys.exit(app.exec_())