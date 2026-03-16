from django.shortcuts import render
from django.http import JsonResponse
from .models import PresenteEscolhido, ConfirmarPresença


# Create your views here.
def home(request):
    return render(request, 'index.html')


def salvar_presente(request):

    if request.method == "POST":

        nome = request.POST.get("nome")
        presente = request.POST.get("presente")

        if PresenteEscolhido.objects.filter(presente=presente).exists():
            return JsonResponse ({
                "status": "erro",
                "mensagem":"Esse presente já foi escolhido."
            })

        PresenteEscolhido.objects.create(
            nome_convidado=nome,
            presente=presente
        )

        return JsonResponse({
            "status":"ok"
        })


def presentes_escolhidos(request):

    presentes = PresenteEscolhido.objects.values_list("presente", flat=True)

    return JsonResponse(list(presentes), safe=False)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def confirmar_presenca(request):

    if request.method == "POST":

        nome = request.POST.get("nome")

        ConfirmarPresença.objects.create(
            nome=nome
        )

        return JsonResponse({"status": "ok"})