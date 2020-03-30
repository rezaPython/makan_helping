from django.db import models


class human(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    job = models.CharField(max_length=250)
    hobbites = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class student(models.Model):
    human = models.ForeignKey(human,on_delete=models.CASCADE)
    moadel = models.BigIntegerField()
    shomare_daneshjoi = models.BigIntegerField()
    dars = models.CharField(max_length=250,default='dars')
    zarfiat = models.BigIntegerField(default=30)

    def __str__(self):
        return 'دسته بندی: {} درس: {} , ظرفیت: {}'.format(self.human,self.dars,self.zarfiat)

