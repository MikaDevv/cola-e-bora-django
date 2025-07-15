Cola & Bora 🚀
Plataforma web para troca de serviços e fortalecimento da economia solidária local.

Status do Projeto: Protótipo Funcional (Em Desenvolvimento)


📖 Sobre o Projeto
Cola & Bora é uma solução web desenvolvida para resolver um problema comum em comunidades: a dificuldade em conectar pessoas que precisam de ajuda em tarefas do dia a dia com aquelas que podem oferecer essas habilidades.

Através de uma interface simples, o projeto permite que usuários cadastrem ofertas ou pedidos de ajuda, utilizando uma moeda social chamada "Bora" como meio de troca. O objetivo é criar um ecossistema colaborativo que valoriza talentos locais, fortalece os laços comunitários e promove uma alternativa à economia tradicional.


✨ Funcionalidades
Mural de Tarefas: Visualização de todos os serviços oferecidos e solicitados na comunidade.

Publicação de Tarefas: Usuários podem criar novas postagens, definindo o tipo de tarefa (oferta ou pedido), categoria e valor em "Boras".

Sistema de Moeda Social: Estrutura de dados pronta para gerenciar o saldo de "Boras" de cada usuário.

Categorias de Serviços: Organização das tarefas para facilitar a navegação.


🛠️ Tecnologias Utilizadas
Backend: Python 3, Django

Frontend: HTML, CSS, Bootstrap 5

Banco de Dados (Desenvolvimento): SQLite3

Controle de Versão: Git & GitHub


⚙️ Como Rodar o Projeto Localmente
Siga os passos abaixo para configurar e executar o projeto em seu ambiente de desenvolvimento.

Pré-requisitos
Antes de começar, você vai precisar ter as seguintes ferramentas instaladas em sua máquina:

- Python 3
- Git


*Instalação*
Clone o repositório:

git clone [URL_DO_SEU_REPOSITORIO_AQUI]
Acesse a pasta do projeto:

cd nome-da-pasta-do-projeto
Crie e ative um ambiente virtual:

# Cria o ambiente
python -m venv venv

# Ativa o ambiente
# No Windows (PowerShell):
venv\Scripts\Activate.ps1
# No Linux ou macOS:
source venv/bin/activate

Instale as dependências do projeto:

pip install -r requirements.txt

Aplique as migrações do banco de dados:

python manage.py migrate

Crie um superusuário para acessar a área de Admin:

python manage.py createsuperuser
Siga as instruções no terminal para criar seu usuário e senha.

Execute a aplicação:

python manage.py runserver

Pronto! Agora você pode acessar a aplicação em seu navegador no endereço http://127.0.0.1:8000/.