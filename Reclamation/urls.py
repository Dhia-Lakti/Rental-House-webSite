from django.urls import path
from .views import getAllReclamations, AddReclamation, getReclamationById, deleteReclamation


urlpatterns = [
    path('', getAllReclamations, name='getAllReclamations'),
    path('add', AddReclamation, name='AddReclamation'),
    path('<int:reclamation_id>', getReclamationById, name='getReclamationById'),
    path('delete/<int:reclamation_id>', deleteReclamation, name='deleteReclamation'),
]
