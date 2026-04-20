from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    city = models.CharField(max_length=100, default="Almaty")
    street = models.TextField(max_length=100, default="ToleBi")
    building_number = models.IntegerField(default=59)

    def __str__(self):
        return f"{self.street}, {self.city}"

class Kitten(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.TextField(blank=True, default="https://placekitten.com/200/300")
    address = models.ForeignKey(Address, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f"{self.name}"

class Message(models.Model):
    
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Message from {self.sender}"
    

# class AdoptionRequest(models.Model):
#     kitten = models.ForeignKey(Kitten, on_delete=models.CASCADE)
#     request_for = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoption_requests_for')
#     request_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoption_requests_from')
#     status = models.CharField(max_length=20, default='pending')

#     def __str__(self):
#         return f"Adoption request for {self.request_for.username} by {self.request_from.username}"