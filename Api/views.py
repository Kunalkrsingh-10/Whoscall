from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser, Contact, Spam
from .serializers import UserSerializer, ContactSerializer, SpamSerializer

class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Welcome in Whoscall !"})
        return Response({"error": "Invalid number , do first register "}, )

class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, )

class Mark_spam(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        phone_no = request.data.get('phone_number')
        spam, created = Spam.objects.get_or_create(phone_no=phone_no)
        spam.spam_count += 1
        spam.save()
        return Response({"message": "Marked as spam"})

class Search_by_name(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        return Contact.objects.filter(name__icontains=name).order_by('name')

class Search_By_num(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        phone_no = request.query_params.get('phone_number')
        contacts = Contact.objects.filter(phone_number=phone_no)
        if contacts:
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)
        user = User.objects.filter(phone_no=phone_no).first()
        if user:
            return Response({"name": user.username, "phone_number": user.phone_no})
        return Response({"message": "No results found"})

