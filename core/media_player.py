from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog, QButtonGroup
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt, QUrl
from app.db.models import Movies, Stars, Series
from app.db.models import session

class Player(QWidget):
    muted = False
    model = Movies
    auto_play=True
    full_screen=False
    session = session

    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1560, 300)
        from core.view import BaseView
        self.base_view = BaseView([], self)
        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

    def run_window(self):
        self.base_view.set_data(self.id)
        self.data = self.base_view.data
        self.init_ui()
        self.show()
        self.setWindowTitle(self.data.name)

    def set_star(self,stars,id):
        Star=None
        for star_array in stars:
            if star_array.id == id:
                Star=star_array
        return Star

    def set_player(self):
        if self.muted:
            self.mute_clicked()
        if self.auto_play:
            self.play_video()
        if self.full_screen:
            self.full_screen_switch()

    def init_ui(self):
        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.data.src)))
        # create videowidget object

        videowidget = QVideoWidget()

        self.playBtn = QPushButton()
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        self.show_full_screen_button = QPushButton('Full Screen')
        self.show_full_screen_button.clicked.connect(self.full_screen_switch)

        self.movie_info_button = QPushButton('Movie')
        self.movie_info_button.clicked.connect(self.movie_info)

        if self.data.series:
            self.series_info_button = QPushButton('Series')
            self.series_info_button.clicked.connect(self.series_info)

        self.mute = QPushButton()
        self.mute.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))
        self.mute.clicked.connect(self.mute_clicked)

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
        hboxLayout.addWidget(self.movie_info_button)

        if self.data.series:
            hboxLayout.addWidget(self.series_info_button)
        hboxLayout.addWidget(self.show_full_screen_button)
        self.set_player()

        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setContentsMargins(10, 10, 10, 10)

        self.buttons_stars = QButtonGroup()
        self.buttons_series = QButtonGroup()

        self.add_grup_movies_buttons()
        # create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addLayout(self.hboxLayout2)
        vboxLayout.addWidget(self.label)

        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(videowidget)

        # media player signals

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

    def closeEvent(self, QCloseEvent):
        self.mediaPlayer.stop()

    def series_info(self):
        self.base_view.load_view('series', self.data.series[0])

    def movie_info(self):
        self.base_view.load_view('movies', self.data.series[0])

    def buttom_genarator(self, list, fuction, id):
        for button in list.buttons():
            if button is list.button(id):
                fuction(button.data)

    def on_movies_series_play(self, id):
        self.buttom_genarator(self.buttons_series, self.next_series, id)

    def on_movies_star_play(self, id):
        self.buttom_genarator(self.buttons_stars, self.next_star, id)

    def add_grup_movies_buttons(self):
        self.button_series = [
            {'button': self.on_movies_series_play, 'obejct': self.buttons_series},
        ]

        index = 0
        for series in self.data.series:
            button = QPushButton('next video in series ' + str(series))
            self.hboxLayout2.addWidget(button)
            button.data = series
            self.button_series[0]['obejct'].addButton(button)
            self.button_series[0]['obejct'].buttonClicked[int].connect(self.button_series[0]['button'])
            index = index + 1

        self.buttons_star = [
            {'button': self.on_movies_star_play, 'obejct': self.buttons_stars},
        ]

        index = 0
        for star in self.data.stars:
            if len(star.movies)>3:
                button = QPushButton('next video with star ' + str(star))
                self.hboxLayout2.addWidget(button)
                button.data = star
                self.buttons_star[0]['obejct'].addButton(button)
                self.buttons_star[0]['obejct'].buttonClicked[int].connect(self.buttons_star[0]['button'])
            index = index + 1

    def mute_clicked(self):
        if self.mediaPlayer.isMuted() is False:
            icon = QStyle.SP_MediaVolumeMuted
            self.mediaPlayer.setMuted(True)
        else:
            icon = QStyle.SP_MediaVolume
            self.mediaPlayer.setMuted(False)

        self.mute.setIcon(self.style().standardIcon(icon))

    def next_series(self, series):
        movies_in_series = self.data.series[0].movies
        self.close()
        self.base_view.load_view('play', self.faind_item(movies_in_series))

    def next_star(self, star):
        star = self.set_star(self.data.stars,star.id)
        movies_with_star=star.movies
        self.close()
        self.base_view.load_view('play', self.faind_item(movies_with_star))

    def faind_item(self, array):
        def faind_item_greater_then_actual_item(array, math_index):
            index_item = 0
            for item in array:
                if index_item > math_index:
                    return index_item
                elif math_index == len(array) - 1:
                    return 0
                index_item = index_item + 1
        math_index = ''
        index_in_array = 0;
        for item in array:
            if self.data.id == item.id:
                math_index = index_in_array;
            index_in_array = index_in_array + 1;

        next_item = faind_item_greater_then_actual_item(array, math_index)
        return array[next_item]

    def full_screen_switch(self):
        if self.isFullScreen() is False:
            self.showFullScreen()
        else:
            self.showNormal()

    def mute_switch(self):
        self.changeMuting.emit(not self.muted)

    def play_video(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            icon = QStyle.SP_MediaPause

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