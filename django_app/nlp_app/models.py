from django.db import models

# Create your models here.

class Category(models.Model):
    clasificacion = models.CharField(
        max_length=255,
        blank=True,
        help_text='Nombre de la categoría'
    )

    def __str__(self):
        return self.clasificacion


class FormSending(models.Model):
    nombre = models.CharField(
        max_length=255,
        blank=True,
        help_text='Ingrese su nombre'
    )
    descripcion = models.TextField(
        blank=True,
        help_text="Descripción ingresada por el usuario."
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Categoría asignada a esta descripción."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha en que se creó la descripción."
    )

    def __str__(self):
        # Se muestra los primeros 50 caracteres de la descripción y la categoría
        return f"{self.descripcion[:50]}... ({self.category})"
    

class ByPass(models.Model):

    formsending = models.ForeignKey(
        FormSending,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Referencia a la descripción")
    
    status = models.BooleanField(
        default=False,
        help_text="True: Aprobado, False: Denegado"
    )

    def __str__(self):
        return f"FormSending {self.formsending_id} - {'Aprobado' if self.status else 'Denegado'}"