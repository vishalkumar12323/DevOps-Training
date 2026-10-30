# Kubernetes (K8s) Learning Repository

This repository contains beginner-friendly Kubernetes examples and notes for understanding the core concepts of Kubernetes (K8s), including Pods, Deployments, Services, and the control plane.

## Repository Contents

- `menual.md` — Kubernetes concepts and architecture explained with simple examples.
- `nginx-deployment.yml` — A Deployment that runs three replicas of the NGINX container.
- `nginx-service.yml` — A ClusterIP Service that exposes NGINX on port 80.

## Learning Topics

The examples cover the following Kubernetes concepts:

- Pods and Containers
- Deployments and desired state
- Services and network exposure
- Kubernetes control plane and worker nodes
- Replicas and workload scaling
- Kubernetes manifests and `kubectl`

## Prerequisites

Before starting, install the following tools:

- `kubectl`
- A Kubernetes cluster, such as Docker Desktop's Kubernetes environment, kind, or a managed cluster
- `kubectl` configured to connect to your cluster

Verify your Kubernetes configuration:

```bash
kubectl cluster-info
kubectl get nodes
```

## Deploy the NGINX Example

From the repository root, apply the Deployment and Service manifests:

```bash
kubectl apply -f nginx-deployment.yml
kubectl apply -f nginx-service.yml
```

The Deployment creates three NGINX Pods. The Service provides a stable ClusterIP endpoint for those Pods.

## Verify the Resources

Check the Deployment and Service status:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

Inspect the NGINX Deployment:

```bash
kubectl describe deployment nginx
```

Inspect the Service:

```bash
kubectl describe service nginx
```

To test the Service from your local terminal, forward port 80:

```bash
kubectl port-forward service/nginx 8080:80
```

In another terminal, request the NGINX page:

```bash
curl http://localhost:8080
```

Stop the port forwarding with `Ctrl+C` in the terminal running `kubectl port-forward`.

## Scale the Deployment

Increase the number of replicas:

```bash
kubectl scale deployment nginx --replicas=5
```

Verify the result:

```bash
kubectl get pods
```

Return the Deployment to three replicas:

```bash
kubectl scale deployment nginx --replicas=3
```

## View the Kubernetes Resources

Use the following commands to inspect the configured resources:

```bash
kubectl get deployment nginx -o yaml
kubectl get service nginx -o yaml
kubectl get pods -o wide
```

## Delete the Example

Remove the resources created from the manifests:

```bash
kubectl delete -f nginx-service.yml
kubectl delete -f nginx-deployment.yml
```

Confirm that the resources were removed:

```bash
kubectl get deployments
kubectl get services
```

## Quick Reference

| Resource     | Purpose                                                     |
| ------------ | ----------------------------------------------------------- |
| `Deployment` | Maintains the desired number of running Pods                |
| `Pod`        | Runs one or more containers as the smallest deployable unit |
| `Service`    | Provides a stable network endpoint for Pods                 |
| `ClusterIP`  | Exposes a Service only inside the Kubernetes cluster        |

## Notes
- The Deployment and Service use matching labels so the Service can select the Pods.
- Review `menual.md` for conceptual explanations before applying the manifests.
