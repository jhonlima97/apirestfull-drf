from django.db import models

# Create your models here.
class Developer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    age      = models.PositiveSmallIntegerField()
    status   = models.BooleanField(default=True)
    class Meta:
        unique_together=('fullname', 'nickname')
    def __str__(self):
        return self.nickname

class Project(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()
    start_date  = models.DateField()
    end_date    = models.DateField(null=True, blank=True)
    developer   = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='projects')
    class Meta:
        unique_together=('name',)    
    def __str__(self):
        return self.name