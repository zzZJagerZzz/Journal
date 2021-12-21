from django.db import models
    
class Status(models.Model):
    status_matanaliz = models.CharField(max_length=30)
    status_informatics = models.CharField(max_length=30)
    status_russian = models.CharField(max_length=30)
    status_gymnastic = models.CharField(max_length=30)
    status_yap = models.CharField(max_length=30)
    status_proglang = models.CharField(max_length=30)
    status_inyaz = models.CharField(max_length=30)
    status_oib = models.CharField(max_length=30)
    status_linal = models.CharField(max_length=30)
    
    def __str__(self):
        return "Статус"

        
class Student(models.Model):
    student_name = models.CharField(max_length=30)
    student_lastname = models.CharField(max_length=30)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.student_name