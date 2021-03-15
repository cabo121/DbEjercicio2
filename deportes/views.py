from django.views.generic import ListView
from .models import deportes,articulo,comentarios
# Create your views here.

class HomePageView(ListView):
	model = deportes
	template_name = 'home.html'
	context_object_name = 'listado_deportes'

class ContentPageView(ListView):
	model = articulo
	template_name = 'content.html'
	context_object_name = 'listado_articulo'

class AboutPageView(ListView):
	model = comentarios
	template_name = 'about.html'
	context_object_name = 'listado_comentarios'

class PrincipalPageView(ListView):
	model = deportes
	template_name = 'principal.html'
