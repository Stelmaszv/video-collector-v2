from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog,QToolButton
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl,pyqtSignal


class Player(QWidget):

    file_name='C:/Users/DeadlyComputer/Desktop/Super star/The World is Not Enough (1999).avi'
    playerMuted = False

    def __init__(self):
        super().__init__()

        self.setWindowTitle("The World is Not Enough (1999)")
        self.setGeometry(0, 0, 2560 , 1300)
        self.setWindowIcon(QIcon('player.png'))

        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        self.init_ui()

        self.show()

    def init_ui(self):

        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

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

        self.next_video_in_series = QPushButton('next video in series')
        self.next_video_in_series.clicked.connect(self.next_series)

        self.next_video_with_star = QPushButton('next video with star')
        self.next_video_with_star.clicked.connect(self.next_star)

        hboxLayout2 = QHBoxLayout()
        hboxLayout2.setContentsMargins(10, 10, 10, 10)
        hboxLayout2.addWidget(self.next_video_in_series)
        hboxLayout2.addWidget(self.next_video_with_star)

        # create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addLayout(hboxLayout2)
        vboxLayout.addWidget(self.label)

        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(videowidget)

        if self.file_name:
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.file_name)))
            self.playBtn.setEnabled(True)
            self.mediaPlayer.play()

        # media player signals

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

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

    def next_star(self):
        print('star')

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


app = QApplication(sys.argv)
window = Player()
sys.exit(app.exec_())