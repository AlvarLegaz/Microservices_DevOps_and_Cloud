# Installing MongoDB on Windows 10 

## 0. Youtube installation tutorial
https://www.youtube.com/watch?v=gB6WLkSrtJk&ab_channel=ProgrammingKnowledge

## 1. Download and Installation
- Go to the official MongoDB website and download the **Community Server** version for Windows. 
https://www.mongodb.com/products/self-managed/community-edition
- Run the downloaded installer and follow the installation wizard. 
- Install MongoDB as service and create the paths of Data directory and Log directory.
- You can also install **MongoDB Compass**, a graphical tool for managing MongoDB.

## 2. Data Folder  
- Inside the `data` folder, create another folder named `db` (e.g., `C:\data\db`). This will be the location where MongoDB stores data.

## 3. Start the MongoDB Server 
- Open a command prompt (cmd) as an administrator.
- Navigate to the folder where you installed MongoDB (usually `C:\Program Files\MongoDB\Server\4.4\bin`).
- Execute the following command to start the MongoDB server:
```
  mongod
```

## 4. Connect to the Database
- Open another command prompt and navigate to the same location (`C:\Program Files\MongoDB\Server\4.4\bin`).
- Run the following command to connect to the server:
```
mongo
```

- ## 5. Verification
- You should see a line indicating that you are connected to the MongoDB server.
- You can run commands like `show dbs` to list available databases.
