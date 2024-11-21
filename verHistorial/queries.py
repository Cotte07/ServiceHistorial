from django.db.models.functions import Now, Concat, ExtractDay, ExtractMonth, ExtractYear, Extract
from django.db.models import F, Value, CharField, IntegerField, ExpressionWrapper, DateField
from django.db.models.functions import Cast
from typing import List, Dict, Any
from .models import Lote_Historial
#consulta la base de datos los productos con el estado FALSE
def historial_productos(orden_descendente=False):
    orden = '-id_historial__fecha_compra' if orden_descendente else 'id_historial__fecha_compra'
    
    return Lote_Historial.objects.select_related(
        'id_lote',
        'id_lote__id_Producto',
        'id_lote__id_Producto__id_categoria',
        'id_historial'
    ).annotate(
        nombre_producto=F('id_lote__id_Producto__nombre'),
        categoria=F('id_lote__id_Producto__id_categoria__nombre'),
        proveedor=F('id_lote__id_Producto__proveedor'),
        numero_lote=F('id_lote__numero_lote'),
        estado_lote=F('id_lote__estado'),
        fecha_rotacion=F('id_lote__fecha_Rotacion'),
        fecha_compra=F('id_historial__fecha_compra')
    ).values(       #datos a traer de la consulta
        'id_lote',
        'nombre_producto',
        'categoria',
        'proveedor',
        'numero_lote',
        'estado_lote',
        'fecha_rotacion',
        'cantidad',
        'unidad_medida',
        'precio_compra',
        'fecha_compra'
    ).order_by(orden)       #ordena las fechas de la mas actual a la mas vieja 