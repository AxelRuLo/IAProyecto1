from MapaView.Views.Ui_Mapa_Ruta_View import Ui_Form

import io
import folium
from mapa import mapa,recorrido_extenso,recorridos,recorridos_nodos
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout,QVBoxLayout,QPushButton,QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

colors = ['red','blue','darkred','orange','green','darkblue',
          'purple','cadetblue','black',"darkgreen","gray","darkpurple"]

class ControllerMapaRuta(QWidget):
    def __init__(self):
        super(ControllerMapaRuta, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.pushButton_Siguiente.clicked.connect(self.siguiente)
        self.ui.pushButton_Anterior.clicked.connect(self.anterior)
        
        self.view = QWebEngineView()
        lay = QHBoxLayout(self.ui.Mapa)
        lay.addWidget(self.view,stretch=1)
        self.contador = 0
        
        self.generarMapa()
        
    def siguiente(self):
        if(self.contador+1 < len(recorrido_extenso)):
            self.contador = self.contador+1
            self.generarMapa()
            print("siguiente")
    
    def anterior(self):
        if(self.contador-1 >= 0):
            self.contador = self.contador-1
            self.generarMapa()
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
        for cord in range(len(recorridos[self.contador])):
            
            if(cord == 0):
                folium.Marker(
                    recorridos[self.contador][cord],
                    icon=folium.Icon(color='green', icon='home', prefix='fa')
                            ).add_to(self.m)
                
            elif(cord <= len(recorridos[self.contador])-2):
                folium.Marker(
                    recorridos[self.contador][cord],
                    icon=folium.Icon(color='blue'),tooltip=f"{cord}"
                            ).add_to(self.m)

        for ruta in range(len(recorrido_extenso[self.contador] )):            
            folium.PolyLine(recorrido_extenso[self.contador][ruta], color=colors[ruta], weight=2.5, opacity=1).add_to(self.m)
        

   