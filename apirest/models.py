from django.core.exceptions import ValidationError
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
    def clean(self):
        super().clean()
        if not self.fullname.isalpha():
            raise ValidationError('The fullname can only contain letters.')
        if not self.fullname or not self.nickname or not self.age:
            raise ValidationError('All fields are required.')

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
    def clean(self):
        super().clean()
        if not self.name.isalpha():
            raise ValidationError('The name can only contain letters.')
        if not self.name or not self.description or not self.start_date or not self.developer:
            raise ValidationError('All fields are required.')
    