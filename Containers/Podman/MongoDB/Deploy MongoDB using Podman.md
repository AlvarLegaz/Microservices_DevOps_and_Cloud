# Setting Up MongoDB with Podman

1. **Locate the MongoDB Image in the docker.io Repository**
	```bash
	podman search docker.io/mongodb
	```
	The chosen image is docker.io/bitnami/mongodb.

2. **Retrieve the Image from the Repository**
	```bash
	podman pull docker.io/bitnami/mongodb
	```

3. **Verify the Successful Retrieval of the Image**
	```bash
	podman images
	```

4. **Establish and Initiate the Container**
	```bash
	podman run -dt -p 27017:27017 docker.io/bitnami/mongodb
	```
	The `-dt` parameter ensures the process runs in the background, preventing the console from hanging.
	The `-p` parameter maps the external port to the internal one.
	The name of the image for the container is required.

5. **Confirm the Successful Creation of the Container**
	```bash
	podman ps
	```

6. **Access MongoDB Using MongoDB Compass or an Alternative Interface**

7. **Perform a Simple Test of the Database**
	```bash
	echo 'db.runCommand({ connectionStatus: 1 })' | podman exec -i [container_id] mongo
	```
	Replace `[container_id]` with the ID of your container. This command checks the status of the MongoDB connection.

	Please replace `[container_id]` with the actual ID of your container. You can find the ID by running `podman ps`.

8. **Stop the Container**
	```bash
	podman stop [container_id]
	```
	Replace `[container_id]` with the ID of your container.

9. **Start the Container**
	```bash
	podman start [container_id]
	```
	Replace `[container_id]` with the ID of your container.

10. **Destroy the Container**
	```bash
	podman rm [container_id]
	```
	Replace `[container_id]` with the ID of your container.