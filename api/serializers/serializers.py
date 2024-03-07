from rest_framework import serializers
from api.models.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta(object): 
        model = User
        fields = ['username','email','first_name','last_name']
        
        
class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
        
class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        
        

class BookingSerializer(serializers.ModelSerializer):
    additional_services = ServiceSerializer(many=True)

    class Meta:
        model = Booking
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Blog
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'


# class ImageGallerySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ImageGallery
#         fields = '__all__'


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
