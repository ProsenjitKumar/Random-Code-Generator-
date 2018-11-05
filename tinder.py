import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class Tinder(QDialog):
    def __int__(self):
        super(Tinder, self).__init__()
        loadUi('tinder_color.ui', self)
        self.setWindowTitle("Find Out Tinder Token")
        self.pushButton.clicked.connect(self.on_pushButton_clocked)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label_3.setText('Welcome :', +self.lineEdit.text())


app = QApplication(sys.argv)
widget = Tinder()
widget.show()
sys.exit(app.exec_())