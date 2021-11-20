from django.shortcuts import render
import requests

# Create your views here.

def Index(request):

    cidade = request.GET.get('cidade')

    if cidade:
        iTOKEN = "b1028450ed2a0dca28af30424d2ed29c"
        iCITY = cidade
        response = requests.get(
            "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=" + str(iCITY) + "&token=" + str(
                iTOKEN)).json()

        context = {
            'response': response
        }
    else:
        iTOKEN = "b1028450ed2a0dca28af30424d2ed29c"
        iCITY = 'Osasco'
        response = requests.get("http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=" + str(iCITY) + "&token=" + str(iTOKEN)).json()

        context = {
            'response': response
        }
    return render(request, 'climatempo/index.html', context)
