import os
import django
import random
from datetime import date, timedelta
from decimal import Decimal

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PRJETO_FROTA.settings')
django.setup()

from APP_FROTA.models import Condutor, Veiculo, VeiculoHistorico

def povoar():
    print("Iniciando povoamento do banco de dados...")
    
    # Limpar dados existentes para ter um estado limpo conforme solicitado
    VeiculoHistorico.objects.all().delete()
    Veiculo.objects.all().delete()
    Condutor.objects.all().delete()
    
    nomes = [
        "João Silva", "Maria Oliveira", "Pedro Santos", "Ana Souza", "Carlos Lima",
        "Juliana Costa", "Lucas Ferreira", "Beatriz Alves", "Ricardo Pereira", "Fernanda Rodrigues",
        "Gabriel Castro", "Camila Gomes", "Bruno Rocha", "Larissa Martins", "Thiago Ribeiro",
        "Amanda Carvalho", "Roberto Xavier", "Patrícia Melo", "Marcelo Barros", "Vanessa Cunha"
    ]
    
    marcas_modelos = [
        ("Volkswagen", "Gol"), ("Fiat", "Uno"), ("Chevrolet", "Onix"), ("Hyundai", "HB20"),
        ("Ford", "Ka"), ("Toyota", "Corolla"), ("Honda", "Civic"), ("Renault", "Sandero"),
        ("Jeep", "Compass"), ("Nissan", "Versa")
    ]
    
    seguradoras = ["Porto Seguro", "Azul Seguros", "Allianz", "Liberty Seguros", "Mapfre", "Tokio Marine", "Bradesco Seguros"]

    condutores = []
    print("Criando 20 condutores...")
    for i in range(20):
        c = Condutor.objects.create(
            nome=nomes[i],
            cpf=f"{random.randint(100,999)}.{random.randint(100,999)}.{random.randint(100,999)}-{random.randint(10,99)}",
            cnh=f"{random.randint(100000000, 999999999)}",
            validade_cnh=date.today() + timedelta(days=random.randint(30, 1000)),
            telefone=f"(11) 9{random.randint(7000, 9999)}-{random.randint(1000, 9999)}"
        )
        condutores.append(c)

    print("Criando 10 veículos de Frota Própria...")
    for i in range(10):
        marca, modelo = marcas_modelos[i % len(marcas_modelos)]
        Veiculo.objects.create(
            tipo_frota='Própria',
            condutor=condutores[i],
            placa=f"ABC{random.randint(1000, 9999)}",
            marca=marca,
            modelo=modelo,
            ano_fabricacao=2020 + (i % 5),
            ano_modelo=2021 + (i % 5),
            seguradora=random.choice(seguradoras),
            vigencia=date.today() + timedelta(days=random.randint(30, 365)),
            valor_parcela=Decimal(f"{random.uniform(500, 1500):.2f}"),
            data_primeiro_vencimento=date.today() - timedelta(days=random.randint(1, 60)),
            numero_parcelas=random.randint(6, 24),
            tipo_cobertura="Completo",
            franquia=Decimal("2500.00"),
            danos_materiais=Decimal("100000.00"),
            danos_corporais=Decimal("100000.00"),
            danos_morais=Decimal("20000.00"),
            app_morte=Decimal("50000.00"),
            app_invalidez=Decimal("50000.00"),
            assistencia_km=400,
            carro_reserva_dias=15,
            vidros=True
        )

    print("Criando 10 veículos Agregados...")
    for i in range(10, 20):
        marca, modelo = marcas_modelos[i % len(marcas_modelos)]
        Veiculo.objects.create(
            tipo_frota='Agregado',
            condutor=condutores[i],
            placa=f"XYZ{random.randint(1000, 9999)}",
            marca=marca,
            modelo=modelo,
            ano_fabricacao=2018 + (i % 5),
            ano_modelo=2019 + (i % 5),
            seguradora=random.choice(seguradoras),
            vigencia=date.today() + timedelta(days=random.randint(30, 365)),
            valor_parcela=Decimal(f"{random.uniform(300, 800):.2f}"),
            data_primeiro_vencimento=date.today() - timedelta(days=random.randint(1, 30)),
            numero_parcelas=random.randint(4, 12),
            tipo_cobertura='RCV Terceiros',
            franquia=Decimal("1500.00"),
            danos_materiais=Decimal("50000.00"),
            danos_corporais=Decimal("50000.00"),
            danos_morais=Decimal("10000.00"),
            app_morte=Decimal("25000.00"),
            app_invalidez=Decimal("25000.00"),
            assistencia_km=200,
            carro_reserva_dias=7,
            vidros=False
        )

    print("Sucesso! Banco de dados povoado com 20 condutores e 20 veículos.")

if __name__ == "__main__":
    povoar()
