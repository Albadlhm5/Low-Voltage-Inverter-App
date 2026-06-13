from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import csv
import math
import random


@dataclass
class ParametresEstimats:
    """
    Guarda els resultats de la identificació.
    """

    rs_mohm: float = 0.0
    ld_uH: float = 0.0
    lq_uH: float = 0.0


class InversorSimulado:
    """
    Aquesta classe simula un inversor trifàsic de baixa tensió.

    La idea és que la interfície pugui funcionar encara que no hi hagi
    un inversor físic connectat.
    """

    def __init__(self):
        """
        Inicialitza l'estat intern del sistema.
        """

        # Estat general
        self.connectat = False
        self.executant = False
        self.identificant = False

        # Variables de funcionament
        self.mode = "Torque"
        self.valor_objectiu = 0.0
        self.temps = 0.0

        # Variables simulades
        self.velocitat_rpm = 0.0
        self.parell_nm = 0.0
        self.temperatura = 25.0
        self.duty = 0.0

        # Resultats de la identificació
        self.parametres_estimats = ParametresEstimats()
        self.progres_identificacio = 0

        # Historial per exportar
        self.historial = []

        # Carregar paràmetres per defecte
        self.parametres = self.carregar_defecte()

    def carregar_defecte(self) -> dict:
        """
        Carrega un conjunt de valors inicials.

        Returns
        -------
        dict
            Diccionari amb els paràmetres per defecte.
        """
        self.parametres = {
            "dc_voltage": 48.0,
            "current_limit_peak": 40.0,
            "speed_limit": 3000.0,
            "pole_pairs": 4.0,
            "d_axis_current_ref": 0.0,
            "q_axis_current_ref": 0.0,
            "current_kp": 2.5,
            "current_ki": 120.0,
            "overcurrent_protection": 60.0,
            "overvoltage_protection": 55.0,
            "undervoltage_protection": 35.0,
            "temperature_limit": 90.0,
        }
        return dict(self.parametres)

    def establir_parametres(self, nous_parametres: dict):
        """
        Actualitza els paràmetres interns del model.

        Parameters
        ----------
        nous_parametres : dict
            Paràmetres llegits des de la interfície.
        """
        self.parametres.update(nous_parametres)

    def conectar(self) -> bool:
        """
        Simula la connexió de l'inversor.

        Returns
        -------
        bool
            True si la connexió ha anat bé.
        """
        self.connectat = True
        return True

    def desconectar(self):
        """
        Simula la desconnexió de l'inversor.
        """
        self.connectat = False
        self.executant = False
        self.identificant = False
        self.velocitat_rpm = 0.0
        self.parell_nm = 0.0
        self.duty = 0.0
        self.progres_identificacio = 0

    def executar_mode(self, mode: str, valor_objectiu: float):
        """
        Activa el sistema en mode Torque o Speed.

        Parameters
        ----------
        mode : str
            Pot ser 'Torque' o 'Speed'.
        valor_objectiu : float
            Valor objectiu del mode seleccionat.
        """
        if not self.connectat:
            raise RuntimeError("L'inversor no està connectat.")

        self.mode = mode
        self.valor_objectiu = max(0.0, valor_objectiu)
        self.executant = True

    def parar_mode(self):
        """
        Atura l'execució del mode actiu.
        """
        self.executant = False
        self.valor_objectiu = 0.0

    def iniciar_identificacio(self):
        """
        Inicia la rutina d'identificació.
        """
        if not self.connectat:
            raise RuntimeError("Cal conectar l'inversor abans d'identificar.")

        self.identificant = True
        self.progres_identificacio = 0

    def parar_identificacio(self):
        """
        Atura la identificació.
        """
        self.identificant = False

    def aplicar_parametres_identificats(self) -> dict:
        """
        Aplica els paràmetres identificats sobre Kp i Ki.

        Returns
        -------
        dict
            Diccionari actualitzat de paràmetres.
        """
        if self.parametres_estimats.rs_mohm <= 0.0:
            raise RuntimeError("Encara no hi ha resultats d'identificació.")

        self.parametres["current_kp"] = round(self.parametres_estimats.ld_uH / 100.0, 2)
        self.parametres["current_ki"] = round(self.parametres_estimats.rs_mohm * 3.0, 2)

        return dict(self.parametres)

    def actualitzar(self, dt: float = 0.1):
        """
        Fa avançar la simulació un pas de temps.

        Parameters
        ----------
        dt : float
            Increment de temps en segons.
        """
        self.temps += dt

        if self.executant:
            if self.mode == "Torque":
                self.parell_nm += (self.valor_objectiu - self.parell_nm) * 0.15
                self.velocitat_rpm += ((200 + self.parell_nm * 50) - self.velocitat_rpm) * 0.10
            else:
                self.velocitat_rpm += (self.valor_objectiu - self.velocitat_rpm) * 0.10
                self.parell_nm += ((self.velocitat_rpm / 500.0) - self.parell_nm) * 0.10
        else:
            self.velocitat_rpm *= 0.95
            self.parell_nm *= 0.90

        # Simulació simple del duty i la temperatura
        self.duty = max(0.0, min(95.0, self.velocitat_rpm / 40.0 + self.parell_nm))
        self.temperatura += ((25.0 + abs(self.parell_nm) * 0.4) - self.temperatura) * 0.05

        # Simulació de la identificació
        if self.identificant:
            self.progres_identificacio += random.randint(2, 6)

            if self.progres_identificacio >= 100:
                self.progres_identificacio = 100
                self.identificant = False

                rs = 20.0 + random.uniform(-2.0, 2.0)
                ld = 150.0 + random.uniform(-10.0, 10.0)
                lq = 170.0 + random.uniform(-10.0, 10.0)

                self.parametres_estimats = ParametresEstimats(
                    rs_mohm=round(rs, 2),
                    ld_uH=round(ld, 2),
                    lq_uH=round(lq, 2),
                )

    def obtenir_estat_identificacio(self) -> tuple[str, int]:
        """
        Retorna l'estat textual i el progrés de la identificació.

        Returns
        -------
        tuple[str, int]
            Text d'estat i percentatge.
        """
        if self.identificant:
            return "Running...", self.progres_identificacio

        if self.progres_identificacio >= 100:
            return "Completed", 100

        return "Idle", 0

    def llegir_senyals(self, senyal1: str, senyal2: str) -> dict:
        """
        Retorna una mostra de dues senyals escollides.

        Parameters
        ----------
        senyal1 : str
            Nom de la primera senyal.
        senyal2 : str
            Nom de la segona senyal.

        Returns
        -------
        dict
            Diccionari amb el temps i els dos valors.
        """
        valors = {
            "vdc": self._vdc(),
            "ia": self._ia(),
            "ib": self._ib(),
            "ic": self._ic(),
            "id": self._id(),
            "iq": self._iq(),
            "speed": round(self.velocitat_rpm, 2),
            "torque": round(self.parell_nm, 2),
            "temperature": round(self.temperatura, 2),
            "duty": round(self.duty, 2),
        }

        mostra = {
            "t": round(self.temps, 3),
            "signal1_name": senyal1,
            "signal1_value": valors.get(senyal1, 0.0),
            "signal2_name": senyal2,
            "signal2_value": valors.get(senyal2, 0.0),
        }

        self.historial.append(mostra)
        return mostra

    def exportar_csv(self, ruta: str | Path):
        """
        Desa l'historial de mostres en un fitxer CSV.

        Parameters
        ----------
        ruta : str | Path
            Ruta on es guardarà el fitxer.
        """
        ruta = Path(ruta)

        with ruta.open("w", newline="", encoding="utf-8") as fitxer:
            escriptor = csv.DictWriter(
                fitxer,
                fieldnames=["t", "signal1_name", "signal1_value", "signal2_name", "signal2_value"],
            )
            escriptor.writeheader()
            escriptor.writerows(self.historial)

    def _vdc(self) -> float:
        """
        Simula la tensió del bus DC amb una mica de ripple.
        """
        ripple = 0.5 * math.sin(self.temps * 10.0)
        return round(self.parametres["dc_voltage"] + ripple, 3)

    def _ia(self) -> float:
        """
        Simula el corrent de fase A.
        """
        amplitud = max(1.0, abs(self.parell_nm) * 0.8 + 2.0)
        return round(amplitud * math.sin(self.temps * 4.0) + random.uniform(-0.2, 0.2), 3)

    def _ib(self) -> float:
        """
        Simula el corrent de fase B.
        """
        amplitud = max(1.0, abs(self.parell_nm) * 0.8 + 2.0)
        return round(amplitud * math.sin(self.temps * 4.0 - 2.0), 3)

    def _ic(self) -> float:
        """
        Simula el corrent de fase C.
        """
        amplitud = max(1.0, abs(self.parell_nm) * 0.8 + 2.0)
        return round(amplitud * math.sin(self.temps * 4.0 + 2.0), 3)

    def _id(self) -> float:
        """
        Simula el corrent d'eix directe.
        """
        return round(self.parametres["d_axis_current_ref"] + 0.2 * math.sin(self.temps * 2.0), 3)

    def _iq(self) -> float:
        """
        Simula el corrent d'eix en quadratura.
        """
        return round(self.parametres["q_axis_current_ref"] + self.parell_nm * 0.5, 3)