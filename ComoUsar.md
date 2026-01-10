Como rodar o projeto

Abra o terminal na pasta do projeto (main.py) e execute o comando:

uvicorn main:app --reload


Após iniciar o servidor, abra o navegador e acesse:

http://127.0.0.1:8000/docs


Essa é a interface interativa do FastAPI (Swagger UI), onde você pode testar a API.

Nela, é possível enviar arquivos CSV e visualizar os funcionários cadastrados, separados entre válidos e inválidos.

Bibliotecas utilizadas

O projeto utiliza as seguintes bibliotecas Python:

fastapi – para criar a API.

uvicorn – servidor ASGI para rodar a API.

pandas – manipulação e análise de dados.

sqlalchemy – conexão com o banco de dados SQLite.

python-multipart – para lidar com uploads de arquivos na API.

pytest – para testes automatizados do código.