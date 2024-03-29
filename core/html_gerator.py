import json
import os
from pathlib import Path

from core.custum_errors import Error
from core.setings import data_JSON


class HtmlGenaratorBase:
    def return_html_as_string(self, shema_url):
        return Path(shema_url).read_text()

    def create_file(self, dir, file_name, shema_url):
        if Path(dir + '\\' + file_name).is_file() is True:
            os.remove(dir + '\\' + file_name)
        f = open(dir + '\\' + file_name, "w")
        file = shema_url + '\\' + str(file_name)
        html = self.return_html_as_string(file)
        htmloutput = html.replace("[#HTMLOUTPUT#]", data_JSON['html_output'])
        f.write(htmloutput)
        f.close()

class HTMLGenaratorMain:
    dir = data_JSON['html_output'] + '\HTML Generator'
    sites = data_JSON['html_output'] + '\HTML Generator\sites'
    css = data_JSON['html_output'] + '\HTML Generator\css'
    js = data_JSON['html_output'] + '\HTML Generator\js'
    json = data_JSON['html_output'] + '\HTML Generator\json'
    project_genarator_url = data_JSON['project_url']

    def __init__(self):
        if os.path.isdir(self.dir) is False:
            os.mkdir(self.dir)

        if os.path.isdir(self.sites) is False:
            os.mkdir(self.sites)

        if os.path.isdir(self.css) is False:
            os.mkdir(self.css)

        if os.path.isdir(self.js) is False:
            os.mkdir(self.js)

        if os.path.isdir(self.json) is False:
            os.mkdir(self.json)

    def generate(self):
        self.create_file(
            self.dir,
            'index.html',
            data_JSON['project_url'] + '\HTML_Genarator')

        self.create_file(
            self.sites,
            'stars.html',
            data_JSON['project_url'] + '\HTML_Genarator\schema')

        self.create_file(
            self.sites,
            'producent.html',
            data_JSON['project_url'] + '\HTML_Genarator\schema')

        self.create_file(
            self.sites,
            'series.html',
            data_JSON['project_url'] + '\HTML_Genarator\schema')

        self.create_file(
            self.sites,
            'movies.html',
            data_JSON['project_url'] + '\HTML_Genarator\schema')

        self.create_file(
            self.css,
            'baguetteBox.css',
            data_JSON['project_url'] + '\HTML_Genarator\css')

        self.create_file(
            self.css,
            'main.css',
            data_JSON['project_url'] + '\HTML_Genarator\css')

        self.create_file(
            self.css,
            'bootstrap.min.css',
            data_JSON['project_url'] + '\HTML_Genarator\css')

        self.create_file(
            self.css,
            'bootstrap.rtl.min.css',
            data_JSON['project_url'] + '\HTML_Genarator\css')

        self.create_file(
            self.js,
            'load.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.js,
            'counter_data.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.js,
            'search.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.js,
            'loadByid.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.js,
            'paginator.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.js,
            'lists.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.js,
            'baguetteBox.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.js,
            'movies.js',
            data_JSON['project_url'] + '\OUTPUT\js')

        self.create_file(
            self.js,
            'series.js',
            data_JSON['project_url'] + '\OUTPUT\js')

        self.create_file(
            self.js,
            'stars.js',
            data_JSON['project_url'] + '\OUTPUT\js')

        self.create_file(
            self.js,
            'producents.js',
            data_JSON['project_url'] + '\OUTPUT\js')

        self.create_file(
            self.js,
            'bootstrap.bundle.min.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.js,
            'cunter.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.js,
            'filters.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.js,
            'font.all.min.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.js,
            'movies_list.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.css,
            'awsome.all.min.css',
            data_JSON['project_url'] + '\HTML_Genarator\css')

        self.create_movies_list()

    def create_movies_list(self):

        def clear_movies_dir():
            movies_lists = os.listdir(self.js+'\\movies')
            for el_dir in movies_lists:
                os.remove(self.js+'\\movies\\'+el_dir)

        def create_file(el_dir):
            dir=self.js+'\movies'
            if Path(dir + '\\' + el_dir).is_file() is True:
                os.remove(dir + '\\' + el_dir)

            f = open(dir + '\\' + el_dir, "w")
            file=data_JSON['project_url'] + '\OUTPUT\movies\\'+el_dir
            f.write(HtmlGenaratorBase().return_html_as_string(file))
            f.close()

        clear_movies_dir()
        movies_lists=os.listdir('OUTPUT/movies')
        for el_dir in movies_lists:
            create_file(el_dir)

    def create_file(self, dir, file_name, shema_url):
        return HtmlGenaratorBase().create_file(dir, file_name, shema_url)

class AbstractGenarta:
    input = ""
    shema_file = ""

    def generate(self):
        Error.throw_error_bool("input not exist", self.input != "")
        Error.throw_error_bool("sheama_file not exist", self.shema_file != "")
        with open(self.input) as json_file:
            data = json.load(json_file)
            for item in data:
                print('Generate HTML for ' + str(item['name']))
                self.create_file(
                    item['dir'],
                    self.shema_file,
                    data_JSON['project_url'] + '\HTML_Genarator\schema')

    def create_file(self, dir, file_name, shema_url):
        return HtmlGenaratorBase().create_file(dir, file_name, shema_url)

class GenerateHTMLMovies(AbstractGenarta):
    input = "OUTPUT/json/movies.JSON"
    shema_file = "movies_id.html"


class GenerateHTMLProducents(AbstractGenarta):
    input = "OUTPUT/json/producents.JSON"
    shema_file = "producent_id.html"


class GenerateHTMLSeries(AbstractGenarta):
    input = "OUTPUT/json/series.JSON"
    shema_file = "series_id.html"


class GenerateHTMLStars(AbstractGenarta):
    input = "OUTPUT/json/stars.JSON"
    shema_file = "stars_id.html"
