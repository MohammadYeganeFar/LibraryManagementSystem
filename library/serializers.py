from rest_framework import serializers
from library import models as lib_models

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = lib_models.Member
        fields = '__all__'
   