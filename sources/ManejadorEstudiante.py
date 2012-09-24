from pymongo import Connection
from datetime import date

class ManejadorEstudiante:

	def __init__(self):
		self.__con=Connection()
	        self.__estudiantes=self.__con.estudiantes.estudiantes2012
		self.__asistencia=self.__con.estudiantes.asistencia
		self.__aesia=self.__con.estudiantes.aesia
		

	def aesia(self,id):
		aesia=self.__aesia.find({"_id":id})
		if(aesia!=None):
			return True
		else:
			return False


	def Buscar_estudiante(self,id):
		estudiante=self.__estudiantes.find_one({"_id":id})
		self.__con.close()
		return estudiante

	def Buscar(self,id):
		asistente=self.__asistencia.find_one({"_id":id})
		self.__con.close()
		return asistente
    
        def Buscar_carrera(self,carrera):
		estudiante=[]
		estudiante=self.__asistencia.find({"carrera":carrera})
		self.__con.close()
		return estudiante
    
	def Inscribir(self,id,nombre,carrera):
		try:
			if(not self.EstaInscrito(id)):
				if not self.aesia(id):
					self.__asistencia.save({"_id":id,"nombre":nombre,"carrera":carrera})
				else:
					self.__asistencia.save({"_id":id,"nombre":nombre,"carrera":carrera,"aesia":True})	
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
		#dia=date(2012,9,26).weekday()
			
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
