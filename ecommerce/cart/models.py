from django.db import models

# Create your models here.
class Cart(models.Model):
    cart_id = models.AutoField
    productname = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="cart", default="")

    class Meta:
        db_table = "cart"