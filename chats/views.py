from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, permissions, generics, permissions
from .serializers import *
from .models import *
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser




# Create your views here.
# get the list of all Posting a specific user has
class AllChatList(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    def get_queryset(self):
        """
        This view should return a list of all the Chats
        for the currently authenticated user.
        """
        #print("request", self.request)
        user = self.request.user
        print(user, 'user')
        return Chat.objects.filter(recipient=user)
    
    def perform_create(self, serializer):
        #TODO: CHANGE CHAT SO THAT there is no need to specify sender
        # logged in user is sender
        return super().perform_create(serializer)



class SpecificChatList(generics.ListAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    def get_queryset(self):
        """
        This view should return a list of all the Messages
        for the currently authenticated user.
        """
        #print("request", self.request)
        sender = self.request.data.get('sender')
        print('sender is', sender)
        return Chat.objects.filter(sender=sender)


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer