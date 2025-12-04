from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Viatura
from django.db.models import Q
from django.contrib import messages

@login_required
def dashboard(request):
    viaturas = Viatura.objects.all().order_by('prefixo', 'placa')

    status_filter = request.GET.get('status')
    if status_filter in ['ok', 'manutencao', 'inoperante']:
        viaturas = viaturas.filter(status=status_filter)

    busca = request.GET.get('q')
    if busca:
        viaturas = viaturas.filter(
            Q(placa__icontains=busca) |
            Q(prefixo__icontains=busca) |
            Q(modelo__icontains=busca)
        )

    total = Viatura.objects.count()
    ok = Viatura.objects.filter(status='ok').count()
    manutencao = Viatura.objects.filter(status='manutencao').count()
    inoperante = Viatura.objects.filter(status='inoperante').count()

    return render(request, 'police_car/dashboard.html', {
        'viaturas': viaturas,
        'total': total,
        'ok': ok,
        'manutencao': manutencao,
        'inoperante': inoperante,
        'busca': busca,
        'status_filter': status_filter,
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

@login_required
def adicionar_viatura(request):
    if request.method == "POST":
        placa = request.POST.get("placa")
        prefixo = request.POST.get("prefixo")
        modelo = request.POST.get("modelo")
        ano = request.POST.get("ano")
        status = request.POST.get("status")
        descricao = request.POST.get("descricao_problema")

        try:
            Viatura.objects.create(
                placa=placa,
                prefixo=prefixo,
                modelo=modelo,
                ano=ano or None,
                status=status,
                descricao_problema=descricao
            )
            messages.success(request, "Viatura adicionada com sucesso!")
            return redirect("police_car:dashboard")

        except Exception as e:
            messages.error(request, f"Erro ao adicionar: {e}")

    return render(request, "police_car/adicionar_viatura.html")


