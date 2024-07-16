# Iniciar os serviços definidos no Docker Compose
docker-compose up -d

# Verificar logs dos serviços
docker-compose logs

# Parar e remover os serviços definidos no Docker Compose
docker-compose down

# Iniciar os serviços forçando build dos Dockerfiles
docker-compose up --build
