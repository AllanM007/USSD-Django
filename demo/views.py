from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, request 


#@require_http_methods(["POST"])
@csrf_exempt
def ussd_callback(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON What would you want to check? \n"
            response += "1. My Phone Number \n"
            response += "2. My Session ID \n"
            response += "3. My Service Code \n"
            response += "4. My Text"

        elif text == "1":
            response = "END My Phone number is {0}".format(phone_number)
        
        elif text == "2":
            response = "END My Session ID is {0}".format(session_id)
        
        elif text == "3":
            response = "END My Service Code is {0}".format(service_code)
        
        elif text == "4":
            response = "END My Text is {0}".format(text)
            
        return HttpResponse(response, content_type='text/plain')
    
    else:
        response = "Wamlambez"

    return HttpResponse(response, content_type='text/plain')