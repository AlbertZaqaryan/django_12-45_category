from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name
    
class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categ_prod')
    name = models.CharField('Product name', max_length=60)
    img = models.ImageField('Product image', upload_to='images')
    price = models.PositiveIntegerField('Product price')

    def __str__(self):
        return self.name