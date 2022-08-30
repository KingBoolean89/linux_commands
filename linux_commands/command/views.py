from django.shortcuts import render
from .models import Command
from .serializers import CommandSerializer
from rest_framework import viewsets

class CommandViewSet(viewsets.ModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
