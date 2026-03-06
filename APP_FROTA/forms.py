from django import forms
from .models import Veiculo, Condutor

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
        widgets = {
            'vigencia': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'data_primeiro_vencimento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'crlv_upload': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(VeiculoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Only add specific classes if we need to override the base.html generic styling,
            # but standard char/number fields will inherit the base.html input CSS. 
            field.widget.attrs['class'] = 'form-control'
            
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] = 'form-file-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'

class CondutorForm(forms.ModelForm):
    class Meta:
        model = Condutor
        fields = '__all__'
        widgets = {
            'validade_cnh': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'cnh_upload': forms.FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CondutorForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
