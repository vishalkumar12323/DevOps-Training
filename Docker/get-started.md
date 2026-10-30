# Docker Exercise
## Run a python file using docker and docker image.
### Pull the python lightweight image from docker hub:
```bash
docker pull python:3.11.18-alpine3.23
```

### Run Python File.
```bash
docker run -v ""/home/vishal/Desktop/DevOps-Training/Docker:/src/app/" python:3.11.18-alpine3.23 python /src/app/python-app.py"
```

### Show all images and containers
```bash
docker images
docker container ls
# or
docker ps
```

### Remove stopped docker container
```bash
docker rm <container-id>, or <container-name>
```

### Remove docker images
```bash
docker image rm <image-id>, or <image-name:tag>
```