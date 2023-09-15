from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import requests


def converter_index(request: HttpRequest) -> HttpResponse:
    """ Функция получения курса валют с дальнейшей конвертацией """

    # получение актуального курса валют.
    response = requests.get(url='https://v6.exchangerate-api.com/v6/b251f9d75c48903e2b2cae0d/latest/USD').json()

    currencies = response.get("conversion_rates")

    if request.method == "GET":
        context = {
            'currencies': currencies,
        }

        return render(request=request, template_name='converter/converter-index.html', context=context)

    if request.method == "POST":
        amount = float(request.POST.get('amount'))
        from_amount = request.POST.get('from')
        to_amount = request.POST.get('to')

        # формула расчёта результата конвертации.
        converted_amount = round(currencies[to_amount] / currencies[from_amount] * float(amount), 2)

        context = {
            'currencies': currencies,
            'converted_amount': converted_amount,
        }

        return render(request=request, template_name='converter/converter-index.html', context=context)
