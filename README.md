# Gestão de Frota - Luparele

Sistema de gerenciamento de frotas e condutores desenvolvido em Django, preparado para deploy no PythonAnywhere.

## 🚀 Funcionalidades

- **Dashboard**: Visão geral e indicadores do sistema.
- **Gestão de Veículos**: Cadastro, consulta, edição e exclusão de veículos da frota.
- **Gestão de Condutores**: Controle completo de motoristas e suas informações.
- **Relatórios**: Geração de relatórios e exportação de dados (PDF, Excel).
- **Controle de Acesso**: Sistema de login e permissões diferenciadas para Superusuários.
- **PWA (Progressive Web App)**: Interface responsiva e otimizada para uso mobile.

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.12, Django 6.0
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Banco de Dados**: SQLite3 (desenvolvimento) / PostgreSQL (recomendado para produção)
- **Hospedagem**: PythonAnywhere

## 📦 Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/Luparele/GESTAO_FROTA.git
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

3. Ative o ambiente virtual:
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## 🌐 Deploy (PythonAnywhere)

O projeto está configurado para o domínio: [frota.pythonanywhere.com](https://frota.pythonanywhere.com)

---
Desenvolvido por Luparele.
