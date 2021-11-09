import sqlite3
import sys

from PyQt5.QtCore import Qt, QSize, QUrl
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QCheckBox, QLineEdit

links_full = ("""SELECT full, short, title FROM books WHERE id = 1""",
              """SELECT full, short, title FROM books WHERE id = 2""",
              """SELECT full, short, title FROM books WHERE id = 3""",
              """SELECT full, short, title FROM books WHERE id = 4""",
              """SELECT full, short, title FROM books WHERE id = 5""",
              """SELECT full, short, title FROM books WHERE id = 6""",
              """SELECT full, short, title FROM books WHERE id = 7""",
              """SELECT full, short, title FROM books WHERE id = 8""",
              """SELECT full, short, title FROM books WHERE id = 9""",
              """SELECT full, short, title FROM books WHERE id = 10""",
              """SELECT full, short, title FROM books WHERE id = 11""",
              """SELECT full, short, title FROM books WHERE id = 12""",
              """SELECT full, short, title FROM books WHERE id = 13""",
              """SELECT full, short, title FROM books WHERE id = 14""",
              """SELECT full, short, title FROM books WHERE id = 15""",
              """SELECT full, short, title FROM books WHERE id = 16""")

last = ("""UPDATE diary SET book = (SELECT title FROM books WHERE id = 1) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 2) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 3) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 4) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 5) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 6) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 7) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 8) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 9) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 10) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 11) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 12) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 13) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 14) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 15) WHERE id = 1""",
        """UPDATE diary SET book = (SELECT title FROM books WHERE id = 16) WHERE id = 1""")

btn_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.title = QLabel(self)
        self.line1 = QLineEdit(self)
        self.label2 = QLabel(self)
        self.label1 = QLabel(self)
        self.webEngineView = QWebEngineView()
        self.st = False
        self.book_buttons = []
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 220, 1050, 1000)
        self.setWindowTitle('Библиотека для ЕГЭ')

        for i in range(16):
            btn = QPushButton(self)
            btn.setText(btn_names[i])
            self.book_buttons.append(btn)
            self.book_buttons[i].clicked.connect(self.open_webbrowser)

        self.book_buttons[0].resize(130, 170)
        self.book_buttons[0].move(75, 115)
        self.book_buttons[0].setIcon(
            QIcon('/Users/nikitochka/Desktop/обложки для проекта/преступление и наказание.jpg'))
        self.book_buttons[0].setIconSize(QSize(230, 210))

        self.book_buttons[1].resize(130, 170)
        self.book_buttons[1].move(220, 115)
        self.book_buttons[1].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/капитанская дочка.jpg'))
        self.book_buttons[1].setIconSize(QSize(230, 210))

        self.book_buttons[2].resize(130, 170)
        self.book_buttons[2].move(365, 115)
        self.book_buttons[2].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/отцы и дети.jpg'))
        self.book_buttons[2].setIconSize(QSize(230, 210))

        self.book_buttons[3].resize(130, 170)
        self.book_buttons[3].move(510, 115)
        self.book_buttons[3].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/война и мир.jpg'))
        self.book_buttons[3].setIconSize(QSize(230, 210))

        self.book_buttons[4].resize(130, 170)
        self.book_buttons[4].move(75, 325)
        self.book_buttons[4].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/гроза.jpg'))
        self.book_buttons[4].setIconSize(QSize(230, 210))

        self.book_buttons[5].resize(130, 170)
        self.book_buttons[5].move(220, 325)
        self.book_buttons[5].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/451 градус.jpg'))
        self.book_buttons[5].setIconSize(QSize(230, 210))

        self.book_buttons[6].resize(130, 170)
        self.book_buttons[6].move(365, 325)
        self.book_buttons[6].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/гордость и ....jpg'))
        self.book_buttons[6].setIconSize(QSize(230, 210))

        self.book_buttons[7].resize(130, 170)
        self.book_buttons[7].move(510, 325)
        self.book_buttons[7].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/судьба ечловека.jpg'))
        self.book_buttons[7].setIconSize(QSize(230, 210))

        self.book_buttons[8].resize(130, 170)
        self.book_buttons[8].move(75, 535)
        self.book_buttons[8].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/герой нашего времени.jpg'))
        self.book_buttons[8].setIconSize(QSize(230, 210))

        self.book_buttons[9].resize(130, 170)
        self.book_buttons[9].move(220, 535)
        self.book_buttons[9].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/горе уот ума.jpg'))
        self.book_buttons[9].setIconSize(QSize(230, 210))

        self.book_buttons[10].resize(130, 170)
        self.book_buttons[10].move(365, 535)
        self.book_buttons[10].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/мастер и маргарита.png'))
        self.book_buttons[10].setIconSize(QSize(230, 210))

        self.book_buttons[11].resize(130, 170)
        self.book_buttons[11].move(510, 535)
        self.book_buttons[11].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/мертвые души.jpg'))
        self.book_buttons[11].setIconSize(QSize(230, 210))

        self.book_buttons[12].resize(130, 170)
        self.book_buttons[12].move(75, 745)
        self.book_buttons[12].setIcon(
            QIcon('/Users/nikitochka/Desktop/обложки для проекта/Господин из Сан Франциско.png'))
        self.book_buttons[12].setIconSize(QSize(230, 210))

        self.book_buttons[13].resize(130, 170)
        self.book_buttons[13].move(220, 745)
        self.book_buttons[13].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/Обломов.jpg'))
        self.book_buttons[13].setIconSize(QSize(230, 210))

        self.book_buttons[14].resize(130, 170)
        self.book_buttons[14].move(365, 745)
        self.book_buttons[14].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/Гранатовый браслет.jpg'))
        self.book_buttons[14].setIconSize(QSize(230, 210))

        self.book_buttons[15].resize(130, 170)
        self.book_buttons[15].move(510, 745)
        self.book_buttons[15].setIcon(QIcon('/Users/nikitochka/Desktop/обложки для проекта/На дне.jpg'))
        self.book_buttons[15].setIconSize(QSize(230, 210))

        self.label1.setText('Доступные для прочтения книги:')
        self.label1.move(80, 50)
        self.label1.setStyleSheet("background-color: yellow;")
        self.label1.setStyleSheet("QLabel{font-size: 30pt;}")

        self.label2.setText('Последний раз вы открывали:')
        self.label2.move(700, 600)
        self.label2.setStyleSheet("background-color: yellow;")
        self.label2.setStyleSheet("QLabel{font-size: 20pt;}")

        self.line1.move(700, 630)
        self.line1.resize(320, 30)

        status = QCheckBox('краткое содержание', self)
        status.move(700, 75)
        status.stateChanged.connect(self.changeStatus)
        status.setStyleSheet("QLabel{font-size: 10pt;}")

        con = sqlite3.connect('/Users/nikitochka/Desktop/mybd.db')
        cur = con.cursor()
        self.line1.setText(cur.execute("""SELECT book FROM diary WHERE id = 1""").fetchone()[0])

        self.title.setText('Доступные книги:')
        self.title.move(700, 150)
        self.title.setStyleSheet("QLabel{font-size: 20pt;}")

        for i in range(16):
            title = cur.execute(links_full[i]).fetchall()[0][2]
            book = QLabel(self)
            book.move(700, 190 + 20 * i)
            book.setStyleSheet("QLabel{font-size: 11pt;}")
            s = f"{i + 1}) {title}"
            book.setText(s)

        Example.setStyleSheet(self, "background-color: #F5F5DC;")

    def changeStatus(self, state):
        if state == Qt.Checked:
            self.st = True
        else:
            self.st = False

    def open(self, a):
        self.webEngineView.load(QUrl(a))
        self.webEngineView.show()

    def open_webbrowser(self):
        n = 0
        con = sqlite3.connect('/Users/nikitochka/Desktop/mybd.db')
        cur = con.cursor()
        for num in btn_names:
            if num == self.sender().text():
                n = btn_names.index(num)
        full = cur.execute(links_full[n]).fetchall()[0][0]
        short = cur.execute(links_full[n]).fetchall()[0][1]
        if not self.st:
            self.open(full)
        else:
            self.open(short)
        cur.execute(last[n])
        con.commit()
        self.line1.setText(cur.execute("""SELECT book FROM diary WHERE id = 1""").fetchone()[0])


StyleSheet = '''
QCheckBox {
    spacing: 5px;
    font-size:25px;     
}

QCheckBox::indicator {
    width:  33px;
    height: 33px;
}
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.setStyle("fusion")
    app.setStyleSheet(StyleSheet)
    ex.show()
    sys.exit(app.exec())
