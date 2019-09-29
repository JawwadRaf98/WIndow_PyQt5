from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
# for setting icon in our window
from PyQt5 import QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # defining the title and size of window
        self.title = "PyQt5_Main_Window"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300
        # defining function that is using in program....
        self.InitWindow()

   # defination of the funtion....
    def InitWindow(self):
        #setting the icon for window
        self.setWindowIcon(QtGui.QIcon("home_icon.png"))
        #setting the title of the window....
        self.setWindowTitle(self.title)
        #setting the geometry of the window...
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

App =QApplication(sys.argv)
window = Window()
sys.exit(App.exec())