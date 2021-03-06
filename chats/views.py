from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, permissions, generics, permissions
from .serializers import *
from .models import *
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Q



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
        This view should return a list of all the chats sent from a 'sender'
        """
        #print("request", self.request)
        sender = self.request.GET.get('sender')
        recipient = self.request.user
        print('sender is', sender)
        filter = Q(sender=sender, recipient=recipient) | Q(sender=recipient, recipient=sender)

        return Chat.objects.filter(filter).order_by('time')

        #return Chat.objects.filter(sender=sender, recipient=recipient)



class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    # def get_queryset(self):
    #     """
    #     This view should return a list of all the Chats
    #     for the currently authenticated user.
    #     """
    #     #print("request", self.request)
    #     user = self.request.user
    #     print(user, 'user')
    #     return Chat.objects.filter(recipient=user)


    # def get_queryset(self):
    #     user = self.request.user
    #     return Chat.objects.filter(receipient=user)
    # # return Chat.objects.filter(recipient=user)
