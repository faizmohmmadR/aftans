from django.contrib import admin
from api.models.models import *
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']


class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']


class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'destination', 'price', 'duration']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'availability', 'location']


class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'date', 'status']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'phone_number', 'date_of_birth']


# class ImageGalleryAdmin(admin.ModelAdmin):
#     list_display = ['destination', 'caption']


# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ['user', 'destination', 'rating']


# class TagAdmin(admin.ModelAdmin):
#     list_display = ['name']


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['blog', 'user', 'timestamp']


# admin.site.register(User, UserAdmin)
admin.site.register(Destination, DestinationAdmin)
admin.site.register(Package, PackageAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(ImageGallery, ImageGalleryAdmin)
# admin.site.register(Review, ReviewAdmin)
# admin.site.register(Tag, TagAdmin)
# admin.site.register(Comment, CommentAdmin)