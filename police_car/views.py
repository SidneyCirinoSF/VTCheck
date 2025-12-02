from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Viatura

@login_required
def dashboard(request):
    viaturas = Viatura.objects.all().order_by('prefixo')
    return render(request, 'police_car/dashboard.html', {
        'viaturas': viaturas,
    })

@login_required
def editar_viatura(request, id):
    viatura = get_object_or_404(Viatura, id=id)

    if request.method == "POST":
        viatura.placa = request.POST.get("placa", viatura.placa)
        viatura.prefixo = request.POST.get("prefixo", viatura.prefixo)
        viatura.modelo = request.POST.get("modelo", viatura.modelo)
        ano = request.POST.get("ano")
        viatura.ano = int(ano) if ano else None
        viatura.status = request.POST.get("status", viatura.status)
        viatura.descricao_problema = request.POST.get("descricao_problema", viatura.descricao_problema)
        viatura.save()
        return redirect('police_car:dashboard')

    # monta lista de choices para o template (key, label)
    status_choices = [(k, v) for k, v in Viatura.STATUS_CHOICES]
    return render(request, 'police_car/editar_viatura.html', {
        'viatura': viatura,
        'status_choices': status_choices,
    })

@login_required
def deletar_viatura(request, id):
    viatura = get_object_or_404(Viatura, id=id)
    if request.method == "POST":
        viatura.delete()
        return redirect('police_car:dashboard')
    # GET -> mostrar confirmação
    return render(request, 'police_car/confirmar_delete.html', {
        'viatura': viatura,
    })
