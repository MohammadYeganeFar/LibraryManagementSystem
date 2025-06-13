from django.contrib.auth.models import User
from rest_framework import serializers, validators
from authenticate.models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {
            "password": {"write_only": True}, # پسورد فقط برای نوشتن است و در خروجی نمایش داده نمی‌شود
            "email": {
                "required": True,
                "allow_blank": False,
                "validators": [
                    validators.UniqueValidator(
                        User.objects.all(), "A user with that Email already exists."
                    )
                ],
            },
        }

    def create(self, validated_data):
        # از متد create_user برای ساخت کاربر استفاده می‌کنیم تا پسورد به درستی هش شود
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'