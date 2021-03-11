from rest_framework import viewsets

from . import permissions
from .models import Ccm
from .serializers import CcmSerializer


class CcmViewSet(viewsets.ModelViewSet):
    queryset = Ccm.objects.all()
    serializer_class = CcmSerializer
    permission_classes = (permissions.Ccm,)
