import sys
from gui1 import *
from PyQt4.QtCore  import *
from  PyQt4.QtGui import *
from os import listdir,makedirs,rename,path
import os
import shutil
import recortar01


class Ventana(QtGui.QMainWindow):
	def __init__(self,parent = None ):
		QtGui.QWidget.__init__(self,parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		#QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL('pressed()'), self.mostrar)

		QtCore.QObject.connect(self.ui.btnMuestra, QtCore.SIGNAL('clicked()'), self.addMuestra )
		QtCore.QObject.connect(self.ui.refreshbtn, QtCore.SIGNAL('clicked()'), self.refresh )

	def addMuestra(self):
		tipo =  self.ui.lineEdit.text()
		self.ui.lineEdit.clear()

		cuadro = QtGui.QFileDialog(self)
		path = QtCore.QDir

		if self.ui.rbtnCarpetas.isChecked():
			# Load a directory
			cuadro.setFileMode(QtGui.QFileDialog.Directory)
			fname = cuadro.getExistingDirectory(self, 'Abrir Imagn',path.homePath())
			fname  = QtCore.QDir.fromNativeSeparators(fname)
			files = listdir(fname)
			print files

			rc = "images/origen/origen-"+str(tipo)
			bc = "images/binar/binar-"+str(tipo)
			try:
				makedirs(rc)
				makedirs(bc)
			except:
				print "carpeta ya creada"

			j = 0
			for i in files:
				shutil.copy(str(fname) + "/" + i, rc)
				rename(rc + "/" + i,rc + "/" + str(tipo) + "-"+str(j)+".jpg")
				print (rc + "/" + i)
				j +=1

		else:
			cuadro.setFileMode(QFileDialog.ExistingFiles)
			fname = cuadro.getOpenFileNames(self, 'Abrir Imagn',path.homePath(),"Imagenes (*.jpg)")
			#fname  = QtCore.QDir.fromNativeSeparators(fname)
			
			#for i in  fname:
			#	print str(i).split("\\")[-1:][0]


			rc = "images/origen/origen-"+str(tipo)
			bc = "images/binar/binar-"+str(tipo)
			try:
				makedirs(rc)
				makedirs(bc)
			except:
				print "carpeta ya creada"
		
			j=0
			for i in fname:
				shutil.copy(str(i), rc)

				rename(rc + "/" + (str(i).split("\\")[-1:][0]), rc + "/" + str(tipo) + "-"+str(j)+".jpg")
				print (rc + "/" + i)
				j +=1

		#Load files

		#
		self.refresh()


	def refresh(self):
		model = QFileSystemModel()
		model.setRootPath(QtCore.QDir.currentPath())

		self.ui.treeView.setModel(model)
		path =  str(QtCore.QDir.currentPath()) + "/images/origen"
		#print type(path)
		model = model.index(path)
		self.ui.treeView.setRootIndex(model)
		self.ui.treeView.hideColumn(1)
		self.ui.treeView.hideColumn(2)
		self.ui.treeView.hideColumn(3)

		#######################
		model = QFileSystemModel()
		model.setRootPath(QtCore.QDir.currentPath())

		self.ui.treeView_2.setModel(model)
		path =  str(QtCore.QDir.currentPath()) + "/images/binar"
		#print type(path)
		model = model.index(path)
		self.ui.treeView_2.setRootIndex(model)
		self.ui.treeView_2.hideColumn(1)
		self.ui.treeView_2.hideColumn(2)
		self.ui.treeView_2.hideColumn(3)
		self.binarizar()

	def binarizar(self):
		files = listdir("images/origen")
		for i in files:
			n = 0
			for j in listdir("images/origen/"+i):
				path = "images/origen/"+i+"/"+j
				tipo = "binar-"+i.split("-")[1]

				print "tipo"
				#print path
				recortar01.binarf(path,tipo,n)
				n+=1

app = QtGui.QApplication(sys.argv)
myapp = Ventana()
myapp.show()
sys.exit(app.exec_())