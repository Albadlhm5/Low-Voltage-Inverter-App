import sys
from PySide6.QtWidgets import QApplication

from pantalla.main_window import MainWindow
from backend.inversor_simulado import InversorSimulado
from presenter.presenter import Presenter


def main():
    app = QApplication(sys.argv)

    vista = MainWindow()
    modelo = InversorSimulado()
    presenter = Presenter(vista, modelo)

    vista.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()