# Multiple Replicas in Kubernetes ☸️
## What are multiple replicas?
- ### Running multiple Pod/Containers of the same application
- Imagine: A backend API application runs on only one Pod, What happen if that Pod craches, The application may become unavailable until Kubernetes replaces the Pod and the application becomes ready again.
Instead, we can run three replicas of the same application.

## ` ℹ️Important: Multiple replicas improve availability and capacity, but they don't guarantee zero downtime. Your application, Service, readiness probes, and cluster infrastructure must also be configured appropriately.`

## What is a ReplicaSet?
- ### Kubernetes uses a controller called a ReplicaSet to maintain a specified number of Pod replicas.

## `ℹ️ In real applications, we generally create a Deployment, which manages ReplicaSets for us.`

## Hands on: Running three Nginx replicas.

### Create a namespace
```bash
kubectl create ns replicas-lab
```
Verify
```bash
kubectl get namespace
# or
kubectl get ns
```

### Apply the nginx-replicas.yml configration
```bash
kubectl apply -f nginx-replicas.yml
```

### Wait for the deployment to become ready
```bash
kubectl rollout status deployment/nginx-deployment \
  -n replicas-demo
```

### Inspect the Deployment, and Pod replicas
```bash
kubectl get deployment,pods -n replicas-demo
```

##  Experiment 1
### Delete the one Pod
```bash
kubectl get pods -n replicas-demo

                            ⬇️

kubectl delete pod <pod-name> -n replicas-demo

                            ⬇️

kubectl get pods -n replicas-demo
```

##  Experiment 2
### Scale from 3 to 5 replicas
Scale the deployment direct
```bash
kubectl scale deployment nginx-deployment \
    --replicas=5 \
    -n replicas-demo
```

###  Wait for readiness and verify
```bash
kubectl rollout status deployment/nginx-deployment -n replicas-demo

                                            ⬇️

kubectl get deployment,pods -n replicas-demo
```
