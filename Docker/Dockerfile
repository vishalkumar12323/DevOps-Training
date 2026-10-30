## Base image do you want to use.
FROM python:3.11.18-alpine3.23

## Set the working directory inside the container.
WORKDIR /src/app

## Copy source code files to the working directory inside the container.
COPY python-app.py .

## Define the command to run when the container starts.
CMD [ "python", "/src/app/python-app.py" ]