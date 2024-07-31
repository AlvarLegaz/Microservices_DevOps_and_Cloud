echo Deploying Services Script ...

echo Create POD and map sercices ports
podman pod create --name users_services_pod -p 3000:3000 -p 27017:27017

echo Create login_service container in pod using image container
podman run -d --pod login_service --name login_service localhost/login_service:latest
podman run -d --pod login_service --name user_database docker.io/bitnami/mongodb:latest

echo Show deploy pod and container
podman ps --pod
