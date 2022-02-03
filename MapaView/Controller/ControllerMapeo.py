from MapaView.Views.Ui_Mapeo import Ui_Form

import io
import folium
from mapa import mapa
from PyQt5.QtWidgets import  QWidget, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

colors = ['red','blue','darkred','orange','green','darkblue',
          'purple','cadetblue','black',"darkgreen","gray","darkpurple"]

class ControllerMapeo(QWidget):
    def __init__(self):
        super(ControllerMapeo, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.view = QWebEngineView()
        lay = QHBoxLayout(self.ui.Mapa)
        lay.addWidget(self.view,stretch=1)
        self.contador = 0
        
        self.generarMapa()
    
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
        for calle in mapa:
            for cord in calle:
                folium.Marker(
                    cord,
                    icon=folium.Icon(color='blue')
                              ).add_to(self.m)
        

   