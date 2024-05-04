import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton # type: ignore
import subprocess

class ProgramChooser(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Program Chooser')

        layout = QHBoxLayout()

        button1 = QPushButton('Giải phương trình bậc 1', self)
        button1.clicked.connect(self.runFirstDegreeProgram)

        button2 = QPushButton('Giải phương trình bậc 2', self)
        button2.clicked.connect(self.runSecondDegreeProgram)

        layout.addWidget(button1)
        layout.addWidget(button2)

        self.setLayout(layout)

    def runFirstDegreeProgram(self):
        subprocess.call(['python', 'ptbac1.py'])

    def runSecondDegreeProgram(self):
        subprocess.call(['python', 'ptbac2.py'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProgramChooser()
    ex.show()
    sys.exit(app.exec_())
