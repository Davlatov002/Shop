from django.db import models
import uuid

class Category(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
class Praduct(models.Model):
    id = models.UUIDField(default = uuid.uuid4, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    category_id = models.ForeignKey(Category, related_name="Category", on_delete=models.CASCADE)
    brend = models.CharField(max_length=255, blank=True, null=True)
    razmer = models.CharField(max_length=255, blank=True, null=True)
    old_price = models.FloatField(default = 0)
    new_price = models.FloatField(default = 0)
    image1 = models.ImageField(upload_to="image/", null=True, blank=True)
    image2 = models.ImageField(upload_to="image/", null=True, blank=True)
    image3 = models.ImageField(upload_to="image/", null=True, blank=True)
    image4 = models.ImageField(upload_to="image/", null=True, blank=True)
    image5 = models.ImageField(upload_to="image/", null=True, blank=True)
    image6 = models.ImageField(upload_to="image/", null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    






