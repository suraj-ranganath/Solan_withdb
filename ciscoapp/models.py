from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.



class Student(models.Model):
    roll_nbr = models.IntegerField(primary_key=True,default = 0, db_column='roll_nbr', null=False)
    student_name = models.CharField(max_length=30, db_column = 'student_name', null = False)
    subject = models.CharField(max_length=20)
    standard = models.IntegerField(default = 0, db_column='standard')

    class Meta:
        db_table = 'students'
        verbose_name_plural = 'students'
        
    def __str__(self):
        return str(self.roll_nbr) + ' Name => ' + str(self.student_name)

class login(models.Model):
    email_id = models.CharField(max_length=50, db_column='email_id', null= False)
    password = models.CharField(max_length=50, db_column='password', null= False)

    class Meta:
        db_table = 'login'
        verbose_name_plural = 'logins'

    def __str__(self):
        return str(self.email_id) + ' Name => ' +  str(self.password)

class subject(models.Model):
    sub=models.CharField(max_length=50, db_column='sub', null=False)
    chp=models.CharField(max_length=25, db_column='chp', null=True)

    class Meta:
        db_table = 'subject'
        verbose_name_plural = 'subjects'

    def __str__(self):
        return str(self.email_id) + ' Name => ' +  str(self.password)

class question(models.Model):
    subject=models.CharField(primary_key=True,max_length=80,db_column='subject', null=False)
    chapter=models.CharField(max_length=80,db_column='chapter', null=False)
    question=models.CharField(max_length=1000, db_column = 'question', null = False)
    qotw = models.CharField(max_length=1, db_column='qotw', default='n')
    class Meta:
        db_table = 'question'
        verbose_name_plural = 'questions'


