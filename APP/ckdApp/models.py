from django.db import models



# Create your models here.
class ckdModel(models.Model):

    radius_mean=models.FloatField()
    def __str__(self):
        return str(self.pk)
    concavity_mean=models.FloatField()
    radius_worst=models.FloatField()
    compactness_worst=models.FloatField()
    concavity_worst=models.FloatField()
