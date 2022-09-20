from rest_framework import serializers
from .models import *

class dataserilaizer(serializers.ModelSerializer):
    class Meta:
        model = JobType_json1
        fields = "__all__"


class candidateserilaizer(serializers.ModelSerializer):
    class Meta:
        model = Candidate1
        fields = "__all__"