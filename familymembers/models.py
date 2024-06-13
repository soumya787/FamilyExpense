from django.db import models

# Create your models here.
class FamilyMember(models.Model):
    name = models.TextField(default=None)
    mobile = models.BigIntegerField(default=0)
    occupation = models.TextField(default=None)
    income = models.BigIntegerField(default=0)

    def __str__(self):
        return self.name

# create table expenses(id pk, expense int, purpose varchar(120), membername_id fk reffering to above)
class Expenses(models.Model):
    membername = models.ForeignKey(FamilyMember,on_delete=models.CASCADE)
    expense = models.IntegerField(default=0)
    purpose = models.TextField(default=None, max_length=120)

    def __str__(self):
        return self.purpose

