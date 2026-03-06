from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Veiculo, VeiculoHistorico, Condutor
from .forms import VeiculoForm, CondutorForm

@login_required
def dashboard(request):
    veiculos_propria = Veiculo.objects.filter(tipo_frota='Própria').order_by('placa')
    veiculos_agregada = Veiculo.objects.filter(tipo_frota='Agregado').order_by('placa')
    return render(request, 'APP_FROTA/dashboard.html', {
        'veiculos_propria': veiculos_propria,
        'veiculos_agregada': veiculos_agregada,
    })

@login_required
def veiculo_list(request):
    veiculos = Veiculo.objects.all()
    return render(request, 'APP_FROTA/veiculo_list.html', {'veiculos': veiculos})

@login_required
def veiculo_create(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo cadastrado com sucesso!')
            return redirect('APP_FROTA:veiculo_list')
    else:
        form = VeiculoForm()
    
    return render(request, 'APP_FROTA/veiculo_form.html', {'form': form})

@login_required
def veiculo_detail(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'edit':
            form = VeiculoForm(request.POST, request.FILES, instance=veiculo)
            if form.is_valid():
                form.save()
                messages.success(request, 'Veículo atualizado com sucesso!')
                return redirect('APP_FROTA:veiculo_detail', pk=veiculo.pk)
        elif action == 'add_note':
            nota = request.POST.get('observacao')
            if nota:
                VeiculoHistorico.objects.create(veiculo=veiculo, descricao=f"Observação: {nota}")
                messages.success(request, 'Observação adicionada ao histórico!')
            return redirect('APP_FROTA:veiculo_detail', pk=veiculo.pk)
    else:
        form = VeiculoForm(instance=veiculo)
        
    historico = veiculo.historico.all()
    
    return render(request, 'APP_FROTA/veiculo_detail.html', {
        'veiculo': veiculo,
        'form': form,
        'historico': historico
    })

@login_required
def veiculo_delete(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        placa = veiculo.placa
        veiculo.delete()
        messages.success(request, f'Veículo {placa} excluído com sucesso.')
        return redirect('APP_FROTA:veiculo_list')
    # If standard GET, we could render a confirmation page, or handle via JS modals. Let's provide a basic confirmation template just in case.
    return render(request, 'APP_FROTA/veiculo_confirm_delete.html', {'veiculo': veiculo})

@login_required
def condutor_list(request):
    condutores = Condutor.objects.all().order_by('nome')
    return render(request, 'APP_FROTA/condutor_list.html', {'condutores': condutores})

@login_required
def condutor_create(request):
    if request.method == 'POST':
        form = CondutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Condutor cadastrado com sucesso!')
            return redirect('APP_FROTA:condutor_list')
    else:
        form = CondutorForm()
    
    return render(request, 'APP_FROTA/condutor_form.html', {'form': form})

@login_required
def condutor_delete(request, pk):
    condutor = get_object_or_404(Condutor, pk=pk)
    if request.method == 'POST':
        nome = condutor.nome
        condutor.delete()
        messages.success(request, f'Condutor {nome} excluído com sucesso.')
    return redirect('APP_FROTA:condutor_list')
