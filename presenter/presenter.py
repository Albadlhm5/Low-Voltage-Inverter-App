from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFileDialog

from backend.inversor_simulado import InversorSimulado


class Presenter:
    """
    Actua com a pont entre la lògica i la pantalla.
    """

    def __init__(self, view, model: InversorSimulado):
        # La vista és la finestra i el model és l'inversor simulat
        self.vista = view
        self.modelo = model

        # Si MainWindow guarda la UI dins self.ui, la fem servir
        self.ui = view.ui if hasattr(view, "ui") else view

        # Timer de monitorització
        self.timer_stream = QTimer()
        self.timer_stream.setInterval(80)
        self.timer_stream.timeout.connect(self._tick_stream)

        # Timer d'identificació
        self.timer_identificacio = QTimer()
        self.timer_identificacio.setInterval(140)
        self.timer_identificacio.timeout.connect(self._tick_identificacio)

        # Dades temporals per a la gràfica
        self.x_data = []
        self.y1_data = []
        self.y2_data = []

        # Preparació inicial de la interfície
        self._preparar_ui()

        # Connexió de botons
        self._connectar_senyals()

        # Carreguem valors inicials
        self.fcarregar_defecto()
        self._registrar_log("Application ready.")

    # ------------------------------------------------------------
    # PREPARACIÓ INICIAL
    # ------------------------------------------------------------

    def _preparar_ui(self):
        """
        Omple els combos i deixa l'estat inicial preparat.
        """
        self._omplir_signals()
        self._omplir_modes()
        self._posar_estat_identificacio("Idle", 0)
        self._netejar_parametres_estimats()

    def _connectar_senyals(self):
        """
        Associa cada botó amb la seva funció del presenter.
        """
        # Bloc Parameters -> Actions
        self._widget("connectButton").clicked.connect(self.fconectar)
        self._widget("defaultsButton").clicked.connect(self.fcarregar_defecto)
        self._widget("disconnectButton").clicked.connect(self.fdesconectar)

        # Bloc Monitoring -> Stream Control
        self._widget("startButton").clicked.connect(self.finiciar_stream)
        self._widget("stopButton").clicked.connect(self.fparar_stream)
        self._widget("exportButton").clicked.connect(self.fexportar)

        # Bloc Identification Setup
        self._widget("runButton").clicked.connect(self.frun)
        self._widget("stopModeButton").clicked.connect(self.fstopcmd)

        # Bloc Actions de la dreta
        self._widget("startIdentificationButton").clicked.connect(self.finiciar_identificacion)
        self._widget("stopIdentificationButton").clicked.connect(self.fparar_identificacion)
        self._widget("applyParametersButton").clicked.connect(self.faplicar_parametros)

    # ------------------------------------------------------------
    # BOTONS DE L'ESQUERRA
    # ------------------------------------------------------------

    def fconectar(self):
        """
        Conecta l'inversor simulat.
        """
        try:
            parametres = self._llegir_parametres_de_la_vista()
            self.modelo.establir_parametres(parametres)
            self.modelo.conectar()
            self._registrar_log("Simulated inverter connected.")
        except Exception as e:
            self._registrar_log(f"ERROR: {e}")

    def fcarregar_defecto(self):
        """
        Carrega els valors per defecte del backend i els mostra a la vista.
        """
        try:
            parametres = self.modelo.carregar_defecte()
            self._escriure_parametres_a_la_vista(parametres)
            self._registrar_log("Default parameters loaded.")
        except Exception as e:
            self._registrar_log(f"ERROR: {e}")

    def fdesconectar(self):
        """
        Desconecta l'inversor i atura tots els processos actius.
        """
        self.timer_stream.stop()
        self.timer_identificacio.stop()
        self.modelo.desconectar()
        self._posar_estat_identificacio("Idle", 0)
        self._registrar_log("Inverter disconnected.")

    # ------------------------------------------------------------
    # MONITORING
    # ------------------------------------------------------------

    def finiciar_stream(self):
        """
        Inicia la monitorització de senyals.
        """
        try:
            if not self.modelo.connectat:
                raise RuntimeError("You need to connect the inverter before starting the stream.")

            parametres = self._llegir_parametres_de_la_vista()
            self.modelo.establir_parametres(parametres)

            self.x_data.clear()
            self.y1_data.clear()
            self.y2_data.clear()

            self.timer_stream.start()
            self._registrar_log("Streaming started.")
        except Exception as e:
            self._registrar_log(f"ERROR: {e}")

    def fparar_stream(self):
        """
        Atura la monitorització.
        """
        self.timer_stream.stop()
        self._registrar_log("Streaming aturat.")

    def fexportar(self):
        """
        Exporta l'historial de mostres a un CSV.
        """
        try:
            if not self.modelo.historial:
                raise RuntimeError("There is no data to export.")

            ruta, _ = QFileDialog.getSaveFileName(
                self.vista,
                "Exportar CSV",
                str(Path.home() / "mostres_inversor.csv"),
                "CSV (*.csv)",
            )

            if not ruta:
                return

            self.modelo.exportar_csv(ruta)
            self._registrar_log(f"Data exported to: {ruta}")
        except Exception as e:
            self._registrar_log(f"ERROR: {e}")

    # ------------------------------------------------------------
    # IDENTIFICATION SETUP (RUN / STOP)
    # ------------------------------------------------------------

    def frun(self):
        """
        Executa el mode seleccionat (Torque o Speed).
        """
        try:
            if not self.modelo.connectat:
                raise RuntimeError("You need to connect the inverter before running a mode.")

            mode = self._widget("modeComboBox").currentText()
            valor = self._widget("modeValueSpinBox").value()

            parametres = self._llegir_parametres_de_la_vista()
            self.modelo.establir_parametres(parametres)
            self.modelo.executar_mode(mode, valor)

            self._registrar_log(f"RUN activated. Mode={mode}, valor={valor}")
        except Exception as e:
            self._registrar_log(f"ERROR: {e}")

    def fstopcmd(self):
        """
        Atura el mode actiu del bloc superior dret.
        """
        self.modelo.parar_mode()
        self._registrar_log("Mode stopped.")

    # ------------------------------------------------------------
    # IDENTIFICATION ACTIONS
    # ------------------------------------------------------------

    def finiciar_identificacion(self):
        """
        Inicia la identificació del sistema.
        """
        try:
            self.modelo.iniciar_identificacio()
            self.timer_identificacio.start()
            self._posar_estat_identificacio("Running...", 0)
            self._registrar_log("Identification started.")
        except Exception as e:
            self._registrar_log(f"ERROR: {e}")

    def fparar_identificacion(self):
        """
        Atura la identificació.
        """
        self.modelo.parar_identificacio()
        self.timer_identificacio.stop()
        self._posar_estat_identificacio("Stopped", 0)
        self._registrar_log("Identification stopped.")

    def faplicar_parametros(self):
        """
        Aplica els paràmetres identificats sobre Kp i Ki.
        """
        try:
            parametres = self.modelo.aplicar_parametres_identificats()
            self._escriure_parametres_a_la_vista(parametres)
            self._registrar_log("Identified parameters applied.")
        except Exception as e:
            self._registrar_log(f"ERROR: {e}")

    # ------------------------------------------------------------
    # TICKS DELS TIMERS
    # ------------------------------------------------------------

    def _tick_stream(self):
        """
        Actualitza la simulació i llegeix dues senyals.
        """
        self.modelo.actualitzar(0.08)

        senyal1 = self._widget("signal1ComboBox").currentData()
        senyal2 = self._widget("signal2ComboBox").currentData()

        if senyal1 is None or senyal2 is None:
            return

        mostra = self.modelo.llegir_senyals(senyal1, senyal2)

        self.x_data.append(mostra["t"])
        self.y1_data.append(mostra["signal1_value"])
        self.y2_data.append(mostra["signal2_value"])

        if len(self.x_data) > 250:
            self.x_data.pop(0)
            self.y1_data.pop(0)
            self.y2_data.pop(0)

        self._actualitzar_grafica()

    def _tick_identificacio(self):
        """
        Fa avançar la identificació i actualitza la barra de progrés.
        """
        self.modelo.actualitzar(0.14)

        text_estat, progres = self.modelo.obtenir_estat_identificacio()
        self._posar_estat_identificacio(text_estat, progres)

        if progres >= 100:
            self.timer_identificacio.stop()
            self._escriure_parametres_estimats()
            self._registrar_log("Identification completed.")

    # ------------------------------------------------------------
    # AUXILIARS DE LECTURA / ESCRIPTURA
    # ------------------------------------------------------------

    def _llegir_parametres_de_la_vista(self) -> dict:
        """
        Llegeix tots els paràmetres de la part esquerra.
        """
        return {
            "dc_voltage": self._widget("dcVoltageSpinBox").value(),
            "current_limit_peak": self._widget("currentLimitPeakSpinBox").value(),
            "speed_limit": self._widget("speedLimitSpinBox").value(),
            "pole_pairs": self._widget("polePairsSpinBox").value(),
            "d_axis_current_ref": self._widget("dAxisCurrentRefSpinBox").value(),
            "q_axis_current_ref": self._widget("qAxisCurrentRefSpinBox").value(),
            "current_kp": self._widget("currentKpSpinBox").value(),
            "current_ki": self._widget("currentKiSpinBox").value(),
            "overcurrent_protection": self._widget("overcurrentProtectionSpinBox").value(),
            "overvoltage_protection": self._widget("overvoltageProtectionSpinBox").value(),
            "undervoltage_protection": self._widget("undervoltageProtectionSpinBox").value(),
            "temperature_limit": self._widget("temperatureLimitSpinBox").value(),
        }

    def _escriure_parametres_a_la_vista(self, p: dict):
        """
        Escriu els paràmetres del model sobre la UI.
        """
        self._widget("dcVoltageSpinBox").setValue(p["dc_voltage"])
        self._widget("currentLimitPeakSpinBox").setValue(p["current_limit_peak"])
        self._widget("speedLimitSpinBox").setValue(p["speed_limit"])
        self._widget("polePairsSpinBox").setValue(p["pole_pairs"])

        self._widget("dAxisCurrentRefSpinBox").setValue(p["d_axis_current_ref"])
        self._widget("qAxisCurrentRefSpinBox").setValue(p["q_axis_current_ref"])
        self._widget("currentKpSpinBox").setValue(p["current_kp"])
        self._widget("currentKiSpinBox").setValue(p["current_ki"])

        self._widget("overcurrentProtectionSpinBox").setValue(p["overcurrent_protection"])
        self._widget("overvoltageProtectionSpinBox").setValue(p["overvoltage_protection"])
        self._widget("undervoltageProtectionSpinBox").setValue(p["undervoltage_protection"])
        self._widget("temperatureLimitSpinBox").setValue(p["temperature_limit"])

    def _escriure_parametres_estimats(self):
        """
        Escriu Rs, Ld i Lq als LineEdit de la dreta.
        """
        self._widget("rsLineEdit").setText(f"{self.modelo.parametres_estimats.rs_mohm:.2f} mΩ")
        self._widget("ldLineEdit").setText(f"{self.modelo.parametres_estimats.ld_uH:.2f} µH")
        self._widget("lqLineEdit").setText(f"{self.modelo.parametres_estimats.lq_uH:.2f} µH")

    def _netejar_parametres_estimats(self):
        """
        Deixa buits els camps de Rs, Ld i Lq al començar.
        """
        self._widget("rsLineEdit").setText("")
        self._widget("ldLineEdit").setText("")
        self._widget("lqLineEdit").setText("")

    def _posar_estat_identificacio(self, text: str, progres: int):
        """
        Actualitza la label i la progressBar d'identificació.
        """
        self._widget("identificationStatusLabel").setText(text)
        self._widget("identificationProgressBar").setValue(progres)

    def _registrar_log(self, text: str):
        """
        Escriu missatges al log.
        """
        self._widget("logPlainTextEdit").appendPlainText(text)

    def _actualitzar_grafica(self):
        """
        Si tens pyqtgraph creat a main_window.py, actualitza les corbes.
        Si encara no tens gràfica real, això no fa res.
        """
        if hasattr(self.vista, "curve1") and hasattr(self.vista, "curve2"):
            self.vista.curve1.setData(self.x_data, self.y1_data)
            self.vista.curve2.setData(self.x_data, self.y2_data)

    # ------------------------------------------------------------
    # HELPERS
    # ------------------------------------------------------------

    def _widget(self, nom: str):
        """
        Retorna un widget segons el seu objectName.
        """
        widget = getattr(self.ui, nom, None)
        if widget is None:
            raise AttributeError(f"Widget not found: {nom}")
        return widget

    def _omplir_signals(self):
        """
        Omple els combos de Signals amb les opcions disponibles.
        """
        opcions = [
            ("Select Signal 1", None),
            ("Select Signal 2", None),
            ("DC Bus Voltage (V)", "vdc"),
            ("Phase A Current (A)", "ia"),
            ("Phase B Current (A)", "ib"),
            ("Phase C Current (A)", "ic"),
            ("d-axis Current (A)", "id"),
            ("q-axis Current (A)", "iq"),
            ("Speed (rpm)", "speed"),
            ("Torque (Nm)", "torque"),
            ("Temperature (°C)", "temperature"),
            ("Duty Cycle (%)", "duty"),
        ]

        combo1 = self._widget("signal1ComboBox")
        combo2 = self._widget("signal2ComboBox")

        combo1.clear()
        combo2.clear()

        for text, data in opcions:
            combo1.addItem(text, data)
            combo2.addItem(text, data)

    def _omplir_modes(self):
        """
        Omple el combo del mode superior dret.
        """
        combo = self._widget("modeComboBox")
        if combo.count() == 0:
            combo.addItems(["Torque", "Speed"])