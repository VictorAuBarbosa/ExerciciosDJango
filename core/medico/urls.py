from django.urls import path, include
from django.contrib import admin  # Importe admin
from medico import views
from medico.views import (EspecialidadeListView, EspecialidadeCreateView, EspecialidadeUpdateView,
                    EspecialidadeDeleteView, MedicoListView, MedicoCreateView, MedicoUpdateView,
                    MedicoDeleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('especialidades/', EspecialidadeListView.as_view(), name='especialidade_list'),
    path('especialidades/create/', EspecialidadeCreateView.as_view(), name='especialidade_create'),
    path('especialidades/<int:pk>/update/', EspecialidadeUpdateView.as_view(), name='especialidade_edit'),
    path('especialidades/<int:pk>/delete/', EspecialidadeDeleteView.as_view(), name='especialidade_delete'),
    path('medicos/', MedicoListView.as_view(), name='medico_list'),
    path('medicos/create/', MedicoCreateView.as_view(), name='medico_create'),
    path('medicos/<int:pk>/update/', MedicoUpdateView.as_view(), name='medico_edit'),
    path('medicos/<int:pk>/delete/', MedicoDeleteView.as_view(), name='medico_delete'),
]