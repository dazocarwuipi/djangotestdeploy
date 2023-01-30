from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):

    #clase Meta necesaria para el serializer
    class Meta:
        #nombre del modelo
        model: Project

        #campos que podran ser consultados 
        fields = ('id', 'title', 'description', 'technology', 'created_at')

        #determina los fields que no se pueden modificar(solo lectura)
        read_only_fields = ('created_at',)