# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/gui2.ui'
#
# Created: Sun Sep 23 21:47:03 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from sources.ManejadorEstudiante import ManejadorEstudiante

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    
    def Buscar(self):
		result=self.manejador.Buscar(str(self.le_due.text()))
		if result==None:
			result=self.manejador.Buscar_estudiante(str(self.le_due.text()))
		        if result!=None:
		 		self.lbl_nombre.setText(result["nombres"]+" "+result["apellidos"])
       				self.lbl_carrera.setText(result["carrear"])
			else:
				QtGui.QMessageBox.information(self.toolBox, 'No Encontrado', "No se han encontrado coincidencias")
    		else:
			self.lbl_nombre.setText(result["nombre"])
                        self.lbl_carrera.setText(result["carrera"])    

    def Inscribir(self):
	if str(self.le_due.text())!="":
		inscrito=self.manejador.Inscribir(str(self.le_due.text()),str(self.lbl_nombre.text()),str(self.lbl_carrera.text()))
		print inscrito
		if inscrito==1:
			self.btn_clear.click()
			self.btn_clear_2.click()
		elif inscrito==0:
			 QtGui.QMessageBox.information(self.toolBox, 'Lo Siento', "Esta persona ya esta inscrita")
		else:
			 QtGui.QMessageBox.information(self.toolBox, 'Error', "Ha ocurrido un error")
    
    def Inscribir2(self):    
	if str(self.le_carnet.text())!="":
		inscrito=self.manejador.Inscribir(str(self.le_carnet.text()),str(self.le_nombre.text()) + str(" ") + str(self.le_apellido.text()),str(self.cmb_carrera.currentText()))
		if inscrito==1:
			self.btn_clear.click()
		elif inscrito==0:
			 QtGui.QMessageBox.information(self.toolBox, 'Lo Siento', "Esta persona ya esta inscrita")
		else:
			 QtGui.QMessageBox.information(self.toolBox, 'Error', "Ha ocurrido un error")
            
    def Asistencia(self):
	if str(self.le_due.text())!="":
		print "hola"		
    
    def Asistencia2(self):
	if str(self.le_carnet.text())!="":
		print "salu"
    
    def __miCod(self):
	self.manejador=ManejadorEstudiante()
	QtCore.QObject.connect(self.btn_buscar,QtCore.SIGNAL("clicked()"),self.Buscar)
	QtCore.QObject.connect(self.btn_inscribir,QtCore.SIGNAL("clicked()"),self.Inscribir)	
	QtCore.QObject.connect(self.btn_asist,QtCore.SIGNAL("clicked()"),self.Asistencia)

    def __btn_click(self):
	self.manejador=ManejadorEstudiante()
	#QtCore.QObject.connect(self.btn_buscar_2,QtCore.SIGNAL("clicked()"),self.Buscar2)
	QtCore.QObject.connect(self.btn_inscribir_2,QtCore.SIGNAL("clicked()"),self.Inscribir2)
	
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(660, 480)
        self.toolBox = QtGui.QToolBox(Form)
        self.toolBox.setGeometry(QtCore.QRect(20, 20, 621, 421))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 621, 281))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.groupBox = QtGui.QGroupBox(self.page_3)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 531, 221))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 40, 274, 33))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.le_due = QtGui.QLineEdit(self.layoutWidget_2)
        self.le_due.setObjectName(_fromUtf8("le_due"))
        self.horizontalLayout.addWidget(self.le_due)
        self.btn_buscar = QtGui.QPushButton(self.layoutWidget_2)
        self.btn_buscar.setObjectName(_fromUtf8("btn_buscar"))
        self.horizontalLayout.addWidget(self.btn_buscar)
        self.label_19 = QtGui.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(0, 10, 191, 21))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(420, 0, 120, 161))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.widget = QtGui.QWidget(self.groupBox_4)
        self.widget.setGeometry(QtCore.QRect(20, 40, 87, 107))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.btn_inscribir = QtGui.QPushButton(self.widget)
        self.btn_inscribir.setEnabled(True)
        self.btn_inscribir.setObjectName(_fromUtf8("btn_inscribir"))
        self.verticalLayout_11.addWidget(self.btn_inscribir)
        self.btn_asist = QtGui.QPushButton(self.widget)
        self.btn_asist.setEnabled(True)
        self.btn_asist.setObjectName(_fromUtf8("btn_asist"))
        self.verticalLayout_11.addWidget(self.btn_asist)
        self.btn_clear = QtGui.QPushButton(self.widget)
        self.btn_clear.setEnabled(True)
        self.btn_clear.setObjectName(_fromUtf8("btn_clear"))
        self.verticalLayout_11.addWidget(self.btn_clear)
        self.widget1 = QtGui.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(31, 81, 283, 50))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_9.addWidget(self.label_2)
        self.lbl_nombre = QtGui.QLabel(self.widget1)
        self.lbl_nombre.setObjectName(_fromUtf8("lbl_nombre"))
        self.verticalLayout_9.addWidget(self.lbl_nombre)
        self.widget2 = QtGui.QWidget(self.groupBox)
        self.widget2.setGeometry(QtCore.QRect(30, 130, 351, 50))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_3 = QtGui.QLabel(self.widget2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_10.addWidget(self.label_3)
        self.lbl_carrera = QtGui.QLabel(self.widget2)
        self.lbl_carrera.setObjectName(_fromUtf8("lbl_carrera"))
        self.verticalLayout_10.addWidget(self.lbl_carrera)
        self.widget3 = QtGui.QWidget(self.page_3)
        self.widget3.setGeometry(QtCore.QRect(50, 210, 516, 30))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.widget3)
        self.horizontalLayout_16.setMargin(0)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_23 = QtGui.QLabel(self.widget3)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_16.addWidget(self.label_23)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.chk_lun = QtGui.QCheckBox(self.widget3)
        self.chk_lun.setObjectName(_fromUtf8("chk_lun"))
        self.horizontalLayout_15.addWidget(self.chk_lun)
        self.chk_mar = QtGui.QCheckBox(self.widget3)
        self.chk_mar.setObjectName(_fromUtf8("chk_mar"))
        self.horizontalLayout_15.addWidget(self.chk_mar)
        self.chk_mier = QtGui.QCheckBox(self.widget3)
        self.chk_mier.setObjectName(_fromUtf8("chk_mier"))
        self.horizontalLayout_15.addWidget(self.chk_mier)
        self.chk_jue = QtGui.QCheckBox(self.widget3)
        self.chk_jue.setObjectName(_fromUtf8("chk_jue"))
        self.horizontalLayout_15.addWidget(self.chk_jue)
        self.chk_vier = QtGui.QCheckBox(self.widget3)
        self.chk_vier.setObjectName(_fromUtf8("chk_vier"))
        self.horizontalLayout_15.addWidget(self.chk_vier)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_15)
        self.toolBox.addItem(self.page_3, _fromUtf8(""))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 621, 281))
        self.page.setObjectName(_fromUtf8("page"))
        self.groupBox_2 = QtGui.QGroupBox(self.page)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 40, 571, 261))
        self.groupBox_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_21 = QtGui.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(0, 10, 371, 31))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(23, 161, 91, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(440, 30, 120, 161))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.widget4 = QtGui.QWidget(self.groupBox_5)
        self.widget4.setGeometry(QtCore.QRect(20, 30, 87, 107))
        self.widget4.setObjectName(_fromUtf8("widget4"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.widget4)
        self.verticalLayout_12.setMargin(0)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.btn_inscribir_2 = QtGui.QPushButton(self.widget4)
        self.btn_inscribir_2.setEnabled(True)
        self.btn_inscribir_2.setObjectName(_fromUtf8("btn_inscribir_2"))
        self.verticalLayout_12.addWidget(self.btn_inscribir_2)
        self.btn_clear_2 = QtGui.QPushButton(self.widget4)
        self.btn_clear_2.setEnabled(True)
        self.btn_clear_2.setObjectName(_fromUtf8("btn_clear_2"))
        self.verticalLayout_12.addWidget(self.btn_clear_2)
        self.cmb_carrera_2 = QtGui.QComboBox(self.groupBox_2)
        self.cmb_carrera_2.setGeometry(QtCore.QRect(120, 160, 281, 31))
        self.cmb_carrera_2.setObjectName(_fromUtf8("cmb_carrera_2"))
        self.cmb_carrera_2.addItem(_fromUtf8(""))
        self.cmb_carrera_2.addItem(_fromUtf8(""))
        self.cmb_carrera_2.addItem(_fromUtf8(""))
        self.cmb_carrera_2.addItem(_fromUtf8(""))
        self.cmb_carrera_2.addItem(_fromUtf8(""))
        self.cmb_carrera_2.addItem(_fromUtf8(""))
        self.cmb_carrera_2.addItem(_fromUtf8(""))
        self.cmb_carrera_2.addItem(_fromUtf8(""))
        self.widget5 = QtGui.QWidget(self.groupBox_2)
        self.widget5.setGeometry(QtCore.QRect(20, 40, 381, 115))
        self.widget5.setObjectName(_fromUtf8("widget5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget5)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_6 = QtGui.QLabel(self.widget5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.le_carnet = QtGui.QLineEdit(self.widget5)
        self.le_carnet.setObjectName(_fromUtf8("le_carnet"))
        self.horizontalLayout_4.addWidget(self.le_carnet)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_11 = QtGui.QLabel(self.widget5)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_5.addWidget(self.label_11)
        self.le_nombre = QtGui.QLineEdit(self.widget5)
        self.le_nombre.setEnabled(True)
        self.le_nombre.setObjectName(_fromUtf8("le_nombre"))
        self.horizontalLayout_5.addWidget(self.le_nombre)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_12 = QtGui.QLabel(self.widget5)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_11.addWidget(self.label_12)
        self.le_apellido = QtGui.QLineEdit(self.widget5)
        self.le_apellido.setEnabled(True)
        self.le_apellido.setObjectName(_fromUtf8("le_apellido"))
        self.horizontalLayout_11.addWidget(self.le_apellido)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 621, 281))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.widget6 = QtGui.QWidget(self.page_2)
        self.widget6.setGeometry(QtCore.QRect(40, 20, 551, 211))
        self.widget6.setObjectName(_fromUtf8("widget6"))
        self.widget7 = QtGui.QWidget(self.widget6)
        self.widget7.setGeometry(QtCore.QRect(60, 10, 361, 99))
        self.widget7.setObjectName(_fromUtf8("widget7"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.widget7)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_10 = QtGui.QLabel(self.widget7)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_7.addWidget(self.label_10)
        self.cmb_carrera = QtGui.QComboBox(self.widget7)
        self.cmb_carrera.setObjectName(_fromUtf8("cmb_carrera"))
        self.cmb_carrera.addItem(_fromUtf8(""))
        self.cmb_carrera.addItem(_fromUtf8(""))
        self.cmb_carrera.addItem(_fromUtf8(""))
        self.cmb_carrera.addItem(_fromUtf8(""))
        self.cmb_carrera.addItem(_fromUtf8(""))
        self.cmb_carrera.addItem(_fromUtf8(""))
        self.cmb_carrera.addItem(_fromUtf8(""))
        self.verticalLayout_7.addWidget(self.cmb_carrera)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.btn_rifa = QtGui.QPushButton(self.widget7)
        self.btn_rifa.setObjectName(_fromUtf8("btn_rifa"))
        self.horizontalLayout_9.addWidget(self.btn_rifa)
        self.btn_clear_4 = QtGui.QPushButton(self.widget7)
        self.btn_clear_4.setObjectName(_fromUtf8("btn_clear_4"))
        self.horizontalLayout_9.addWidget(self.btn_clear_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.widget8 = QtGui.QWidget(self.widget6)
        self.widget8.setGeometry(QtCore.QRect(60, 110, 395, 52))
        self.widget8.setObjectName(_fromUtf8("widget8"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget8)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_7 = QtGui.QLabel(self.widget8)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_5.addWidget(self.label_7)
        self.lbl_ganador = QtGui.QLabel(self.widget8)
        self.lbl_ganador.setObjectName(_fromUtf8("lbl_ganador"))
        self.verticalLayout_5.addWidget(self.lbl_ganador)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_8 = QtGui.QLabel(self.widget8)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_6.addWidget(self.label_8)
        self.lbl_codigo = QtGui.QLabel(self.widget8)
        self.lbl_codigo.setObjectName(_fromUtf8("lbl_codigo"))
        self.verticalLayout_6.addWidget(self.lbl_codigo)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.page_5 = QtGui.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 621, 281))
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.groupBox_3 = QtGui.QGroupBox(self.page_5)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 10, 521, 211))
        self.groupBox_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_8.setGeometry(QtCore.QRect(330, 30, 181, 101))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.btn_cambiar = QtGui.QPushButton(self.groupBox_8)
        self.btn_cambiar.setGeometry(QtCore.QRect(10, 40, 151, 31))
        self.btn_cambiar.setObjectName(_fromUtf8("btn_cambiar"))
        self.widget9 = QtGui.QWidget(self.groupBox_3)
        self.widget9.setGeometry(QtCore.QRect(20, 10, 255, 152))
        self.widget9.setObjectName(_fromUtf8("widget9"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.widget9)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.widget9)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        self.le_ip = QtGui.QLineEdit(self.widget9)
        self.le_ip.setObjectName(_fromUtf8("le_ip"))
        self.horizontalLayout_6.addWidget(self.le_ip)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_5 = QtGui.QLabel(self.widget9)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_12.addWidget(self.label_5)
        self.le_port = QtGui.QLineEdit(self.widget9)
        self.le_port.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.le_port.setObjectName(_fromUtf8("le_port"))
        self.horizontalLayout_12.addWidget(self.le_port)
        self.verticalLayout_8.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_15 = QtGui.QLabel(self.widget9)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_13.addWidget(self.label_15)
        self.le_user = QtGui.QLineEdit(self.widget9)
        self.le_user.setText(_fromUtf8(""))
        self.le_user.setObjectName(_fromUtf8("le_user"))
        self.horizontalLayout_13.addWidget(self.le_user)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_22 = QtGui.QLabel(self.widget9)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_14.addWidget(self.label_22)
        self.le_pass = QtGui.QLineEdit(self.widget9)
        self.le_pass.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le_pass.setText(_fromUtf8(""))
        self.le_pass.setObjectName(_fromUtf8("le_pass"))
        self.horizontalLayout_14.addWidget(self.le_pass)
        self.verticalLayout_8.addLayout(self.horizontalLayout_14)
        self.toolBox.addItem(self.page_5, _fromUtf8(""))

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(1)
        self.cmb_carrera_2.setCurrentIndex(0)
        QtCore.QObject.connect(self.le_pass, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.btn_cambiar.click)
        QtCore.QObject.connect(self.le_port, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.le_user.setFocus)
        QtCore.QObject.connect(self.btn_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.le_due.clear)
        QtCore.QObject.connect(self.le_due, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.btn_buscar.click)
        QtCore.QObject.connect(self.le_carnet, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.le_nombre.setFocus)
        QtCore.QObject.connect(self.le_user, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.le_pass.setFocus)
        QtCore.QObject.connect(self.le_nombre, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.le_apellido.setFocus)
        QtCore.QObject.connect(self.le_ip, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.le_port.setFocus)
        QtCore.QObject.connect(self.btn_clear_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.le_apellido.clear)
        QtCore.QObject.connect(self.btn_clear_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.le_nombre.clear)
        QtCore.QObject.connect(self.btn_clear_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.le_carnet.clear)
        QtCore.QObject.connect(self.btn_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lbl_carrera.clear)
        QtCore.QObject.connect(self.btn_clear_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lbl_codigo.clear)
        QtCore.QObject.connect(self.btn_clear_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lbl_ganador.clear)
        QtCore.QObject.connect(self.btn_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lbl_nombre.clear)
        QtCore.QObject.connect(self.btn_clear_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cmb_carrera_2.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.le_due, self.btn_buscar)
        Form.setTabOrder(self.btn_buscar, self.btn_inscribir)
        Form.setTabOrder(self.btn_inscribir, self.chk_lun)
        Form.setTabOrder(self.chk_lun, self.chk_mar)
        Form.setTabOrder(self.chk_mar, self.chk_mier)
        Form.setTabOrder(self.chk_mier, self.chk_jue)
        Form.setTabOrder(self.chk_jue, self.chk_vier)
        Form.setTabOrder(self.chk_vier, self.btn_asist)
        Form.setTabOrder(self.btn_asist, self.le_carnet)
        Form.setTabOrder(self.le_carnet, self.le_nombre)
        Form.setTabOrder(self.le_nombre, self.le_apellido)
        Form.setTabOrder(self.le_apellido, self.btn_inscribir_2)
        Form.setTabOrder(self.btn_inscribir_2, self.btn_rifa)
        Form.setTabOrder(self.btn_rifa, self.le_ip)
        Form.setTabOrder(self.le_ip, self.le_port)
        Form.setTabOrder(self.le_port, self.le_user)
        Form.setTabOrder(self.le_user, self.le_pass)
        Form.setTabOrder(self.le_pass, self.btn_cambiar)

        self.__miCod()
    	self.__btn_click()
    	
    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Ingenieria Y Arquitectura", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "DUE:", None, QtGui.QApplication.UnicodeUTF8))
        self.le_due.setInputMask(QtGui.QApplication.translate("Form", "AA99999; ", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_buscar.setText(QtGui.QApplication.translate("Form", "Buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Form", "DUE del estudiante a buscar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Opciones", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_inscribir.setText(QtGui.QApplication.translate("Form", "Inscribir", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_asist.setText(QtGui.QApplication.translate("Form", "Asistencia", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_clear.setText(QtGui.QApplication.translate("Form", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Nombres", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_nombre.setText(QtGui.QApplication.translate("Form", "    @Nombres + @Apellidos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "                       Carrera", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_carrera.setText(QtGui.QApplication.translate("Form", "@Carrera               ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("Form", "Asistencia:", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_lun.setText(QtGui.QApplication.translate("Form", "Lunes", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_mar.setText(QtGui.QApplication.translate("Form", "Martes", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_mier.setText(QtGui.QApplication.translate("Form", "Miércoles", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_jue.setText(QtGui.QApplication.translate("Form", "Jueves", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_vier.setText(QtGui.QApplication.translate("Form", "Viernes", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QtGui.QApplication.translate("Form", "Inscribir Estudiantes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Form", "Información del Estudiante:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Form", "       Carrera:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "Opciones", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_inscribir_2.setText(QtGui.QApplication.translate("Form", "Inscribir", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_clear_2.setText(QtGui.QApplication.translate("Form", "Limpiar", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera_2.setItemText(0, QtGui.QApplication.translate("Form", "INGENIERIA QUIMICA", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera_2.setItemText(1, QtGui.QApplication.translate("Form", "INGENIERIA MECANICA", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera_2.setItemText(2, QtGui.QApplication.translate("Form", "ARQUITECTURA", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera_2.setItemText(3, QtGui.QApplication.translate("Form", "INGENIERIA CIVIL", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera_2.setItemText(4, QtGui.QApplication.translate("Form", "INGENIERIA INDUSTRIAL", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera_2.setItemText(5, QtGui.QApplication.translate("Form", "INGENIERIA DE SISTEMAS INFORMATICOS", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera_2.setItemText(6, QtGui.QApplication.translate("Form", "INGENIERIA ELECTRICA", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera_2.setItemText(7, QtGui.QApplication.translate("Form", "NO ES ESTUDIANTE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "          Carnet:", None, QtGui.QApplication.UnicodeUTF8))
        self.le_carnet.setInputMask(QtGui.QApplication.translate("Form", "AA99999; ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "        Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Form", "     Apellidos:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("Form", "Inscribir Estudiantes Otros", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Carrera según día:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera.setItemText(0, QtGui.QApplication.translate("Form", "INGENIERIA QUIMICA", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera.setItemText(1, QtGui.QApplication.translate("Form", "INGENIERIA MECANICA", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera.setItemText(2, QtGui.QApplication.translate("Form", "ARQUITECTURA", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera.setItemText(3, QtGui.QApplication.translate("Form", "INGENIERIA CIVIL", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera.setItemText(4, QtGui.QApplication.translate("Form", "INGENIERIA INDUSTRIAL", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera.setItemText(5, QtGui.QApplication.translate("Form", "INGENIERIA DE SISTEMAS INFORMATICOS", None, QtGui.QApplication.UnicodeUTF8))
        self.cmb_carrera.setItemText(6, QtGui.QApplication.translate("Form", "INGENIERIA ELECTRICA", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_rifa.setText(QtGui.QApplication.translate("Form", "Iniciar Rifa", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_clear_4.setText(QtGui.QApplication.translate("Form", "Iniciar Rifa", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Ganador:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_ganador.setText(QtGui.QApplication.translate("Form", "@Nombre + @Apellido                                      ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "DUE", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_codigo.setText(QtGui.QApplication.translate("Form", "@DUE        ", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QtGui.QApplication.translate("Form", "Rifa", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("Form", "Opciones", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cambiar.setText(QtGui.QApplication.translate("Form", "Cambiar Configuración", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Direccion IPv4:", None, QtGui.QApplication.UnicodeUTF8))
        self.le_ip.setInputMask(QtGui.QApplication.translate("Form", "999.999.999.999; ", None, QtGui.QApplication.UnicodeUTF8))
        self.le_ip.setText(QtGui.QApplication.translate("Form", "127.0.0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "            Puerto:", None, QtGui.QApplication.UnicodeUTF8))
        self.le_port.setInputMask(QtGui.QApplication.translate("Form", "99999; ", None, QtGui.QApplication.UnicodeUTF8))
        self.le_port.setText(QtGui.QApplication.translate("Form", "27017", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Form", "           Usuario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("Form", "    Contraseña:", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QtGui.QApplication.translate("Form", "Configuración", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

