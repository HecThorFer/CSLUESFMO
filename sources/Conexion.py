#!/usr/bin/python

from pymongo import Connection

class Conexion:
	
	def __init__(self,host="127.0.0.1",puerto=27017):
		self.__host=host
		self.__puerto=puerto

	def Conectar(self):
	   	self.__con=Connection(self.__host,self.__puerto)
	   	return self.__con.estudiantes
	  
	def Desconectar(self):
	   	self.__con.disconnect()

	def getHost(self):
		return self.__host

	def getPuerto(self):
		return self.__puerto
        
	def setHost(self,host):
		self.__host=host
	
	def setPuerto(self,puerto):
		self.__puerto=puerto
		
