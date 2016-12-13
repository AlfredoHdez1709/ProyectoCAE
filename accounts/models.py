from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	GENEROS = (
		('Hombre','Hombre'),
		('Mujer','Mujer')
		)

	ocupacion = models.CharField(max_length=140,null=True,blank=True)
	sexo = models.CharField(max_length=140,choices=GENEROS, default="Hombre")
	user = models.OneToOneField(User)
	

	def __str__(self):
		return 'este perfil es de: {}'.format(self.user)

class RegistroClie(models.Model):
	nombre = models.CharField(max_length=140, null= True, blank=True)
	apellido = models.CharField(max_length=140, null= True, blank=True)
	matricula = models.IntegerField(blank=True, null=True)
	fecha = models.DateTimeField(auto_now=True)
	media = models.FileField(upload_to='file' , blank=True, null=True)