from django.db import models

# Create your models here.
class Autor(models.Model):
    id= models.AutoField(primary_key = True)#campo autoincremental
    nombre=models.CharField(max_length=200,blank = False, null = False)#tipo CharField y parametros son caracteres, no se puede dejar en blanco ni valores nulos
    apellidos=models.CharField(max_length=200,blank = False, null = False)
    nacionalidad=models.CharField(max_length=200,blank = False, null = False)
    descripcion=models.TextField(blank = False, null = False)#TextField bastantes mas caracteres
