from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog,QToolButton,QButtonGroup
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl,pyqtSignal
from app.db.models import Movies,Stars
from app.db.models import session

class Player(QWidget):

    playerMuted = False
    model=Movies
    session=session
    list=1

    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1560 , 300)
        from core.view import BaseView
        self.base_view = BaseView([], self)

        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)



    def run_window(self):
        self.base_view.set_data(self.id)
        self.data = self.base_view.data
        print(self.data.id)
        self.file_name = self.data.src
        self.init_ui()
        self.show()
        self.setWindowTitle(self.data.name)
        self.mediaPlayer.play()


    def init_ui(self):


        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.file_name)))

        # create videowidget object

        videowidget = QVideoWidget()

        # create open button
        """
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)
        """

        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        self.show_full_screen_button = QPushButton('Full Screen')
        self.show_full_screen_button.clicked.connect(self.full_screen_switch)

        self.mute = QPushButton()
        self.mute.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        self.mute.clicked.connect(self.muteClicked)

        # create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(20, 20, 20, 10)

        # set widgets to the hbox layout
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)
        hboxLayout.addWidget(self.mute)
        hboxLayout.addWidget(self.show_full_screen_button)


        # create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addLayout(self.add_grup_movies_buttons())
        vboxLayout.addWidget(self.label)

        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(videowidget)


        # media player signals

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def buttom_genarator(self,list,fuction,id):
        for button in list.buttons():
            if button is list.button(id):
                fuction(button.data)

    def on_movies_play(self, id):
        self.buttom_genarator(self.buttons_stars, self.next_star, id)

    def add_grup_movies_buttons(self):
        hboxLayout2 = QHBoxLayout()
        hboxLayout2.setContentsMargins(10, 10, 10, 10)


        self.buttons_stars = QButtonGroup()

        self.buttons= [
            {'button': self.on_movies_play, 'obejct': self.buttons_stars},
        ]

        index=0
        for star in self.data.stars:
            button = QPushButton('next video with star '+str(star))
            hboxLayout2.addWidget(button)
            button.data=star
            self.buttons[0]['obejct'].addButton(button)
            self.buttons[0]['obejct'].buttonClicked[int].connect(self.buttons[0]['button'])
            index = index+1


        """
        self.next_video_in_series = QPushButton('next video in series')
        self.next_video_in_series.clicked.connect(self.next_series)
        """

        #hboxLayout2.addWidget(self.next_video_in_series)
        return hboxLayout2

    def closeEvent(self, QCloseEvent):
        self.mediaPlayer.stop()
        self.Router.close_window()

    def muteClicked(self):
        if self.mediaPlayer.isMuted() is False:
            icon= QStyle.SP_MediaVolumeMuted
            self.mediaPlayer.setMuted(True)
        else:
            icon = QStyle.SP_MediaVolume
            self.mediaPlayer.setMuted(False)

        self.mute.setIcon(self.style().standardIcon(icon))


    def next_series(self):
        print('series')

    def next_star(self,star):
        movies_with_star=session.query(self.model).filter(Stars.id==star.id).all()

        self.close()

        self.base_view.menu.searchIn='play'
        self.base_view.menu.open(movies_with_star[self.list])



    def full_screen_switch(self):
        if self.isFullScreen() is False:
            self.showFullScreen()
        else:
            self.showNormal()

    def mute_switch(self):
        self.changeMuting.emit(not self.playerMuted)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            icon=QStyle.SP_MediaPause

        else:
            icon = QStyle.SP_MediaPlay

        self.playBtn.setIcon(
            self.style().standardIcon(icon)
        )

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())

"""
app = QApplication(sys.argv)
window = Player('C:/Users/DeadlyComputer/Desktop/Super star/The World is Not Enough (1999).avi')
sys.exit(app.exec_())
"""