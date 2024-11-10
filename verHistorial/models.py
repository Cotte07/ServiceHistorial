from django.db import models
#db_table -> sirve para comunicarse con la tabla de la bd
#manage: false -> asi se restringe hacer cambios en la bd desde este proyecto
class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'consultarInv_categoria'

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    proveedor = models.CharField(max_length=20)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True)
    estado = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'consultarInv_producto'

class Historial(models.Model):
    fecha_compra = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'consultarInv_historial'

class Lote(models.Model):
    fecha_Rotacion = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, blank=True)
    id_Producto = models.ForeignKey(Producto, on_delete=models.PROTECT, null=True)
    numero_lote = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'consultarInv_lote'

class Lote_Historial(models.Model):
    id_lote = models.ForeignKey(Lote, on_delete=models.PROTECT, null=True)
    id_historial = models.ForeignKey(Historial, on_delete=models.PROTECT, null=True)
    cantidad = models.DecimalField(max_digits=9, decimal_places=0)
    unidad_medida = models.CharField(max_length=20)
    precio_compra = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'consultarInv_lote_historial'