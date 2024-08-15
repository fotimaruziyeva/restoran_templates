from django.db import models

class Team (models.Model):
    image=models.ImageField(upload_to='Images/team')
    full_name=models.CharField(max_length=50)
    description=models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f"{self.full_name}"
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"
    
class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    
    
    
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='Images/menu_images')
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.name