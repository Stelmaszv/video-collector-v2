import sys
from PyQt5.QtWidgets import QApplication
from core.setings import MODERUN, start_page
from core.run import Run,JSONRun
from view.config.config_data_json import JSONConfigView
from view.menu.menu import Menu
#run !
if __name__ == '__main__':
    app = QApplication(sys.argv)
    if MODERUN == "console":
        Run = Run(Menu(start_page), JSONConfigView())
        Run.start()
        if Run.config:
            Run.show_start_view()
    if MODERUN == "config":
        Run = JSONRun()
        Run.start()
    sys.exit(app.exec_())