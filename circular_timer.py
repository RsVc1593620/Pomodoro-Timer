from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen, QColor, QFont
from PyQt6.QtCore import Qt, QRectF


class CircularTimer(QWidget):

    def __init__(self):
        super().__init__()

        self.progress = 100
        self.minutes = "25:00"

        self.setFixedSize(180, 180)

    def set_time(self, text):
        self.minutes = text
        self.update()

    def set_progress(self, value):
        self.progress = value
        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        outer_rect = QRectF(10, 10, 160, 160)

        progress_rect = QRectF(15, 15, 150, 150)

        # outer ring
        pen = QPen(QColor("#4989c9"))
        pen.setWidth(15)
        pen.setCapStyle(Qt.PenCapStyle.FlatCap)

        painter.setPen(pen)

        painter.drawEllipse(outer_rect)

        # progress
        pen = QPen(QColor("#00ffd0"))
        pen.setWidth(5)
        pen.setCapStyle(Qt.PenCapStyle.FlatCap)

        painter.setPen(pen)

        angle = 360 * self.progress / 100

        painter.drawArc(
            progress_rect,
            90 * 16,
            int(-angle * 16)
        )

        # text
        painter.setPen(Qt.GlobalColor.white)

        font = QFont()
        font.setPointSize(24)
        font.setBold(True)

        painter.setFont(font)

        painter.drawText(
            self.rect(),
            Qt.AlignmentFlag.AlignCenter,
            self.minutes
        )