from django.db import models

# Create your models here.

from django.db import models

class HousePriceHistory(models.Model):
    size = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    location = models.CharField(max_length=50)
    age = models.IntegerField()
    garage = models.IntegerField()
    predicted_price = models.DecimalField(max_digits=15, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.size} sqft, {self.bedrooms} beds - ${self.predicted_price}"
