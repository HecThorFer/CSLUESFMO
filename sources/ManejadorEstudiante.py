from pymongo import Connection
from datetime import date
class ManejadorEstudiante

	def __init__(self):
		self.__con=Connection()
	        self.__estudiantes=self.__con.estudiantes.estudiantes2012
		self.__asistencia=self.con.estudiantes.asistencia
		self.__inicio=date(2012,9,24)
		self.__fin=date(2012,9,28)

	def Buscar(self,id):
		estudiante=self.__asistencia.find_one({"_id":id})
		self.__con.close()
		return estudiante

	def Inscribir(self,id,nombres,apellidos,carrera):
		if(self.__asistencia.find_one({"_id",id})!=None):
			self.__asistencia.save({"_id":id,"nombres":nombres,"apellidos":apellidos,"carrera":carrera})
			self.__con.close()
			return true
		else:
			return false

	def MarcarAsistencia(self,id)
		 if(self.__asistencia.find_one({"_id",id})!=None):
			
	
