from django.db import models



# Task model
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
   
    def __str__(self):
        return self.title
    


# Category model
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    img = models.ImageField()
    def __str__(self):
        return self.description


# Product model
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    price  = models.FloatField()
    img = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.description