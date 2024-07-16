# Rodar um container MySQL
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=mydb -d mysql:latest


--name mysql-container: Nome do container.
-e MYSQL_ROOT_PASSWORD=rootpassword: Define a senha do usuário root.
-e MYSQL_DATABASE=mydatabase: Cria um banco de dados chamado mydatabase.
-v mysql-data:/var/lib/mysql: Monta o volume para persistência de dados.
-d mysql:latest: Usa a imagem mais recente do MySQL.


# Verificar o container MySQL
docker logs mysql-container

# Conectar ao MySQL a partir do host
docker exec -it mysql-container mysql -uroot -proot mydb


### Conectar ao Container MySQL a partir do Host e de Outros Containers


#### Conectar a partir do Host
Você pode usar o cliente MySQL instalado no seu host para se conectar ao container:


mysql -h 127.0.0.1 -P 3306 -u root -p
-h 127.0.0.1: Host (localhost).
-P 3306: Porta (3306 é a porta padrão do MySQL).
-u root: Usuário (root).
-p: Solicita a senha do usuário root (use a senha rootpassword definida anteriormente).


#### Conectar a partir de Outro Container
Você pode usar um segundo container para se conectar ao MySQL:

Executar um Container MySQL Client:

docker run -it --rm --network container:mysql-container mysql mysql -h127.0.0.1 -uroot -p
--network container:mysql-container: Usa a rede do container mysql-container.
mysql: Inicia o cliente MySQL.
-h127.0.0.1 -uroot -p: Parâmetros de conexão.


### Integração python

docker build -t python-mysql-app .
docker run --rm --name python-app --network container:mysql-container python-mysql-app
