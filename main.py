import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation
from Project import Ui_MainWindow
from p1 import Ui_Dialog
from pag import Ui_Dialog1
from pag2 import Ui_Dialog2
from pag3 import Ui_Dialog3
from Square import Ui_Square
from Square1 import Ui_Square1
from Square2 import Ui_Square2
from Sim import Ui_Sim
from Sim1 import Ui_Sim1
from Sim2 import Ui_Sim2
from Circle import Ui_Circle
from Circle1 import Ui_Circle1
from Circle2 import Ui_Circle2

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def openOtherWindow():
    global Dialog
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    MainWindow.close()

    def returnToMain():
        Dialog.hide()
        MainWindow.show()

    ui.pushButton_6.clicked.connect(returnToMain)

    #ЧЕТЫРЁХУГОЛЬНИКИ

    def openChetWindow1():
        global Dialog1
        Dialog1 = QtWidgets.QWidget()
        ui = Ui_Dialog1()
        ui.setupUi(Dialog1)
        Dialog.hide()
        Dialog1.show()

        def returnToWindow1():
            Dialog1.close()
            Dialog.show()

        ui.pushButton_2.clicked.connect(returnToWindow1)

    ui.pushButton.clicked.connect(openChetWindow1)

    def openChetWindow2():
        global Dialog2
        Dialog2 = QtWidgets.QDialog()
        ui = Ui_Dialog2()
        ui.setupUi(Dialog2)
        Dialog.close()
        Dialog2.show()

        def returnToWindow2():
            Dialog2.close()
            Dialog.show()

        ui.pushButton_2.clicked.connect(returnToWindow2)

    ui.pushButton_2.clicked.connect(openChetWindow2)

    def openChetWindow3():
        global Dialog3
        Dialog3 = QtWidgets.QDialog()
        ui = Ui_Dialog3()
        ui.setupUi(Dialog3)
        Dialog.close()
        Dialog3.show()

        def returnToWindow3():
            Dialog3.close()
            Dialog.show()

        ui.pushButton_2.clicked.connect(returnToWindow3)

    ui.pushButton_4.clicked.connect(openChetWindow3)

    # ПЛОЩАДИ ФИГУР ----------------------------------------------------------------------------------------------------

def Square():
    global Square
    Square = QtWidgets.QDialog()
    ui = Ui_Square()
    ui.setupUi(Square)
    MainWindow.close()
    Square.show()

    def returnToMainSquare():
        Square.close()
        MainWindow.show()

    ui.pushButton_6.clicked.connect(returnToMainSquare)

    def Square1():
        global Square1
        Square1 = QtWidgets.QDialog()
        ui = Ui_Square1()
        ui.setupUi(Square1)
        Square.hide()
        Square1.show()

        def returnToMainSquare1():
            Square1.hide()
            Square.show()

        ui.pushButton_2.clicked.connect(returnToMainSquare1)

    ui.pushButton_.clicked.connect(Square1)

    def Square2():
        global Square2
        Square2 = QtWidgets.QDialog()
        ui = Ui_Square2()
        ui.setupUi(Square2)
        Square.hide()
        Square2.show()

        def returnToMainSquare2():
            Square2.hide()
            Square.show()

        ui.pushButton_2.clicked.connect(returnToMainSquare2)

    ui.pushButton_3.clicked.connect(Square2)

    # ПОДОБНЫЕ ТРЕУГОЛЬНИКИ --------------------------------------------------------------------------------------------

def Sim():
    global Sim
    Sim = QtWidgets.QDialog()
    ui = Ui_Sim()
    ui.setupUi(Sim)
    Sim.show()
    MainWindow.close()

    def returnToMainSim():
        Sim.close()
        MainWindow.show()

    ui.pushButton_6.clicked.connect(returnToMainSim)

    def Sim1():
        global Sim1
        Sim1 = QtWidgets.QDialog()
        ui = Ui_Sim1()
        ui.setupUi(Sim1)
        Sim1.show()
        Sim.close()

        def returnToMainSim1():
            Sim1.close()
            Sim.show()

        ui.pushButton_2.clicked.connect(returnToMainSim1)

    ui.pushButton_3.clicked.connect(Sim1)

    def Sim2():
        global Sim2
        Sim2 = QtWidgets.QDialog()
        ui = Ui_Sim2()
        ui.setupUi(Sim2)
        Sim2.show()
        Sim.close()

        def returnToMainSim2():
            Sim2.close()
            Sim.show()

        ui.pushButton_2.clicked.connect(returnToMainSim2)

    ui.pushButton_.clicked.connect(Sim2)

    # ОКРУЖНОСТЬ -------------------------------------------------------------------------------------------------------

def Circle():
    global Circle
    Circle = QtWidgets.QDialog()
    ui = Ui_Circle()
    ui.setupUi(Circle)
    Circle.show()
    MainWindow.close()

    def returnToMainCircle():
        Circle.close()
        MainWindow.show()

    ui.pushButton_6.clicked.connect(returnToMainCircle)

    def Circle1():
        global Circle
        Circle1 = QtWidgets.QDialog()
        ui = Ui_Circle1()
        ui.setupUi(Circle1)
        Circle1.show()
        Circle.close()

        def returnToMainCircle1():
            Circle1.close()
            Circle.show()

        ui.pushButton_2.clicked.connect(returnToMainCircle1)

    ui.pushButton_3.clicked.connect(Circle1)

    def Circle2():
        global Circle
        Circle2 = QtWidgets.QDialog()
        ui = Ui_Circle2()
        ui.setupUi(Circle2)
        Circle2.show()
        Circle.close()

        def returnToMainCircle2():
            Circle2.close()
            Circle.show()

        ui.pushButton_2.clicked.connect(returnToMainCircle2)

    ui.pushButton_.clicked.connect(Circle2)

ui.pushButton_4.clicked.connect(Circle)

ui.pushButton_3.clicked.connect(Sim)

ui.pushButton_2.clicked.connect(Square)

ui.pushButton.clicked.connect(openOtherWindow)

sys.exit(app.exec_())