import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton # type: ignore


class LinearEquationSolver(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Giải phương trình bậc 1')

        label_a = QLabel('Nhập hệ số a: ', self)
        label_a.setGeometry(20, 20, 120, 20)
        self.input_a = QLineEdit(self)
        self.input_a.setGeometry(140, 20, 50, 20)

        label_b = QLabel('NHập hệ số b: ', self)
        label_b.setGeometry(20, 50, 120, 20)
        self.input_b = QLineEdit(self)
        self.input_b.setGeometry(140, 50, 50, 20)

        solve_button = QPushButton('Giải', self)
        solve_button.setGeometry(130, 80, 70, 25)
        solve_button.clicked.connect(self.solve_equation)

        self.solution_label = QLabel('', self)
        self.solution_label.setGeometry(100, 80, 200, 25)

        self.show()

    def solve_equation(self):
        try:
            a = float(self.input_a.text())
            b = float(self.input_b.text())

            if a == 0:
                self.solution_label.setText('Lỗi: Hệ số a không thể bằng 0.')
                return

            solution = -b / a

            # Display the solution
            self.solution_label.setText(f'Nghiệm: x = {solution:.2f}')
        except ValueError:
            # Handle invalid input (non-numeric values)
            self.solution_label.setText('Lỗi: Vui lòng nhập số!.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LinearEquationSolver()
    sys.exit(app.exec_())
