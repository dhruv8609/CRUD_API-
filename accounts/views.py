from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password

from rest_framework.authtoken.models import Token
from accounts.serializers import *


@api_view(['POST'])
def student_registration(request):
    serializer = StudentRegisterSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "Successfully registered ! please login via api/accounts/login"
        data['username'] = account.username
        data['email'] = account.email
    else:
        data = serializer.errors
    return Response(data)


@api_view(['POST'])
def mentor_registration(request):
    serializer = MentorRegisterSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "Successfully registered! please login via api/accounts/login"
        data['username'] = account.username
        data['email'] = account.email
        # token = Token.objects.get(user=account).key
        # data['token'] = token
    else:
        data = serializer.errors
    return Response(data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def change_password(request):

    account = request.user

    serializer = ChangePasswordSerializer(data=request.data)

    if serializer.is_valid():

        # Checking old password
        if not account.check_password(serializer.data.get("old_password")):
            return Response({"response": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

        # set_password also hashes the password that the user will get
        account.set_password(serializer.data.get("new_password"))
        account.save()
        response = {
            'status': 'success',
            'response': 'Password updated successfully',
        }

        return Response(response)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
