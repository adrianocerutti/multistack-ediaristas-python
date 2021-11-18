from django.db import models
from rest_framework import serializers
from ..models import Diaria, Usuario
from administracao.services import servico_service

class UsuarioDiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'nascimento', 'telefone', 'tipo_usuario', 'reputacao', 'foto_usuario')

class DiariaSerializer(serializers.ModelSerializer):
    cliente = UsuarioDiariaSerializer(read_only=True)
    class Meta:
        model = Diaria
        fields = '__all__'
    
    def create(self, validated_data):
        servico = servico_service.listar_servico_id(validated_data["servico"].id)
        valor_comissao = validated_data["preco"] - (
            validated_data["preco"] * servico.porcentagem_comissao / 100)
        print(valor_comissao)
        diaria = Diaria.objects.create(cliente_id=self.context['request'].user.id,**validated_data)
        return diaria