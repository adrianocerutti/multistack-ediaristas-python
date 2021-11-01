from django.db import models
from rest_framework import fields, serializers
from administracao.models import Servico

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'