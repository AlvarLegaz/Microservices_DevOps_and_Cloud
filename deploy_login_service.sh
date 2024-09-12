echo off

echo Deploy Login service

# Step 3: Establish and Initiate the Container
echo "Creating and running the container..."
container_id=$(podman run -dt -p 27017:27017 docker.io/bitnami/mongodb)

# Step 4: Confirm the Successful Creation of the Container
echo "Confirming the container has been created..."
podman ps


echo Deploy API LOGIN at PORT 3000
export PYTHONPATH=.
export FLASK_APP=./app/microservices/login/api_login.py
flask --debug run -h 0.0.0.0 -p 3000


