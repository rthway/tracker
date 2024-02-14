
import qrcode
from django.shortcuts import render
from django.http import HttpResponse
from .models import GeneratedSerialNumber
from datetime import datetime
from io import BytesIO

def generate_serial_numbers(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        min_bulk_id = int(request.POST.get('min_bulk_id'))
        max_bulk_id = int(request.POST.get('max_bulk_id'))

        serial_numbers = []
        factory_id = "01"
        lots = datetime.now().strftime("%y%m%d")
        bundle_id = str(min_bulk_id) + "_" + str(max_bulk_id)

        for i in range(min_bulk_id, max_bulk_id + 1):
            serial_number = f"{factory_id}{lots}{bundle_id}{i}"
            serial_numbers.append(serial_number)
            # Save generated serial number to the database
            GeneratedSerialNumber.objects.create(
                product_name=product_name,
                lots=lots,
                bundle_id=bundle_id,
                serial_number=serial_number
            )



        return render(request, 'generated_serial_numbers.html', {
            'product_name': product_name,
            'lots': lots,
            'bundle_id': bundle_id,
            'serial_numbers': serial_numbers

        })
    else:
        return render(request, 'generate_serial_form.html')
    
def serial_number_list(request):
    serial_numbers = GeneratedSerialNumber.objects.all()
    return render(request, 'serial_number_list.html', {'serial_numbers': serial_numbers})
