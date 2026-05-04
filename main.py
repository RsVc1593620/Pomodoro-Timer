import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtCore import QTimer, Qt
from qt_material import apply_stylesheet
from circular_timer import CircularTimer


WORK_TIME = 25 * 60
BREAK_TIME = 5 * 60

class PomodoroApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pomodoro Timer")
        self.setFixedSize(300, 260)

        self.time_left = WORK_TIME
        self.is_running = False
        self.is_work = True

        self.init_ui()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

    def init_ui(self):
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
        layout.addWidget(self.timer_widget,
                         alignment=Qt.AlignmentFlag.AlignCenter
                         )
        layout.addWidget(self.status)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_display()
        else:
            self.switch_mode()

    def update_display(self):
        mins, secs = divmod(
            self.time_left,
            60
        )

        self.timer_widget.set_time(
            f"{mins:02d}:{secs:02d}"
        )

        if self.is_work:
            total = WORK_TIME
        else:
            total = BREAK_TIME

        progress = (
            self.time_left / total
        ) * 100

        self.timer_widget.set_progress(
            progress
        )

    def switch_mode(self):
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml', invert_secondary=True)
    window = PomodoroApp()
    window.show()
    sys.exit(app.exec())