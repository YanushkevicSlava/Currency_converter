from django.shortcuts import render
import requests


def converter_index(request):
    response = requests.get(url='https://v6.exchangerate-api.com/v6/b251f9d75c48903e2b2cae0d/latest/USD').json()
    currencies = response.get("conversion_rates")

    if request.method == "GET":
        context = {
            'currencies': currencies
        }

        return render(request=request, template_name='converter/converter-index.html', context=context)
