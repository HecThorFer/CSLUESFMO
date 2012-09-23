from pymongo import Connection
from datetime import date

class ManejadorEstudiante:

	def __init__(self):
		self.__con=Connection()
	        self.__estudiantes=self.__con.estudiantes.estudiantes2012
		self.__asistencia=self.__con.estudiantes.asistencia
		self.__inicio=date(2012,9,24)
		self.__fin=date(2012,9,28)

	def Buscar_estudiante(self,id):
		estudiante=self.__estudiantes.find_one({"_id":id})
		self.__con.close()
		return estudiante

	def Buscar(self,id):
		asistente=self.__asistencia.find_one({"_id":id})
		self.__con.close()
		return asistente

	def Inscribir(self,id,nombre,carrera):
		try:
			if(not EstaInscrito(id)):
				self.__asistencia.save({"_id":id,"nombre":nombre,"apellidos":apellidos,"carrera":carrera})
				self.__con.close()
				return 1
			else:
				return 0
		except:
			return 2
		finally:
			self.__con.close()

	def EstaInscrito(self,id):
		if(self.__asistencia.find_one({"_id":id})==None):
			self.__con.close()
			return False
		else:
			self.__con.close()
			return True

	def MarcarAsistencia(self,id):
		dia=date.today().weekday()
		if dia==0:
			self.__asistencia.update({"_id":id},{"$set":{"dias.lun":True}})
		elif dia==1:
			self.__asistencia.update({"_id":id},{"$set":{"dias.mar":True}})
		elif dia==2:
			self.__asistencia.update({"_id":id},{"$set":{"dias.mie":True}})
		elif dia==3:
			self.__asistencia.update({"_id":id},{"$set":{"dias.jue":True}})
		elif dia==4:
			self.__asistencia.update({"_id":id},{"$set":{"dias.vie":True}})
		self.__con.close()
