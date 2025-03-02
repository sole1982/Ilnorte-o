from django.shortcuts import render, redirect
from .models import Seccion, Galeria, Reseña
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
def index(request):
    fotos = Galeria.objects.all()
    reseñas = Reseña.objects.order_by('-fecha_creacion')
    return render(request, "index.html", {"galeria": fotos,'reseñas': reseñas })




def menu(request):
    secciones = Seccion.objects.prefetch_related("platos").all()
    return render(request, "menu.html", {"secciones": secciones})




@csrf_exempt  # Para evitar problemas con CSRF (si usas fetch en frontend)
@require_POST  # Solo permite métodos POST
def agregar_reseña(request):
    nombre = request.POST.get('nombreUsuario')  # Ajustado al name del input en el formulario
    comentario = request.POST.get('comentario')
    puntuacion = request.POST.get('puntuacion')

    if nombre and comentario and puntuacion:
        try:
            nueva_reseña = Reseña.objects.create(
                nombre=nombre,
                comentario=comentario,
                puntuacion=int(puntuacion)
            )
            return JsonResponse({'success': True, 'nombre': nueva_reseña.nombre, 'comentario': nueva_reseña.comentario, 'puntuacion': nueva_reseña.puntuacion})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Datos inválidos'})
