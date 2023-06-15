from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Entry
from .serializers import UserSerializer, EntrySerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EntryListView(generics.ListCreateAPIView):
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Entry.objects.filter(user=user)

class EntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [permissions.IsAuthenticated]
