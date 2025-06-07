from django.shortcuts import render
#from django.http import HttpResponse
#from imcApp.models import Profile


def calculadora_view(request):
    imc = None
    categoria = None


    if request.method == "GET" and 'peso' in resquest.GET and 'altura' in request.GET:
        try:
            peso = float(resquest.GET.get('peso'))
            altura = float(request.GET.get('altura'))

            if altura > 0:
                imc = round(peso / (altura ** 2), 2)

                if imc < 18.5:
                    categoria = 'Abaixo peso'

                elif 18.5 <= imc < 24.9:
                    categoria = 'Peso normal'

                elif 25 <= imc < 29.9:
                    categoria = 'Sobrepeso'

                elif 30 <= imc < 35:
                    categoria = 'Obesidade grau I'

                elif 35 <= imc < 40:
                    categoria = 'Obesidade grau II'

                else:
                    categoria = 'Obesidade grau III'

        except (ValueError, TypeError):
            imc = None
            categoria = 'Valores inválidos'

    return render(request, 'imc/calculadora.html', {'imc':imc, 'categoria':categoria}, status=200)
