# Kubernetes (k8s)

## what kubernetes actually?

Kubernetes (K8s), is an open source system for automating deployment, scaling, and management of containerized applications.

### Understanding in a better way:

Suppose you run a api service using docker

```bash
docker run --name api-service-container -p 8080:8080  my-api
```

Docker start one container

Now suppose our API get heavy traffic and you want:

```bash
API Container 1
API Container 2
API Container 3
API Container 4
```

For that you could menually start four containers and distribute traffic around these containers using Load Balancer

But then you have problems

- What happens if container 2 crashes?
- How do you distribute traffic?
- How do you replace a failed container?
- How do you deploy a new version?
- How do you scale from 4-10 containers?
- How do you rollback?
- How do container find each-other?
- How do you manage configration and secrets?

This is where kubernetes comes in.

### Kubernetes provide a system for managing containers

You tells k8s what desired state you want:

```bash
"I want 4 Instances of my API running."
```

Kubernetes continuously works toward that state.

if one dies

```bash
Desired: 4

Running:
API-1
API-2
API-3
```

k8s notices:

```bash
3 != 4
```

And creates another.

```bash
API-1
API-2
API-3
API-4
```

### That's one of the fundamental ideas behind Kubernetes:

- You declare what you want, and Kubernetes continuously works to maintain that state.

### K8s high level architecture

```bash
                 Kubernetes Cluster
                         │
              ┌──────────┴──────────┐
              │                     │
        Control Plane            Worker Node
              │                     │
       ┌──────┴──────┐        ┌─────┴─────┐
       │             │        │           │
   API Server    Scheduler   Kubelet    Kube Proxy
       │                         │
       │                     Container
       │                     Runtime
       │                         │
       │                      Pod
       │                       │
       │                    Container
```

### The most common words you heard when you learning about k8s

## cluster:

### The entire kubernetes environment called kubernetes cluster.

## Node:

### A machine inside the cluster.

```bash
Cluster
   │
   ├── Node 1
   ├── Node 2
   └── Node 3
```

## Pod:

### The smallest deployable unit in k8s.

```bash
Pod
 │
 └── Container
```

For example:

```bash
Pod
 │
 └── Nodejs API container
```

### A Pod can technically contain multiple containers:

```bash
Pod
 ├── Application container
 └── Database container
```

### You can think like:

- Pod ≈ wrapper around a container.

## Deployment:

### A deployment manages pods.

```bash
Deployment
    │
    ├── Pod 1
    ├── Pod 2
    └── Pod 3
```

## Service:

### A stable network endpoint that routes traffic to dynamic Pods.

```bash
              Service
                 │
        ┌────────┼────────┐
        │        │        │
      Pod 1    Pod 2    Pod 3
```
