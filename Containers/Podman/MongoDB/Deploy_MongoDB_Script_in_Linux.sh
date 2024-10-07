#!/bin/bash

# Step 1: Retrieve the Image from the Repository
echo "Pulling MongoDB image from docker.io repository..."
podman pull docker.io/bitnami/mongodb

# Step 2: Verify the Successful Retrieval of the Image
echo "Verifying the image has been pulled..."
podman images

# Step 3: Establish and Initiate the Container
echo "Creating and running the container..."
container_id=$(podman run -dt -p 27017:27017 docker.io/bitnami/mongodb)

# Step 4: Confirm the Successful Creation of the Container
echo "Confirming the container has been created..."
podman ps

# Step 5: Access MongoDB Using MongoDB Compass or an Alternative Interface
echo "Accessing MongoDB..."

# Simple test of the database
echo "Testing the database..."
echo 'db.runCommand({ connectionStatus: 1 })' | podman exec -i $container_id mongo

echo "Script completed."
