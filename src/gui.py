from sys import exit
from PyQt5.QtWidgets import QApplication, QWidget


def main():
    app = QApplication([''])
    w = QWidget()
    w.resize(600, 250)
    w.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()