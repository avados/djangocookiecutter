from rest_framework import serializers

from .models import Ccm


class CcmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ccm
        fields = ('url', 'field1','id')
