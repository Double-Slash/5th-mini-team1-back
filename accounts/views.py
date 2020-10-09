from django.shortcuts import render

from rest_framework import viewsets, status
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema

# from .permissions import is_user


class CustomUserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [is_user]

    # def create(self, request, *args, **kwargs):

    

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        # hash plaintext password into hased with set_password
        instance.set_password(request.data['password'])
        # set request password as hashed password
        request.data['password'] = instance.password
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    # def get_queryset(self):
    #     if self.request.user.is_superuser:
    #         return CustomUser.objects.all()
    #     else:

    #         return CustomUser.objects.filter(id=self.request.user.id)


class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class CustomLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'pk': user.pk})



# social login
from django.contrib.auth.models import User
from django.conf import settings

from google.auth.transport import requests
from google.oauth2 import id_token
from google.auth.transport import requests

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['POST',])
@permission_classes((AllowAny,))
def exchange_token(request):
    token = request.data.get('token')
    print(token)
    CLIENT_ID = settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    print(CLIENT_ID, 'DEBUGG!!!!!\n\n\n\n')
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
    print(idinfo, 'DEBUGG!!!!!\n\n\n\n')

    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise ValueError('Wrong issuer.')

    try:
        user = User.objects.get(email=idinfo['email'])
        if not user:
            return Response({'error': 'Auth failed'}, status=status.HTTP_401_UNAUTHORIZED)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({'error': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)