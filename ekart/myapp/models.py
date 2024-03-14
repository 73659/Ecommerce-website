from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CAT=((1,"Mobile"),(2, "Shoes"), (3, "cloths"), (4, "Grocery"), (5, "'Home and Furniture"),(6,"Toys"))
    name=models.CharField(max_length=50, verbose_name="Product Name")
    price=models.IntegerField()
    cat=models.IntegerField(verbose_name='Category')
    product_details=models.CharField(max_length=500, verbose_name="Product Details")
    is_active=models.BooleanField(default=True, verbose_name="Available")
    p_img=models.ImageField(upload_to='image', null="True")

class Cart(models.Model):
    user_id=models.ForeignKey('auth.User', on_delete=models.CASCADE,db_column="userid")
    pid=models.ForeignKey("Product",on_delete=models.CASCADE,db_column="pid")
    qty=models.IntegerField(default=1)

    def __str__(self):
        return self.name
        