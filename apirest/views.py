from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.
class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class= DeveloperSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class= ProjectSerializer