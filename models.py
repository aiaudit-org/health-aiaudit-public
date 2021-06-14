from django.db import models

# Create your data models here.
class ModelFactsheet(models.Model):
    ChallengeId=models.CharField(max_length=50)
    ModelName=models.CharField(max_length=50)
    ModelDeveloper=models.CharField(max_length=50)
    ModelTask=models.CharField(max_length=50)
    ModelAlgo=models.CharField(max_length=50)
    ModelOutput=models.CharField(max_length=200)
    ModelAccuracy=models.DecimalField(max_digits=5,decimal_places=2)
    ModelSensitivity=models.DecimalField(max_digits=5,decimal_places=2)
    ModelSpecificity=models.DecimalField(max_digits=5,decimal_places=2)
    ModelF1Score=models.DecimalField(max_digits=5,decimal_places=2)
    ModelAUROC=models.DecimalField(max_digits=5,decimal_places=2)
    ModelClnImp=models.CharField(max_length=1000)
    ModelSafImp=models.CharField(max_length=1000)
    ModelEffy=models.CharField(max_length=1000)
    ModelAssump=models.CharField(max_length=1000)
    ModelCav=models.CharField(max_length=1000)
    ModelGenblty=models.CharField(max_length=1000)
    ModelRisks=models.CharField(max_length=1000)
    ModelRisks=models.CharField(max_length=1000)
