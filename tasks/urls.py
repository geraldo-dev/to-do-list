from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.detail, name="detail"),
    path('<int:id>/update', views.update, name="update"),
    path('<int:id>/delete', views.delete, name="delete"),
    path('<int:id>/activer', views.activer, name="activer"),
]