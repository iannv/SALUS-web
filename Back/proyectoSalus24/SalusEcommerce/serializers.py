from rest_framework import serializers

# Tablas Paciente
from.models import (
    Paciente,
    Especialidad,
    Turno,
)
# --- User
from django.contrib.auth.models import User

'''SERIALIZERS'''
# PacienteSerializer
class PacienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Paciente
		fields = '__all__'

# EspecialidadSerializer
class EspecialidadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Especialidad
		fields = '__all__'

# TurnoSerializer
class TurnoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Turno
		fields = '__all__'

# User Serializer
class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','email','is_superuser','is_staff','is_active')           
# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','email','password')
		extra_kwargs = {'password':{'write_only':True}}
	
	def create(self, validated_data):
		user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
		return user

