# tankbot
The project to build a tank that uses fast API and a flutter app to control


## to deploy do the following:

### build the docker file locally.

```
docker build -t robotank-api:0.1 -t robotank-api:latest .
```

### save the docker image as a tar to sent to strongbrew

```
docker save robotank-api -o "C:\Playground\Sinic Website\tar files\robotank-api.tar"
```

### then run the below to copy to server:

```
scp "C:\Playground\Sinic Website\tar files\robotank-api.tar" sinic@192.168.4.199:/home/sinic
```

### then go to the server and run the below command:

```
 docker load -i robotank-api.tar
```