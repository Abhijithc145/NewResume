from rest_framework import serializers
from .models import *

class dataserilaizer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = "__all__"


class candidateserilaizer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"

class Matchserilaizer(serializers.ModelSerializer):
    class Meta:
        model = Matchdata
        fields = "__all__"       