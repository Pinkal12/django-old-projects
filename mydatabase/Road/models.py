from django.db import models

# Create your models here.

# class Sagment(models.Model):
#     road_name = models.CharField(max_length=200)
#     road_code = models.IntegerField(max_length=50)
#     mc = models.CharField(max_length=200)
#     length = models.FloatField(max_length=100)
    
#     def __str__(self):
#         return self.mc\
    
class Mc(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    
    def __str__(self):
        return self.state
    
class Segment(models.Model):
    roadname = models.CharField(max_length=100)
    roadcode = models.CharField(max_length=100)
    mc = models.ForeignKey(Mc,on_delete=models.CASCADE)
       
    def __str__(self):
        return self.roadname
    