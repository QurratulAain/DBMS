from django.db import models


#Adding 
# Create your models here.
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    payment_method = models.CharField(max_length=50)
    items = models.CharField(max_length=255)
    items_numbering = models.IntegerField()

   
    quantity_of_items = models.IntegerField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
  

    