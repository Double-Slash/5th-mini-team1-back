from django.shortcuts import render
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, permissions, generics, permissions
from .serializers import *
from .models import *
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser



# only for admin, testin purposes
class AdminPostingList(generics.ListCreateAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer
    # permission_classes = [permissions.IsAdminUser]



# get the list of all Posting a specific user has
class UserPostingList(generics.ListCreateAPIView):
    serializer_class = PostingSerializer
    queryset = Posting.objects.all()

    def get_queryset(self):
        """
        This view should return a list of all the Posting
        for the currently authenticated user.
        """
        #print("request", self.request)
        user = self.request.user
        return Posting.objects.filter(author=user)

    def perform_create(self, serializer):
        return super().perform_create(serializer)



# get individual clothing, only works for owners
class PostingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer
    # permission_classes = [is_owner]
