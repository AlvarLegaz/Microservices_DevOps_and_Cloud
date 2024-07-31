echo Deploying Services Script ...

echo Create POD and map sercices ports
podman pod create --name users_services_pod -p 3000:3000 -p 27017:27017

echo Create login_service container in pod using image container
podman run -d --pod users_services_pod --name login_service localhost/login_service:latest
podman run -d --pod users_services_pod --name users_database docker.io/bitnami/mongodb:latest

echo Show deploy pod and container
podman ps --pod

echo Init Database

# Variables
CONTAINER_NAME="users_database"
DB_NAME="my_users_db"
COLLECTION_NAME="users"
DATA_FILE="Containers/Podman/init_my_users_db.json"

# Asegúrate de que el contenedor esté en ejecución
podman start $CONTAINER_NAME

# Copia el archivo JSON al contenedor
podman cp $DATA_FILE $CONTAINER_NAME:/tmp/init_my_users_db.json

# Ejecuta el comando mongoimport dentro del contenedor
podman exec -it $CONTAINER_NAME mongoimport --db $DB_NAME --collection $COLLECTION_NAME --file /tmp/init_my_users_db.json

# Verifica la importación
podman exec -it $CONTAINER_NAME mongosh --eval "use $DB_NAME; db.$COLLECTION_NAME.find().pretty()"