from django.db import models

class Condutor(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    cnh = models.CharField(max_length=20, unique=True, verbose_name="Número da CNH")
    validade_cnh = models.DateField(verbose_name="Validade da CNH")
    telefone = models.CharField(max_length=20, verbose_name="Telefone")
    cnh_upload = models.FileField(upload_to='documentos/cnh/', blank=True, null=True, verbose_name="CNH")

    def __str__(self):
        return self.nome

    @property
    def cnh_filename(self):
        import os
        return os.path.basename(self.cnh_upload.name) if self.cnh_upload else ''

    @property
    def telefone_limpo(self):
        if not self.telefone:
            return ''
        import re
        return re.sub(r'\D', '', self.telefone)

    @property
    def whatsapp_url(self):
        clean = self.telefone_limpo
        if not clean:
            return '#'
        return f"https://wa.me/55{clean}" if len(clean) <= 11 else f"https://wa.me/{clean}"

class Veiculo(models.Model):
    TIPO_FROTA_CHOICES = [
        ('Própria', 'Própria'),
        ('Agregado', 'Agregado'),
    ]

    tipo_frota = models.CharField(max_length=20, choices=TIPO_FROTA_CHOICES, verbose_name="Frota (Própria ou Agregado)")
    condutor = models.ForeignKey(Condutor, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Condutor", related_name="veiculos")
    placa = models.CharField(max_length=10, unique=True, verbose_name="Placa")
    crlv_upload = models.FileField(upload_to='documentos/crlv/', blank=True, null=True, verbose_name="CRLV")
    marca = models.CharField(max_length=50, verbose_name="Marca")
    modelo = models.CharField(max_length=100, verbose_name="Modelo")
    ano_fabricacao = models.IntegerField(verbose_name="Ano Fabricação")
    ano_modelo = models.IntegerField(verbose_name="Ano Modelo")
    
    seguradora = models.CharField(max_length=100, verbose_name="Seguradora")
    vigencia = models.DateField(verbose_name="Vigência")
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor da Parcela")
    data_primeiro_vencimento = models.DateField(verbose_name="Data do Primeiro Vencimento")
    numero_parcelas = models.IntegerField(verbose_name="Número de Parcelas")
    
    tipo_cobertura = models.CharField(max_length=50, verbose_name="Tipo de Cobertura")
    franquia = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Franquia")
    danos_materiais = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Danos Materiais")
    danos_corporais = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Danos Corporais")
    danos_morais = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Danos Morais")
    app_morte = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="APP Morte")
    app_invalidez = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="APP Invalidez")
    assistencia_km = models.IntegerField(verbose_name="Assistência 24 Horas (KM)")
    carro_reserva_dias = models.IntegerField(verbose_name="Carro Reserva (Dias)")
    vidros = models.BooleanField(default=False, verbose_name="Vidros (Sim/Não)")

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        changes = []
        if not is_new:
            try:
                orig = Veiculo.objects.get(pk=self.pk)
                for field in self._meta.fields:
                    if field.name in ['id', 'cnh_upload', 'crlv_upload']:
                        continue # File comparisons require special handling, skipping for simplicity now
                    orig_val = getattr(orig, field.name)
                    new_val = getattr(self, field.name)
                    if orig_val != new_val:
                        p_orig = str(orig_val) if orig_val is not None else 'Nenhum'
                        p_new = str(new_val) if new_val is not None else 'Nenhum'
                        changes.append(f"Alteração de '{field.verbose_name}' de '{p_orig}' para '{p_new}'")
            except Veiculo.DoesNotExist:
                pass
                
        super(Veiculo, self).save(*args, **kwargs)
        
        # We need to import VeiculoHistorico here to avoid circular dependencies at module level if they arise
        if is_new:
            VeiculoHistorico.objects.create(veiculo=self, descricao="Veículo cadastrado.")
        elif changes:
            descricao = " | ".join(changes)
            VeiculoHistorico.objects.create(veiculo=self, descricao=descricao)

    def __str__(self):
        return f"{self.placa} - {self.modelo} ({self.tipo_frota})"

    @property
    def crlv_filename(self):
        import os
        return os.path.basename(self.crlv_upload.name) if self.crlv_upload else ''

class VeiculoHistorico(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='historico')
    data_hora = models.DateTimeField(auto_now_add=True, verbose_name="Data e Hora")
    descricao = models.TextField(verbose_name="Descrição")

    class Meta:
        ordering = ['-data_hora']

    def __str__(self):
        return f"[{self.data_hora.strftime('%d/%m/%Y %H:%M')}] {self.veiculo.placa} - {self.descricao[:50]}"
