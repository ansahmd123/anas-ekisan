from django.db import models
from accounts.models import User,Subscription

# Create your models here.
class Bit(models.Model):
    farmer_id=models.ForeignKey(User,on_delete=models.CASCADE)
    farmer = models.CharField(max_length=255)
    farmer_address = models.CharField(max_length=1000)
    product = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    quality = models.CharField(max_length=255)
    rate = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    bit_value = models.CharField(max_length=255)
    bitter = models.CharField(max_length=255)
    bitter_address = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,default=False)
    def __str__(self):
        return f"{self.farmer}'s Bit: {self.bit_value}"
    


class DealerProfilepic(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic=models.CharField(max_length=100)


class DealerBitCounts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True)
    current_bid_count = models.IntegerField(default=0)

    def reset_bid_count(self):
        self.current_bid_count = 0
        self.save()