from django.db import models

# Create your models here.

class VehicleModel(models.Model):
    name = models.CharField(max_length=150)
    brand = models.CharField(max_length=150)


class Vehicle(models.Model):
    km = models.IntegerField()
    licence_plate = models.CharField(max_length=150,verbose_name='plaka numarası')
    chasis_no = models.CharField(max_length=150, verbose_name='şase numarası')
    vehicle_model = models.ForeignKey(VehicleModel,on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()


