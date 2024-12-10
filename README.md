# **Guia para Configuração do Projeto**

Este tutorial irá guiá-lo para configurar e executar o projeto em sua máquina local.

---

## **Visão Geral do Projeto**

![BD Eventus](imagens/eventus.png)

Eventus é uma plataforma de gerenciamento de eventos desenvolvida como parte de um projeto acadêmico para a disciplina de Programação Web da UFLA. O sistema permite a divulgação de eventos, o cadastro de usuários e a administração eficiente de eventos e participantes, oferecendo também um painel administrativo completo para facilitar o gerenciamento de toda a plataforma.

---

## **1. Pré-requisitos**

- **Python** (versão 3.10 ou superior): [Download Python](https://www.python.org/downloads/)
- **Git** (para clonar o repositório): [Download Git](https://git-scm.com/)

---

## **2. Clonar o Repositório**

Faça o clone do repositório do projeto em sua máquina local.
```bash
git clone https://github.com/AgostiniGuilherme/Eventus.git
   ```

## **3. Criar um Ambiente Virtual**

Crie e ative um ambiente virtual para o projeto:

### **No Windows**:
1. Crie o ambiente virtual:
   ```bash
   Set-ExecutionPolicy Unrestricted -Scope Process
   python -m venv venv
   ```

2. Ative o ambiente virtual:
   ```bash
   venv\Scripts\activate
   ```

   Ou:
    ```bash
   venv\Scripts\Activate.ps1  
   ```


## **4. Instalar Dependências**

Com o ambiente virtual ativado, instale o Django:

```bash
pip install Django
```

---

## **5. Configurar o Banco de Dados**

Execute as migrações para configurar o banco de dados:

```bash
python manage.py migrate
```

---

## **6. Criar um Superusuário**

Se desejar acessar o painel administrativo do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

Siga as instruções fornecidas no terminal para definir o nome de usuário, email e senha.

---

## **7. Rodar o Servidor Local**

Execute o servidor de desenvolvimento do Django para testar o projeto:

```bash
python manage.py runserver
```

Acesse o projeto no navegador no seguinte endereço:
```
http://127.0.0.1:8000/
```

---

## **10. Finalização**

Parabéns! O projeto está configurado e rodando em sua máquina. Agora você pode começar a utilizá-lo ou desenvolvê-lo.

---

© Projeto desenvolvido por Guilherme Noronha de Agostini e Gustavo Viana Avelar Dutra para a disciplina Programação Web, realizada na UFLA - Universidade Federal de Lavras.

---
