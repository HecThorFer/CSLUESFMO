# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtSDK/projects/pruebaComboBox.ui'
#
# Created: Sun Sep  9 13:41:57 2012
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!
from pymongo import Connection
from array import *
from PyQt4 import QtCore, QtGui

class modelo:
	def extraerCarreras(x):
		connection = Connection()
		db = connection.test
		carreras = []
		for estudiante in db.estudiantes.find({"carrera": { '$exists' : True } }):
			carreras.append(estudiante["carrera"])
		return carreras	
	
class Ui_Form(object):
	def envioDatos(self):
		connection = Connection()
		db = connection.test
		carnet = unicode(self.txtCarnet.text())
		nombre = unicode(self.txtNombre.text())
		carrera = unicode(self.cmbCarrera.currentText())
		db.estudiantes.insert({"_id":carnet, "nombre":nombre, "carrera":carrera})
		print "Exito"
	
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(400, 300)
		self.btnAgregar = QtGui.QPushButton(Form)
		self.btnAgregar.setGeometry(QtCore.QRect(10, 220, 91, 41))
		self.btnAgregar.setObjectName("btnAgregar")
		self.cmbCarrera = QtGui.QComboBox(Form)
		self.cmbCarrera.setGeometry(QtCore.QRect(70, 90, 181, 26))
		self.cmbCarrera.setObjectName("cmbCarrera")
		self.txtCarnet = QtGui.QLineEdit(Form)
		self.txtCarnet.setGeometry(QtCore.QRect(70, 10, 71, 26))
		self.txtCarnet.setMaxLength(7)
		self.txtCarnet.setCursorPosition(0)
		self.txtCarnet.setObjectName("txtCarnet")
		self.label = QtGui.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(10, 20, 55, 16))
		self.label.setObjectName("label")
		self.label_2 = QtGui.QLabel(Form)
		self.label_2.setGeometry(QtCore.QRect(10, 60, 55, 16))
		self.label_2.setObjectName("label_2")
		self.txtNombre = QtGui.QLineEdit(Form)
		self.txtNombre.setGeometry(QtCore.QRect(70, 50, 261, 26))
		self.txtNombre.setObjectName("txtNombre")
		self.label_3 = QtGui.QLabel(Form)
		self.label_3.setGeometry(QtCore.QRect(10, 90, 55, 16))
		self.label_3.setObjectName("label_3")
		self.lineEdit_3 = QtGui.QLineEdit(Form)
		self.lineEdit_3.setEnabled(True)
		self.lineEdit_3.setGeometry(QtCore.QRect(70, 130, 301, 26))
		self.lineEdit_3.setVisible(False)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.chkOtraCarrera = QtGui.QCheckBox(Form)
		self.chkOtraCarrera.setGeometry(QtCore.QRect(260, 90, 111, 21))
		self.chkOtraCarrera.setObjectName("chkOtraCarrera")
		self.label_4 = QtGui.QLabel(Form)
		self.label_4.setGeometry(QtCore.QRect(10, 120, 51, 41))
		self.label_4.setVisible(False)
		self.label_4.setObjectName("label_4")

		self.retranslateUi(Form)
		QtCore.QObject.connect(self.chkOtraCarrera, QtCore.SIGNAL("toggled(bool)"), self.lineEdit_3.setShown)
		QtCore.QObject.connect(self.chkOtraCarrera, QtCore.SIGNAL("toggled(bool)"), self.label_4.setShown)
		QtCore.QObject.connect(self.chkOtraCarrera, QtCore.SIGNAL("toggled(bool)"), self.cmbCarrera.setDisabled)
		QtCore.QObject.connect(self.btnAgregar, QtCore.SIGNAL("clicked()"), self.envioDatos)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
		self.btnAgregar.setText(QtGui.QApplication.translate("Form", "Agregar", None, QtGui.QApplication.UnicodeUTF8))
		instancia = modelo()
		carreras = instancia.extraerCarreras()
		for i, carrera in enumerate(carreras):
			self.cmbCarrera.addItem("")
			self.cmbCarrera.setItemText(i, QtGui.QApplication.translate("Form", carrera, None, QtGui.QApplication.UnicodeUTF8))
		self.txtCarnet.setInputMask(QtGui.QApplication.translate("Form", ">AA99999;_", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("Form", "Carnet:", None, QtGui.QApplication.UnicodeUTF8))
		self.label_2.setText(QtGui.QApplication.translate("Form", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
		#self.txtNombre.setInputMask(QtGui.QApplication.translate("Form", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa; ", None, QtGui.QApplication.UnicodeUTF8))
		self.label_3.setText(QtGui.QApplication.translate("Form", "Carrera:", None, QtGui.QApplication.UnicodeUTF8))
		self.chkOtraCarrera.setText(QtGui.QApplication.translate("Form", "Otra Carrera", None, QtGui.QApplication.UnicodeUTF8))
		self.label_4.setText(QtGui.QApplication.translate("Form", "Nueva\n"
"Carrera:", None, QtGui.QApplication.UnicodeUTF8))
		

if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	Form = QtGui.QWidget()
	ui = Ui_Form()
	ui.setupUi(Form)
	Form.show()
	sys.exit(app.exec_())

