from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'APP_FROTA'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('veiculos/', views.veiculo_list, name='veiculo_list'),
    path('veiculos/novo/', views.veiculo_create, name='veiculo_create'),
    path('veiculos/<int:pk>/', views.veiculo_detail, name='veiculo_detail'),
    path('veiculos/<int:pk>/excluir/', views.veiculo_delete, name='veiculo_delete'),
    path('condutores/', views.condutor_list, name='condutor_list'),
    path('condutores/novo/', views.condutor_create, name='condutor_create'),
    path('condutores/<int:pk>/excluir/', views.condutor_delete, name='condutor_delete'),
]
