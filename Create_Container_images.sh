#Create container images

podman images

podman build -t login_service:latest ./Containers/Podman/login_service/
podman build -t todo_service:latest ./Containers/Podman/todo_service/

podman images