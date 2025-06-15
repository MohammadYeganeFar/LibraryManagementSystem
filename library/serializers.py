from rest_framework import serializers
from library.models import Member, Author

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
   