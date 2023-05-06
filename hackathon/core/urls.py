from django.urls import path
from . import views


urlpatterns = [
	
	path('', views.view),
    path('shapes', views.shape)
    

	
	]