from django.db import models

class deportes (models.Model):
	articulo = models.TextField(default = "",null=True)
	deporte = models.TextField(default = "",null=True)
	imagen = models.TextField(default = "",null=True)

	def __str__ (self):
		return self.articulo

class articulo (models.Model):
	nombre = models.TextField(default = "",null=True)
	descripcion = models.TextField(default = "",null=True)
	tipo = models.TextField(default = "",null=True)

	def __str__ (self):
		return self.nombre
		
class comentarios (models.Model):
	usuario = models.TextField(default = "",null=True)
	comentario = models.TextField(default = "",null=True)
	fecha = models.TextField(default = "",null=True)

	def __str__ (self):
		return self.usuario