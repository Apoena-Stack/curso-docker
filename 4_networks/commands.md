# Criar uma rede bridged
docker network create my-bridge-network

# Rodar dois containers na rede bridged
docker run -d --name container1 --network my-bridge-network python:3.9-slim sleep 1000
docker run -d --name container2 --network my-bridge-network python:3.9-slim sleep 1000

# Verificar a comunicação entre os containers
docker exec container1 ping -c 3 container2


Explicação:
Como os containers podem se comunicar usando a rede bridged.
Benefícios de usar redes bridged em ambientes de desenvolvimento e produção.


# Rodar um container na rede host
docker run -d --name myhostcontainer --network host python:3.9-slim sleep 1000

# Verificar a comunicação com serviços locais
docker exec myhostcontainer curl http://localhost:5000


