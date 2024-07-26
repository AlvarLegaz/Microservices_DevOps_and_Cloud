Deploy MongoDB using Podman.

1. Search MongoDB image in docker.io repo.
	```
	podman search docker.io/mongodb
	```
	docker.io/bitnami/mongodb has been chosen.

2. Pull image from repo
	```
	podman pull docker.io/bitnami/mongodb
	````
3. Check if image has been pulled
	```
	podman images
	```
4. Creater and run container
	```
	podman run -dt -p 27017:27017 docker.io/bitnami/mongodb
5. Check if container has been created
	```
	podman ps
	```
6. Connect to MongoDB using MongoDB Compass or other interface.	