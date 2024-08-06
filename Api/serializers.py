# this is use to convert object into JSON for interact to other servers.
# api/serializers.py
from rest_framework import serializers
from .models import CustomUser, Contact, Spam

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'phone_number', 'email', 'password']
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'user', 'name', 'phone_number', 'is_spam']

class SpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spam
        fields = ['id', 'phone_number', 'spam_count']
