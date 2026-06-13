from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from pantalla.ui_main_window import Ui_MainWindow
import pyqtgraph as pg


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Crear la gràfica dins del plotFrame
        self._crear_grafica()

    def _crear_grafica(self):
        """
        Crea el widget de pyqtgraph dins del contenidor del Plot Area.
        """

        # Layout dins del frame del plot
        self.plot_layout = QVBoxLayout(self.ui.plotFrame)
        self.plot_layout.setContentsMargins(0, 0, 0, 0)

        # Widget principal de la gràfica
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground("w")
        self.plot_widget.showGrid(x=True, y=True)

        # Etiquetes dels eixos
        self.plot_widget.setLabel("left", "Valor")
        self.plot_widget.setLabel("bottom", "Temps", units="s")

        # Llegenda
        self.plot_widget.addLegend()

        # Corbes
        self.curve1 = self.plot_widget.plot(
            [],
            [],
            pen=pg.mkPen(color=(0, 114, 189), width=2),
            name="Signal 1"
        )

        self.curve2 = self.plot_widget.plot(
            [],
            [],
            pen=pg.mkPen(color=(217, 83, 25), width=2),
            name="Signal 2"
        )

        self.plot_layout.addWidget(self.plot_widget)