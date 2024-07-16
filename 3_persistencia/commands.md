# Criar um volume
docker volume create myvolume

# Executar um container com um volume
docker run -d --name mycontainer -v myvolume:/data busybox

# Verificar a criação do volume
docker volume inspect myvolume

# Criar um arquivo no volume (dentro do container)
docker exec mycontainer sh -c "echo 'Hello World' > /data/hello.txt"

# Parar e remover o container
docker stop mycontainer
docker rm mycontainer

# Executar outro container usando o mesmo volume
docker run --rm -v myvolume:/data busybox cat /data/hello.txt



# Executar um container com bind mount
docker run -d --name mybindcontainer -v /path/host:/data busybox

# Criar um arquivo no bind mount (dentro do container)
docker exec mybindcontainer sh -c "echo 'Hello from bind mount' > /data/hello.txt"

# Verificar o arquivo no sistema de arquivos do host
cat /path/host/hello.txt
