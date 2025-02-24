from django.db import models

class Mobile(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    specifications = models.TextField()
    image = models.ImageField(upload_to='mobiles/')

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.CharField(max_length=100)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"Cart {self.id} for {self.user}"

    def get_item(self, mobile_id):
        try:
            return self.mobile.get(id=mobile_id)
        except Mobile.DoesNotExist:
            return None
