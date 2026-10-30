# Kubernetes Local Development --- Installation & Setup Guide

This guide sets up a local Kubernetes learning environment on:

-   Ubuntu Linux
-   Windows
-   macOS

The setup used by this project is:

-   **Docker** --- container runtime
-   **kubectl** --- Kubernetes command-line client
-   **Minikube** --- local Kubernetes cluster
-   **Docker driver** --- Minikube runs Kubernetes inside Docker

> The commands in this guide are intended for a local
> learning/development environment, not a production Kubernetes cluster.

------------------------------------------------------------------------

## 1. Architecture of the Local Setup

``` text
Your Computer
│
├── Docker
│
├── Minikube
│   └── Kubernetes Cluster
│       ├── Control Plane
│       └── Worker Node
│
└── kubectl
    └── Communicates with the Kubernetes API Server
```

The basic relationship is:

``` text
kubectl → Kubernetes API Server → Minikube Cluster → Containers
```

------------------------------------------------------------------------

# 2. Prerequisites

Before installing Kubernetes tools, make sure your operating system is
supported and virtualization is enabled.

You need:

1.  Docker
2.  kubectl
3.  Minikube
4.  A terminal:
    -   Ubuntu: Terminal
    -   Windows: PowerShell
    -   macOS: Terminal

Recommended hardware for a comfortable learning environment:

-   4 GB+ RAM available for the cluster
-   2+ CPU cores
-   10 GB+ free disk space

------------------------------------------------------------------------

# 3. Ubuntu Linux

## 3.1 Update the system

``` bash
sudo apt update
sudo apt upgrade -y
```

## 3.2 Install Docker

Install Docker using Docker's official Ubuntu installation instructions.

After installation, verify it:

``` bash
docker --version
```

Also verify that Docker is running:

``` bash
sudo systemctl status docker
```

If Docker is not running:

``` bash
sudo systemctl start docker
```

Enable Docker at boot:

``` bash
sudo systemctl enable docker
```

### Optional: Run Docker without `sudo`

Add your user to the Docker group:

``` bash
sudo usermod -aG docker $USER
```

Then log out and log back in.

Verify:

``` bash
docker ps
```

If this works without `sudo`, Docker is ready.

------------------------------------------------------------------------

## 3.3 Install kubectl

One option on Ubuntu is Snap:

``` bash
sudo snap install kubectl --classic
```

Verify:

``` bash
kubectl version --client
```

Check where it is installed:

``` bash
which kubectl
```

Example:

``` text
/snap/bin/kubectl
```

------------------------------------------------------------------------

## 3.4 Install Minikube

Download and install the latest Minikube binary using the official
Minikube installation instructions.

After installation:

``` bash
minikube version
```

------------------------------------------------------------------------

## 3.5 Start the Kubernetes cluster

Because this project uses Docker as the Minikube driver:

``` bash
minikube start --driver=docker
```

Check the cluster status:

``` bash
minikube status
```

You should see the control plane and Kubernetes components running.

------------------------------------------------------------------------

## 3.6 Verify kubectl

Check the Kubernetes nodes:

``` bash
kubectl get nodes
```

Example:

``` text
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   ...   v1.x.x
```

Check all system pods:

``` bash
kubectl get pods -A
```

Check cluster information:

``` bash
kubectl cluster-info
```

At this point, the local Kubernetes environment is ready.

------------------------------------------------------------------------

# 4. Windows

## 4.1 Install Docker Desktop

Install Docker Desktop for Windows.

During installation, use the recommended WSL 2 backend when prompted.

After installation, start Docker Desktop and verify from PowerShell:

``` powershell
docker --version
```

Verify Docker is running:

``` powershell
docker ps
```

------------------------------------------------------------------------

## 4.2 Install kubectl

### Option A --- Chocolatey

If Chocolatey is installed:

``` powershell
choco install kubernetes-cli -y
```

Verify:

``` powershell
kubectl version --client
```

### Option B --- Official Kubernetes installation

Alternatively, install kubectl using the official Kubernetes
documentation.

Verify:

``` powershell
kubectl version --client
```

------------------------------------------------------------------------

## 4.3 Install Minikube

Using Chocolatey:

``` powershell
choco install minikube -y
```

Verify:

``` powershell
minikube version
```

------------------------------------------------------------------------

## 4.4 Start Minikube

Make sure Docker Desktop is running.

Then:

``` powershell
minikube start --driver=docker
```

Check:

``` powershell
minikube status
```

------------------------------------------------------------------------

## 4.5 Verify Kubernetes

``` powershell
kubectl get nodes
```

Then:

``` powershell
kubectl get pods -A
```

And:

``` powershell
kubectl cluster-info
```

The local Kubernetes cluster is now ready.

------------------------------------------------------------------------

# 5. macOS

## 5.1 Install Homebrew

If Homebrew is not already installed, install it using the official
Homebrew installation instructions.

Verify:

``` bash
brew --version
```

------------------------------------------------------------------------

## 5.2 Install Docker Desktop

Install Docker Desktop for Mac.

Start Docker Desktop and wait until Docker is running.

Verify:

``` bash
docker --version
```

Then:

``` bash
docker ps
```

------------------------------------------------------------------------

## 5.3 Install kubectl

Using Homebrew:

``` bash
brew install kubectl
```

Verify:

``` bash
kubectl version --client
```

------------------------------------------------------------------------

## 5.4 Install Minikube

Using Homebrew:

``` bash
brew install minikube
```

Verify:

``` bash
minikube version
```

------------------------------------------------------------------------

## 5.5 Start Minikube

Because Docker is used as the driver:

``` bash
minikube start --driver=docker
```

Check:

``` bash
minikube status
```

------------------------------------------------------------------------

## 5.6 Verify Kubernetes

``` bash
kubectl get nodes
```

Then:

``` bash
kubectl get pods -A
```

And:

``` bash
kubectl cluster-info
```

The local Kubernetes environment is ready.

------------------------------------------------------------------------

# 6. Verify the Complete Installation

Regardless of the operating system, these commands should work:

## Docker

``` bash
docker --version
```

## kubectl

``` bash
kubectl version --client
```

## Minikube

``` bash
minikube version
```

## Minikube status

``` bash
minikube status
```

## Kubernetes nodes

``` bash
kubectl get nodes
```

## Kubernetes system pods

``` bash
kubectl get pods -A
```

## Kubernetes cluster information

``` bash
kubectl cluster-info
```

------------------------------------------------------------------------

# 7. Start and Stop the Local Cluster

## Start

``` bash
minikube start --driver=docker
```

If the cluster already exists and was previously stopped, this starts it
again.

## Stop

``` bash
minikube stop
```

`minikube stop` stops the virtualized/containerized Kubernetes
environment but preserves the cluster configuration and resources.

Start it again with:

``` bash
minikube start
```

------------------------------------------------------------------------

# 8. Delete the Local Cluster

If you want to completely remove the Minikube cluster:

``` bash
minikube delete
```

This is different from `minikube stop`.

### `minikube stop`

``` text
Stops the cluster
       ↓
Cluster remains available
       ↓
minikube start
```

### `minikube delete`

``` text
Deletes the cluster
       ↓
Cluster resources are removed
       ↓
minikube start --driver=docker
```

------------------------------------------------------------------------

# 9. Check the Current Kubernetes Context

kubectl can work with multiple Kubernetes clusters. Check the current
context:

``` bash
kubectl config current-context
```

For Minikube, it should normally be:

``` text
minikube
```

List all configured contexts:

``` bash
kubectl config get-contexts
```

Switch to Minikube if necessary:

``` bash
kubectl config use-context minikube
```

------------------------------------------------------------------------

# 10. First Kubernetes Test

Create a simple NGINX deployment:

``` bash
kubectl create deployment nginx --image=nginx
```

Check the deployment:

``` bash
kubectl get deployments
```

Check the pod:

``` bash
kubectl get pods
```

Expose the deployment:

``` bash
kubectl expose deployment nginx --type=NodePort --port=80
```

Check the service:

``` bash
kubectl get services
```

Open the service through Minikube:

``` bash
minikube service nginx
```

Clean up the test:

``` bash
kubectl delete service nginx
kubectl delete deployment nginx
```

------------------------------------------------------------------------

# 11. Recommended Project Workflow

For this Kubernetes learning project, use the following workflow:

``` text
1. Start Docker
       ↓
2. Start Minikube
       ↓
3. Verify cluster
       ↓
4. Create Kubernetes resources
       ↓
5. Inspect resources with kubectl
       ↓
6. Test the application
       ↓
7. Stop Minikube when finished
```

Typical daily startup:

``` bash
minikube start --driver=docker
kubectl get nodes
```

Typical end-of-day shutdown:

``` bash
minikube stop
```

There is no need to delete the cluster every day.

------------------------------------------------------------------------

# 12. Common Commands

## Cluster

``` bash
minikube status
minikube start
minikube stop
minikube delete
```

## Nodes

``` bash
kubectl get nodes
kubectl describe node minikube
```

## Pods

``` bash
kubectl get pods
kubectl get pods -A
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

## Deployments

``` bash
kubectl get deployments
kubectl describe deployment <deployment-name>
```

## Services

``` bash
kubectl get services
kubectl describe service <service-name>
```

## All resources

``` bash
kubectl get all
```

------------------------------------------------------------------------

# 13. Troubleshooting

## Docker is not running

Check Docker:

``` bash
docker ps
```

Start Docker Desktop on Windows/macOS, or on Ubuntu:

``` bash
sudo systemctl start docker
```

------------------------------------------------------------------------

## Minikube cannot start

Check:

``` bash
minikube status
```

Check the configured driver:

``` bash
minikube config get driver
```

You can explicitly start with Docker:

``` bash
minikube start --driver=docker
```

------------------------------------------------------------------------

## kubectl cannot connect to Kubernetes

Check the current context:

``` bash
kubectl config current-context
```

It should normally be:

``` text
minikube
```

Then check:

``` bash
minikube status
```

If Minikube is stopped:

``` bash
minikube start
```

------------------------------------------------------------------------

## Check Minikube logs

If Minikube has a startup problem:

``` bash
minikube logs
```

------------------------------------------------------------------------

# 14. Installation Summary

  --------------------------------------------------------------------------------------------------------------------------
  Component         Ubuntu                             Windows                            macOS
  ----------------- ---------------------------------- ---------------------------------- ----------------------------------
  Container runtime Docker Engine                      Docker Desktop                     Docker Desktop

  Kubernetes CLI    kubectl                            kubectl                            kubectl

  Local Kubernetes  Minikube                           Minikube                           Minikube

  Minikube driver   Docker                             Docker                             Docker

  Cluster startup   `minikube start --driver=docker`   `minikube start --driver=docker`   `minikube start --driver=docker`
  --------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

# 15. Official Documentation

Use official documentation for the latest installation instructions
because package names, supported versions, and operating-system
requirements can change.

-   Kubernetes: https://kubernetes.io/docs/setup/
-   kubectl: https://kubernetes.io/docs/tasks/tools/
-   Minikube: https://minikube.sigs.k8s.io/docs/start/
-   Docker: https://docs.docker.com/
-   Docker Desktop: https://docs.docker.com/desktop/
-   Homebrew: https://brew.sh/

------------------------------------------------------------------------

## Setup Complete

After completing this guide, you should have:

``` text
Docker
  │
  └── Minikube
       │
       └── Kubernetes Cluster
            │
            ├── Control Plane
            └── Worker Node

kubectl
  │
  └── Communicates with the cluster
```

You can now continue with Kubernetes fundamentals such as:

-   Pods
-   Deployments
-   ReplicaSets
-   Services
-   Namespaces
-   ConfigMaps
-   Secrets
-   Volumes
-   Ingress
-   StatefulSets
-   Jobs and CronJobs
-   Resource limits
-   Health probes
-   Kubernetes networking
