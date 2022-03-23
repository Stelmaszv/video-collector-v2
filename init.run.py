import sys

from PyQt5.QtWidgets import QApplication

from core.run import JSONRun, Run
from core.setings import MODERUN, start_page
from view.config.config_data_json import JSONConfigView
from view.menu.menu import Menu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if MODERUN == "console":
        Run = Run(Menu(start_page), JSONConfigView())
        Run.start()
        if Run.config:
            Run.show_start_view()
    if MODERUN == "config":
        Run = JSONRun(Menu(start_page), JSONConfigView())
        Run.show_start_view()
    sys.exit(app.exec_())