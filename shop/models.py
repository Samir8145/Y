from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    old_price = models.FloatField(null=True, blank=True, default=None)
    description = models.TextField()
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)
    image = models.ImageField(upload_to='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name