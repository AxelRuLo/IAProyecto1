from MapaView.Controller.ControllerMapaRuta import ControllerMapaRuta
from MapaView.Controller.ControllerMapeo import ControllerMapeo
from MapaView.Views.Ui_Principal import Ui_MainWindow

from generacionInicial import algoritmogenetico, cleanPedidos,pedidos_table
from PyQt5.QtWidgets import QMainWindow,QTableWidgetItem

from mapa import cleanRutas


class ControllerPrincipal(QMainWindow):
    def __init__(self):
        super(ControllerPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.tables = [self.ui.table_Pedidos]
        self.ui.pushButton_Mapa_Ruta.setEnabled(False)
        self.ui.pushButton_Mapa_Ruta.clicked.connect(self.vistaMapa)
        self.ui.pushButton_Recibir_pedidos.clicked.connect(self.algoritmo)
        self.ui.pushButton_Mapeo.clicked.connect(self.vistaMapeo)
        
    def inicializar_datos(self):
        self.cleanTable()
        self.datos= pedidos_table.copy()
        self.llenar_tablas(self.ui.table_Pedidos, self.datos)

    def llenar_tablas(self, table, datos):
        if datos is not None and len(datos) > 0:
            fila = 0
            for registo in datos:
                columna = 0
                self.tables[self.tables.index(table)].insertRow(fila)
                for elemento in registo:
                    celda = QTableWidgetItem(str(elemento))
                    self.tables[self.tables.index(table)].setItem(fila, columna, celda)
                    columna +=1
                fila += 1

    def cleanTable(self):
        for table in self.tables:
            table.clearContents()
            table.setRowCount(0)
            table.update()
            
    def vistaMapa(self):
        self.vista = ControllerMapaRuta()
        self.vista.show()
        
    def algoritmo(self):
        cleanRutas()
        bandera = algoritmogenetico()
        if(bandera):
            self.inicializar_datos()
            self.ui.pushButton_Mapa_Ruta.setEnabled(True)
            
    def vistaMapeo(self):
        self.vista = ControllerMapeo()
        self.vista.show()
        
            
        