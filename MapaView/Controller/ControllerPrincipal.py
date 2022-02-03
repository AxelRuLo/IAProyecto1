from MapaView.Controller.ControllerMapaRuta import ControllerMapaRuta
from MapaView.Controller.ControllerMapeo import ControllerMapeo
from MapaView.Views.Ui_Principal import Ui_MainWindow

from generacionInicial import algoritmogenetico
from PyQt5.QtWidgets import QMainWindow


class ControllerPrincipal(QMainWindow):
    def __init__(self):
        super(ControllerPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_Mapa_Ruta.setEnabled(False)
        self.ui.pushButton_Mapa_Ruta.clicked.connect(self.vistaMapa)
        self.ui.pushButton_Recibir_pedidos.clicked.connect(self.algoritmo)
        self.ui.pushButton_Mapeo.clicked.connect(self.vistaMapeo)
    def vistaMapa(self):
        self.vista = ControllerMapaRuta()
        self.vista.show()
        
    def algoritmo(self):
        bandera = algoritmogenetico()
        if(bandera):
            self.ui.pushButton_Mapa_Ruta.setEnabled(True)
            
    def vistaMapeo(self):
        self.vista = ControllerMapeo()
        self.vista.show()
        
            
        