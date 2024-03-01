from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    attractions = models.TextField()
    activities = models.TextField()
    image = models.ImageField(upload_to='destination_images')

    def __str__(self):
        return self.name


class Package(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField()
    accommodation = models.CharField(max_length=255)
    inclusions = models.TextField()
    exclusions = models.TextField()

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_travelers = models.PositiveIntegerField()
    special_requests = models.TextField()
    additional_services = models.ManyToManyField(Service)

    def __str__(self):
        return f"{self.user.username}'s Booking"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    content = models.TextField()
    tags = models.ManyToManyField('Tag')
    comments = models.TextField()

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    preferences = models.TextField()

    def __str__(self):
        return self.user.username


# class ImageGallery(models.Model):
#     destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='image_galleries')
#     caption = models.CharField(max_length=255)

#     def __str__(self):
#         return self.caption


# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
#     rating = models.PositiveIntegerField()
#     review_text = models.TextField()

#     def __str__(self):
#         return f"Review by {self.user.username}"


# class Tag(models.Model):
#     name = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.name


# class Comment(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     comment_text = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Comment by {self.user.username}"