from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Withdrawal

# Create your views here.

def health_check(request):
    return JsonResponse({"status": "ok"})

def product_locations(request):
    if request.method != 'GET':
        return HttpResponseBadRequest("Only GET allowed")
    data = list(Product.objects.values('sku', 'location'))
    return JsonResponse({"results": data})

@csrf_exempt
def create_withdrawal(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Only POST allowed")
    try:
        body = json.loads(request.body.decode('utf-8'))
        sku = body.get('sku')
        quantity = int(body.get('quantity', 0))
        motive = body.get('motive', '').strip()
        if not sku or quantity <= 0 or not motive:
            return HttpResponseBadRequest("sku, quantity>0 y motive son obligatorios")
        try:
            product = Product.objects.get(sku=sku)
        except Product.DoesNotExist:
            return HttpResponseBadRequest("Producto no existe (cree el producto primero)")
        Withdrawal.objects.create(product=product, quantity=quantity, motive=motive)
        return JsonResponse({"ok": True, "sku": sku, "quantity": quantity, "motive": motive})
    except Exception:
        # táctica de Fallar con gracia
        return HttpResponseBadRequest("No se pudo procesar la solicitud; sistema en recuperación")