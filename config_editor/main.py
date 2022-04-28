from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from gui import *
from settings_utils import *


class App(QtWidgets.QMainWindow):
    config = load_config()
    
    current_btn = 1
    # create a list name buttons that contains deck_x where x is from 1 to 16
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.update_img()
        #header buttons
        self.ui.menuToggle.clicked.connect(self.menuBar)
        self.ui.closeButton.clicked.connect(self.close)
        
        #menu buttons
        self.ui.Page1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.Page2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.Page3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.save_btn.clicked.connect(lambda: self.set_settings(self.current_btn))
        
        

                
        for i in range(1,16):
            exec("self.ui.deck_{}.clicked.connect(lambda: self.set_active_btn({}))".format(i, i), locals(), locals())
        
        
          
    def update_img(self):
        self.config = load_config()
        for i in range(1,16):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap('../Assets/'+self.config[str(i-1)]["image"]), QtGui.QIcon.Normal, QtGui.QIcon.On) 
            exec("self.ui.deck_{}.setIcon(icon)".format(i), locals(), locals())
            exec("self.ui.deck_{}.setIconSize(QtCore.QSize(100, 100))".format(i), locals(), globals())
            

    def set_active_btn(self, id):
        self.config = load_config()
        self.ui.command_label.setText(self.config[str(id-1)]["command"])
        self.ui.icon_label.setText(self.config[str(id-1)]["image"])
        self.ui.title_label.setText(self.config[str(id-1)]["text"])
        self.current_btn = id
        
        
    def set_settings(self, id):
        self.config = load_config()
        command = self.ui.command_label.text()
        icon = self.ui.icon_label.text()
        title = self.ui.title_label.text()
        self.config[str(id-1)]["command"] = command
        self.config[str(id-1)]["image"] = icon
        self.config[str(id-1)]["text"] = title
        save_config(self.config)
        self.update_img()
       
    def menuBar(self):
               
        if self.ui.menu_frame.width() == 0:
            self.ui.menu_frame.setFixedWidth(100)
        else:
            self.ui.menu_frame.setFixedWidth(0)
        
    def close(self):
        sys.exit()
        
        
        
def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()
    
    
main()