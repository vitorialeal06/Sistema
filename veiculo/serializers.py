from rest_framework.serializers import ModelSerializer
from .models import Veiculo
from rest_framework import serializers

class SerializadorVeiculo(serializers.ModelSerializer):
    """
    Serializador para o modelo Veiculo.
    """

    nome_marca = serializers.SerializerMethodField()
    nome_cor = serializers.SerializerMethodField()
    nome_combustivel = serializers.SerializerMethodField()


    class Meta:
        model = Veiculo
        exclude = []

    def get_nome_marca(self, intancia):
        return intancia.get_marca_display()
    def get_nome_cor(self, intancia):
        return intancia.get_cor_display()
    def get_nome_combustivel(self, intancia):
        return intancia.get_combustivel_display()
