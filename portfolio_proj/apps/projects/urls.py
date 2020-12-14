from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('<int:prid>', views.project, name="project"),
    path('conservation', views.conservation, name="conservation"),
]