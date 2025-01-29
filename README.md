# Eventus 

Eventus é um sistema web desenvolvido com Django para gerenciamento de eventos. Com uma interface intuitiva, ele permite que os usuários criem, editem, visualizem e excluam eventos, além de se inscreverem e gerenciarem suas participações. O sistema também conta com um mecanismo de autenticação para garantir que apenas organizadores possam modificar e excluir seus eventos.

## 📌 Funcionalidades

- 🔹 **Autenticação de Usuário** (Login, Logout e Cadastro)
- 🔹 **CRUD de Eventos** (Criar, Listar, Editar e Deletar eventos)
- 🔹 **Gerenciamento de Participação** (Inscrição, Lista e Cancelamento de Inscrição em eventos)
- 🔹 **Sistema de Mensagens** para feedback ao usuário
- 🔹 **Proteção de Rotas** (Somente organizadores podem editar/deletar seus eventos)

## 🚀 Tecnologias Utilizadas

- **Django** (Back-end)
- **Django Authentication** (Autenticação de usuários)
- **HTML + CSS + Bootstrap** (Front-end)
- **SQLite** (Banco de dados padrão do Django)



## 📂 Estrutura do Projeto

```
Eventus/
│-- manage.py
│-- eventus/
│   │-- settings.py
│   │-- urls.py
│-- gerenciador_eventos/
│   │-- urls.py
│   │-- views.py
│   │-- models.py
│   │-- forms.py
|   |-- admin.py
|   |-- apps.py
|   │-- templates/
│   │   |-- principal.html
│   │   |-- login.html
│   │   |-- cadastrar.html
│   │   |-- meus_eventos.html
│   │   |-- listar_eventos.html
│   │   |-- detalhar_evento.html
│   │   |-- criar_evento.html
│   │   |-- editar_evento.html
│   │   |-- deletar_evento.html
```


### 📊 Modelo do Banco de Dados  

![BD Eventus](imagens/eventus.png)

---

## 🔗 **Rotas e Endpoints**

| Rota | Método | Descrição |
|------|--------|-------------|
| `/` | GET | Página principal |
| `/auth/cadastrar/` | POST | Cadastro de usuário |
| `/auth/login/` | POST | Login de usuário |
| `/auth/logout/` | GET | Logout do sistema |
| `/meus-eventos/` | GET | Lista eventos que o usuário participa |
| `/eventos/` | GET | Lista todos os eventos |
| `/eventos/criar/` | POST | Criar um novo evento |
| `/eventos/<id>/` | GET | Detalhes de um evento |
| `/eventos/<id>/editar/` | PUT | Editar um evento |
| `/eventos/<id>/deletar/` | DELETE | Deletar um evento |
| `/evento/<id>/inscrever/` | POST | Inscrever-se em um evento |
| `/evento/<id>/cancelar-inscricao/` | DELETE | Cancelar inscrição |

---

## 📌 Como Rodar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/AgostiniGuilherme/Eventus.git
cd eventus
```

### 2️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar o banco de dados
```bash
python manage.py migrate
```

### 5️⃣ Criar um superusuário (opcional, mas útil para testes)
```bash
python manage.py createsuperuser
```

### 6️⃣ Rodar o servidor
```bash
python manage.py runserver
```
Acesse no navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🛠 Como Contribuir
1. **Fork** este repositório
2. Crie uma nova branch: `git checkout -b minha-feature`
3. Faça as alterações e commit: `git commit -m 'Adicionando nova feature'`
4. Envie para o repositório remoto: `git push origin minha-feature`
5. Abra um **Pull Request** 🚀

---
💡 **Eventus** - Sistema de gerenciamento de eventos desenvolvido em Django. 

© Projeto desenvolvido por Guilherme Noronha de Agostini e Gustavo Viana Avelar Dutra para a disciplina Programação Web, realizada na UFLA - Universidade Federal de Lavras.
