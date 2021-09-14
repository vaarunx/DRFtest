from django.db.models import fields
from rest_framework import serializers
from .models import Person


class personSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
