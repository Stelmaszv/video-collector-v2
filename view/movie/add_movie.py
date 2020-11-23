from PyQt5.QtWidgets import QWidget
class AddMovieView(QWidget):

    def __init__(self):
        super().__init__()
        self.window_title = 'add new Movie'

    def run_window(self):
        self.setWindowTitle(self.window_title)
        self.show()