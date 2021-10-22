from core.setings import data_JSON
from pathlib import Path
import os

class HTMLGenaratorBase:
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
            'main.css',
            data_JSON['project_url'] + '\HTML_Genarator\css')

        self.create_file(
            self.js,
            'main.js',
            data_JSON['project_url'] + '\HTML_Genarator\js')

        self.create_file(
            self.js,
            'movies.js',
            data_JSON['project_url'] + '\OUTPUT\js')

        self.create_file(
            self.js,
            'producents.js',
            data_JSON['project_url'] + '\OUTPUT\js')

        self.create_file(
            self.js,
            'series.js',
            data_JSON['project_url'] + '\OUTPUT\js')

        self.create_file(
            self.js,
            'movies.js',
            data_JSON['project_url'] + '\OUTPUT\js')

        self.create_file(
            self.js,
            'stars.js',
            data_JSON['project_url'] + '\OUTPUT\js')

        self.create_file(
            self.json,
            'movies.JSON',
            data_JSON['project_url'] + '\OUTPUT\json')

        self.create_file(
            self.json,
            'producents.JSON',
            data_JSON['project_url'] + '\OUTPUT\json')

        self.create_file(
            self.json,
            'series.JSON',
            data_JSON['project_url'] + '\OUTPUT\json')

        self.create_file(
            self.json,
            'stars.JSON',
            data_JSON['project_url'] + '\OUTPUT\json')


    def return_html_as_string(self, shema_url):
        return Path(shema_url).read_text()

    def create_file(self, dir, file_name, shema_url):
        if Path(dir + '\\' + file_name).is_file() is True:
            os.remove(dir + '\\' + file_name)
        f = open(dir + '\\' + file_name, "x")
        f.write(self.return_html_as_string(shema_url + '\\' + str(file_name)))
        f.close()
