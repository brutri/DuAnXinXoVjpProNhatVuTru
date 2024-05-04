import sys
from math import sqrt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout # type: ignore

class GiaiPhuongTrinhBac2(QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):

    self.setWindowTitle("Giải phương trình bậc 2")

    self.label_a = QLabel("Hệ số a:")
    self.line_edit_a = QLineEdit()
    self.label_b = QLabel("Hệ số b:")
    self.line_edit_b = QLineEdit()
    self.label_c = QLabel("Hệ số c:")
    self.line_edit_c = QLineEdit()

    self.button_giai = QPushButton("Giải")
    self.button_giai.clicked.connect(self.giai_phuong_trinh)

    self.label_ket_qua = QLabel("")

    layout = QVBoxLayout()
    layout.addWidget(self.label_a)
    layout.addWidget(self.line_edit_a)
    layout.addWidget(self.label_b)
    layout.addWidget(self.line_edit_b)
    layout.addWidget(self.label_c)
    layout.addWidget(self.line_edit_c)
    layout.addWidget(self.button_giai)
    layout.addWidget(self.label_ket_qua)
    self.setLayout(layout)

  def giai_phuong_trinh(self):

    try:
      a = float(self.line_edit_a.text())
      b = float(self.line_edit_b.text())
      c = float(self.line_edit_c.text())
    except ValueError:
      self.label_ket_qua.setText("Vui lòng nhập số!")
      return


    if a == 0:
        if b == 0:
            if c == 0:
                self.label_ket_qua.setText("Phương trình vô số nghiệm!")
            else:
                self.label_ket_qua.setText("Phương trình vô nghiệm!")
        else:
            if c == 0:
                self.label_ket_qua.setText("Phương trình có 1 nghiệm x = 0")
            else:
                x = -c / b
                self.label_ket_qua.setText(f"Phương trình có 1 nghiệm x = {x}")
    else:
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            self.label_ket_qua.setText("Phương trình vô nghiệm!")
        elif delta == 0:
            x = -b / (2 * a)
            self.label_ket_qua.setText(f"Phương trình có 1 nghiệm x = {x} ")
        else:
            x1 =  float((-b - sqrt(delta)) / (2 * a))
            x2 =  float((-b + sqrt(delta)) / (2 * a))
            self.label_ket_qua.setText(f"Nghiệm thứ nhất: {x1:.2f}\nNghiệm thứ hai: {x2:.2f}")


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = GiaiPhuongTrinhBac2()
  window.show()
  sys.exit(app.exec_())
