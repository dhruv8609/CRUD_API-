from rest_framework import serializers
from accounts.models import *


class StudentRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Student
        fields = ['username', 'email', 'password', 'password2']

    def save(self):
        account = Student(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password ': 'passwords must match'})

        account.set_password(password)
        account.save()
        return account


class MentorRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Mentor
        fields = ['username', 'email', 'password', 'password2']

    def save(self):
        account = Mentor(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password ': 'passwords must match'})

        account.set_password(password)
        account.save()
        return account


class ChangePasswordSerializer(serializers.ModelSerializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password']
