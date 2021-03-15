from django.urls import path
from .views import HomePageView,ContentPageView,AboutPageView,PrincipalPageView

urlpatterns = [
	path('',HomePageView.as_view(),name = 'home'),
	path('content',ContentPageView.as_view(),name = 'content'),
	path('about',AboutPageView.as_view(),name = 'about'),
	path('principal',PrincipalPageView.as_view(),name = 'principal')
]