from django.shortcuts import render,redirect
from django.http import JsonResponse
from django_esewa import generate_signature
import uuid
def home(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount', 0))
        product_delivery_charge = float(request.POST.get('product_delivery_charge', 0))
        product_service_charge = float(request.POST.get('product_service_charge', 0))
        tax_amount = float(request.POST.get('tax_amount', 0))
        product_code = request.POST.get('product_code', 'EPAYTEST')
        total_amount_float = amount + tax_amount + product_delivery_charge + product_service_charge
        total_amount = "{:.2f}".format(total_amount_float)  
        transaction_uuid = str(uuid.uuid4())
        signed_field_names = "total_amount,transaction_uuid,product_code"
        payload = {
            "total_amount": total_amount,
            "transaction_uuid": transaction_uuid,
            "product_code": product_code,
            "amount": "{:.2f}".format(amount),
            "tax_amount": "{:.2f}".format(tax_amount),
            "product_service_charge": "{:.2f}".format(product_service_charge),
            "product_delivery_charge": "{:.2f}".format(product_delivery_charge),    
            "success_url": "http://localhost:8000/success/",
            "failure_url": "http://localhost:8000/fail/",
            "signed_field_names": signed_field_names,
        }
        payload["signature"] = generate_signature(total_amount=payload["total_amount"],transaction_uuid=payload["transaction_uuid"],product_code=payload["product_code"])
        print(payload)
        return JsonResponse(payload)
    return render(request, "Home.html")

def sucess(request): return render(request,'Success.html')
def fail(request):return render(request,'fail.html')
def readme(request):return render(request,'Readme.html')

