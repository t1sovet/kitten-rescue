from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='address')
    city = models.CharField(max_length=67, default="Almaty")
    street = models.TextField(max_length=67)
    building_number = models.IntegerField()

    def __str__(self):
        return f"{self.street}, {self.city}"


class Kitten(models.Model):
    name = models.CharField(max_length=67)
    breed = models.CharField(max_length=67, default="Tang Tang")
    age_months = models.PositiveIntegerField(default=67)
    description = models.TextField(blank=True)
    image = models.TextField(blank=True, null=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_kittens",
    )

    address = models.ForeignKey(
        Address, default="ToleBi 59", on_delete=models.SET_DEFAULT
    )

    def __str__(self):
        return f"{self.name} ({self.breed})"

    @property
    def is_adopted(self):
        return self.owner is not None

class Message(models.Model):
    TAG_CHOICES = [
        ("REQ", "Request"),
        ("QUE", "Question"),
        ("ADV", "Advice"),
        ("NON", "None"),
    ]

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    tag = models.CharField(max_length=3, choices=TAG_CHOICES, default="NON")

    kitten = models.ForeignKey(
        Kitten,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="related_messages",
    )

    class Meta:
        ordering = ["-timestamp"]  

    def __str__(self):
        return f"[{self.get_tag_display()}] {self.sender.username}: {self.content[:30]}"
