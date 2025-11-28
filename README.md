# 🚓 VTCheck --- Sistema de Gestão de Viaturas Policiais

O **VTCheck** é uma aplicação web desenvolvida em **Django** para
gerenciamento de viaturas policiais e autenticação de usuários da
corporação.\
O sistema oferece cadastro seguro, login, estrutura organizada de apps e
base sólida para expansão (monitoramento, ordens de patrulha, checklist
de viaturas etc.).

## 🧱 Tecnologias Utilizadas

-   Python 3.13.5
-   Django 5.1.14
-   django.contrib.auth (autenticação)
-   python-dotenv
-   HTML5 + CSS3
-   Google Fonts

## 📁 Estrutura do Projeto

    VTCheck/
    │── VTCheck/
    │── user/
    │── police_car/
    │── static/
    │   └── css/
    │       └── styles.css
    │── templates/
    │── manage.py
    │── .env
    │── .gitignore
    │── requirements.txt
    └── README.md

## ⚙️ Configuração do Ambiente

### 1️⃣ Criar ambiente virtual

``` bash
python -m venv venv
```

### 2️⃣ Instalar dependências

``` bash
pip install -r requirements.txt
```

### 3️⃣ Criar arquivo .env

    SECRET_KEY=sua_chave_secreta

### 4️⃣ Aplicar migrações

``` bash
python manage.py migrate
```

### 5️⃣ Criar superusuário

``` bash
python manage.py createsuperuser
```

### 6️⃣ Executar servidor

``` bash
python manage.py runserver
```

## 🚀 Funcionalidades

### 🔐 App user

-   Cadastro
-   Login / Logout
-   Feedback com mensagens do Django

### 🚓 App police_car

-   Cadastro de viaturas
-   Base pronta para expansão

## 🎨 Arquivos Estáticos (CSS)

    static/
    └── css/
        └── styles.css
