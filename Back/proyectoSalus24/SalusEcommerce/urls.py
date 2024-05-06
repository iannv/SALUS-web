from django.urls import path, include
from rest_framework import routers

''' IMPORTAR VISTAS DE appSalus '''
from SalusEcommerce import views
''' IMPORTAR VISTAS DE VIEWS '''
from .views import (
    RegisterAPI,
    LoginAPI,
    ManagerUserView,
    PacientePorUserView
)
''' IMPORTAR USER KANOX TOKEN '''
from knox import views as kanox_views
router = routers.DefaultRouter()
router.register(r'paciente',views.PacienteViewSet)
#--
urlpatterns = [
    path('registro',RegisterAPI.as_view(),name='register'),
    path('profile',ManagerUserView.as_view(),name='profile'),
    path('login',LoginAPI.as_view(),name='login'),
    path('logout',kanox_views.LogoutView.as_view(),name='logout'),
    path('logoutall',kanox_views.LogoutAllView.as_view(),name='logoutall'),
    path('paciente-user/<int:idpu>',PacientePorUserView.as_view(),name='paciente_user'),
    path('',include(router.urls)),
]