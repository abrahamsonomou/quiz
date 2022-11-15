from pyexpat import model
from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    model=Category
    fields='__all__'

