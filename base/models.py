from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone as tz

# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    complete=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    complete_by=models.DateField(null=True)
    def __str__(self):
        return self.title
    def dit(self):
        if self.complete_by>tz.localtime(tz.now()).date():
            return True
    

class Meta:
    ordering=['complete']