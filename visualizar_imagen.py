# -*- coding: utf-8 -*-
"""
Codigo para visualizar una imagen en un form agregando un titulo
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
 
class App(QWidget):
 
    def __init__(self):
        super().__init__(image=None, title='')
        self.title = title #se utiliza para el titulo de la imagen
        self.image = image
        self.left = 10 
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI(self)
 
    def initUI(self, Form):
        self.setWindowTitle(self.title) #establezco el titulo de la imagen
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.verticalLayout = QVBoxLayout(Form)      
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QLabel(Form)
        self.labelTitle.setObjectName("labelTitle")
        self.labelTitle.setText(self.title) #establezco el titulo
        self.labelTitle.setWordWrap(True) #para el caso de que sea muy largo hace un wordwrap
        self.verticalLayout.addWidget(self.labelTitle)
        # creo el widget para la imagen
        label = QLabel(self)
        pixmap = QPixmap(self.image)
        label.setPixmap(pixmap)
        self.verticalLayout.addWidget(label) #agrego la imagen al layout
        self.resize(pixmap.width(),pixmap.height()+self.labelTitle.height()) #alto y ancho del form ajustado al tamaño de la imagen
 
        self.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
