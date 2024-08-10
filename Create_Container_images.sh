#Create container images

podman build -t login_service:latest ./Containers/Podman/login_service/
podman build -t login_service:latest ./Containers/Podman/todo_service/
