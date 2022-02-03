from MapaView.Views.Ui_Mapa_Ruta_View import Ui_Form

import io
import folium
from mapa import mapa,recorrido_extenso,recorridos,pedidos_recorrido
from PyQt5.QtWidgets import QWidget, QHBoxLayout,QTableWidgetItem
from PyQt5.QtWebEngineWidgets import QWebEngineView

colors = ['red','blue','darkred','orange','green','darkblue',
          'purple','cadetblue','black',"darkgreen","gray","darkpurple"]

class ControllerMapaRuta(QWidget):
    def __init__(self):
        super(ControllerMapaRuta, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.tables = [self.ui.table_pedidos]
        self.ui.pushButton_Siguiente.clicked.connect(self.siguiente)
        self.ui.pushButton_Anterior.clicked.connect(self.anterior)
        
        self.view = QWebEngineView()
        lay = QHBoxLayout(self.ui.Mapa)
        lay.addWidget(self.view,stretch=1)
        self.contador = 0
        
        self.generarMapa()
        self.inicializar_datos()
        
    def inicializar_datos(self):
        self.cleanTable()
        pedidos = pedidos_recorrido
        self.datos= pedidos[self.contador]
        self.llenar_tablas(self.ui.table_pedidos, self.datos)


    def cleanTable(self):
        for table in self.tables:
            table.clearContents()
            table.setRowCount(0)
            table.update()
        
    def llenar_tablas(self, table, datos=[]):
        if datos is not None and len(datos) > 0:
            fila = 0
            columna = 0
            for registro in datos:
                # self.tables[self.tables.index(table)].insertRow(fila)
                self.ui.table_pedidos.insertRow(fila)
                celda = QTableWidgetItem(str(registro))
                # self.tables[self.tables.index(table)].setItem(fila, columna, celda)
                self.ui.table_pedidos.setItem(fila,columna,celda)
                fila += 1
        
    def cleanContador(self):
        self.contador = 0
        
    def siguiente(self):
        if(self.contador+1 < len(recorrido_extenso)):
            self.contador = self.contador+1
            self.generarMapa()
            self.inicializar_datos()
            print("siguiente")
    
    def anterior(self):
        if(self.contador-1 >= 0):
            self.contador = self.contador-1
            self.generarMapa()
            self.inicializar_datos()
            print("Anterior")
    
    def generarMapa(self):
        self.m = folium.Map(
            title="Mapeo Ruta",
            zoom_start= 16,
            location=(16.75054678343964, -93.12154505429446),
            zoom_control= False,
            no_touch=True
            
            )
        self.createMakers()
        # save map data to data object
        data = io.BytesIO()
        self.m.save(data,close_file=False)

        self.view.setHtml(data.getvalue().decode())
        
    def createMakers(self):
        pedidos = pedidos_recorrido
        # print(pedidos[self.contador])
        # print(recorridos[self.contador])
        
        for cord in range(len(recorridos[self.contador])):
            
            if(cord == 0):
                folium.Marker(
                    recorridos[self.contador][cord],
                    icon=folium.Icon(color='green', icon='home', prefix='fa')
                            ).add_to(self.m)
                
            elif(cord <= len(recorridos[self.contador])-2):
                folium.Marker(
                    recorridos[self.contador][cord],
                    icon=folium.Icon(color='blue'),tooltip=f"Pedido {pedidos[self.contador][cord-1]}"
                            ).add_to(self.m)

        for ruta in range(len(recorrido_extenso[self.contador] )):            
            folium.PolyLine(recorrido_extenso[self.contador][ruta], color=colors[ruta], weight=2.5, opacity=1).add_to(self.m)
        

   