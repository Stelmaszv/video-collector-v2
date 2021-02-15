import sys
from PyQt5.QtWidgets import QApplication
from view.menu.menu import Menu

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.run_window()
    sys.exit(app.exec_())