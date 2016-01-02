import sys
from gui import *

def mostrar():
	print "OOO"

class Ventana(QtGui.QMainWindow):
	def __init__(self,parent = None ):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		QtCore.QObject.connect(self.ui.action_Lol, QtCore.SIGNAL('triggered()'), self.showDialog)
		#QtCore.QObject.connect(self.ui.fileMenu, QtCore.SIGNAL('trigger()'), self.mostrar)
		QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('pressed()'), self.mostrar)

	def mostrar(self):
		print "OOO"

	def showDialog(self):
		cuadro = QtGui.QFileDialog(self)
		path = QtCore.QDir
		cuadro.setFileMode(QFileDialog.ExistingFiles)
		fname = cuadro.getOpenFileNames(self, 'Abrir Imagn',path.homePath(),"Imagenes (*.png *.jpg *.bmp)")

		print fname

		for i in fname:
			print i


app = QtGui.QApplication(sys.argv)
myapp = Ventana()
myapp.show()
sys.exit(app.exec_())
