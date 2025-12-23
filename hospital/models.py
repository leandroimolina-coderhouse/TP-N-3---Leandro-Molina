from django.db import models

class DepartamentoMedico(models.Model):
    nombre = models.nombre(max_lenght=50)
    nro_departamento = models.IntegerField(unique=True)
    nro_empleados = models.IntegerField(null=True)
    fecha_de_creacion = models.fecha_de_creacion(auto_now_add=true)
    email_dpto = models.email_dpto() 

    def __str__(self):
        return f"Nombre: {self.nombre} / Nro_depto: {self.nro_departamento}"