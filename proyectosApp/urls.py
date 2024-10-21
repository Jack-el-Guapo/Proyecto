from django.urls import path
from . import views
app_names='proyecto'
urlpatterns =[
    path('', views.listadoProyectos,name="lista_proyecto"),
    path('proyectos/' views.listadoProyectos),
    path('agregarProyecto/', views.agregarProyecto,name="agregar_proyecto"),
    path('eliminarProyecto/<int:id>', views.eliminarProyecto, name="eliminar_proyecto"),
    path('actualizarProyecto/<int:id>', views.actualizarProyecto,name="actualizar_proyecto"),
]