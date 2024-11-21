from django.http import JsonResponse
from .queries import historial_productos
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime

#cambiar formato de la fecha
class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return super().default(obj)
#Funcion para traer la consulta del historial
def historial_productos_view(request):
    try:
        productos = historial_productos()
        
        return JsonResponse({
            'status': 'success',
            'data': list(productos),
            'message': 'Historial completo de productos ordenado por fecha'
        }, encoder=CustomJSONEncoder)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)