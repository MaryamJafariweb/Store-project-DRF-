from rest_framework import serializers
from django.contrib.auth.models import User


def clean_email(value):
    if 'admin' in value:
        raise serializers.ValidationError('admin can not be in email')


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        extra_kwarg = {
            'password': {'write_only': True},
            'email': {'validators': (clean_email,)}
        }

    def create(self, validated_data):
        del validated_data['password2']
        return User.objects.create_user(**validated_data)

    def validate_username(self, value):
        if value == 'admin':
            return serializers.ValidationError('username can not be admin!')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password must match')
        return data