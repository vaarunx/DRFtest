from people.models import Person
from django.shortcuts import render
from .serializers import personSerializer
from rest_framework import viewsets

# Create your views here.


class personViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = personSerializer
