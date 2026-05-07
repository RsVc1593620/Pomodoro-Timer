import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QSystemTrayIcon,
    QMenu,
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QSoundEffect
from qt_material import apply_stylesheet
from circular_timer import CircularTimer
from PyQt6.QtGui import QIcon
import ctypes
import platform

if platform.system() == "Windows":

    myappid = "stelian.pomodoro.timer.1.0"

    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

WORK_TIME = 30 * 60
BREAK_TIME = 10 * 60


class PomodoroApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pomodoro Timer")
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.setFixedSize(300, 260)

        self.time_left = WORK_TIME
        self.is_running = False
        self.is_work = True

        self.init_ui()
        self.setup_tray()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

    def init_ui(self):
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile("assets/ding.wav"))

        self.sound.setVolume(0.8)
        self.timer_widget = CircularTimer()

        self.status = QLabel("Work")
        self.status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.start_btn = QPushButton("Start")
        self.start_btn.clicked.connect(self.start)

        self.pause_btn = QPushButton("Pause")
        self.pause_btn.clicked.connect(self.pause)

        self.reset_btn = QPushButton("Reset")
        self.reset_btn.clicked.connect(self.reset)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.pause_btn)
        btn_layout.addWidget(self.reset_btn)

        layout = QVBoxLayout()
        layout.addWidget(self.timer_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def setup_tray(self):

        self.tray = QSystemTrayIcon(self)

        self.tray.setIcon(QIcon("assets/icon.png"))

        menu = QMenu()

        start_action = menu.addAction("Start")
        pause_action = menu.addAction("Pause")
        reset_action = menu.addAction("Reset")

        menu.addSeparator()

        exit_action = menu.addAction("Exit")

        start_action.triggered.connect(self.start)

        pause_action.triggered.connect(self.pause)

        reset_action.triggered.connect(self.reset)

        exit_action.triggered.connect(self.quit_app)

        self.tray.activated.connect(self.toggle_window)

        self.tray.setContextMenu(menu)

        self.tray.show()

    def quit_app(self):

        self.tray.hide()

        QApplication.quit()

    def toggle_window(self):

        if self.isVisible():
            self.hide()

        else:
            self.show()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_display()
        else:
            self.switch_mode()

    def update_display(self):
        mins, secs = divmod(self.time_left, 60)

        self.timer_widget.set_time(f"{mins:02d}:{secs:02d}")

        if self.is_work:
            total = WORK_TIME
        else:
            total = BREAK_TIME

        progress = (self.time_left / total) * 100

        self.timer_widget.set_progress(progress)

    def switch_mode(self):
        self.sound.play()
        self.show()
        self.raise_()
        self.activateWindow()
        self.timer.stop()
        self.is_running = False

        if self.is_work:
            self.time_left = BREAK_TIME
            self.status.setText("Break")
        else:
            self.time_left = WORK_TIME
            self.status.setText("Work")

        self.is_work = not self.is_work
        self.update_display()

    def start(self):
        if not self.is_running:
            self.timer.start(1000)
            self.is_running = True

    def pause(self):
        self.timer.stop()
        self.is_running = False

    def reset(self):
        self.timer.stop()
        self.is_running = False
        self.is_work = True
        self.time_left = WORK_TIME
        self.status.setText("Work")
        self.update_display()

    def closeEvent(self, event):

        event.ignore()

        self.hide()

        self.tray.showMessage("Pomodoro Timer", "Application minimized to tray.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_teal.xml", invert_secondary=True)
    window = PomodoroApp()
    window.show()
    sys.exit(app.exec())
