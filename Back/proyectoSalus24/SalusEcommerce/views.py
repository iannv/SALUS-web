from django.shortcuts import render

# Create your views here.
# Model Serializer
from .models import (
    Paciente,
    Especialidad,
    Turno,
)
from .serializers import (
    PacienteSerializer,
    EspecialidadSerializer,
    TurnoSerializer,
    
)
''' API REST FRAMEWORK CORS '''
from rest_framework import viewsets
# --- User
from rest_framework import (
    generics,
    permissions
)
from .serializers import (
    RegisterSerializer,
    UserSerializer
)
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework.views import APIView
# Create your views here.
'''CRUD - ABML'''
# Tabla Paciente
class PacienteViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
class PacientePorUserView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request,idpu=None):
        pacienteUser = Paciente.objects.filter(pacienteUser=idpu)
        serializer = PacienteSerializer(pacienteUser,many=True)
        return Response(serializer.data)

# Tabla Especialidad
class EspecialidadViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
class EspecialidadPorIdView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request,ide=None):
        especialidadId = Especialidad.objects.filter(id=ide)
        serializer = EspecialidadSerializer(especialidadId,many=True)
        return Response(serializer.data)

# Tabla Turno
class TurnoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer

# ------------ API usuario token
class RegisterAPI(generics.GenericAPIView):
	serializer_class = RegisterSerializer

	def post(self,request,*args,**kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user= serializer.save()
		return Response({
		"user":UserSerializer(user, context=self.get_serializer_context()).data,
		"token":AuthToken.objects.create(user)[1]
		})
    
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)
        return super(LoginAPI,self).post(request,format=None)
    
class ManagerUserView(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user