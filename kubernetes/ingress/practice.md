# Kubernetes Ingress
### Kubernetes Ingress is an API object that manages external (usually HTTP and HTTPS) access to services running inside a cluster.

## Core Components
- ### The Ingress Resource: `A declarative networking.k8s.io/v1 Kubernetes manifest (written in YAML) that acts as a rulebook. It defines mapping rules based on hostnames (e.g., app.example.com) and URL paths (e.g., /login or /api) to direct traffic to specific internal Kubernetes Services`

- ### The Ingress Controller: `A daemon or reverse-proxy application running inside the cluster that actively watches the Kubernetes API for Ingress resource changes. It is the actual data-plane engine that implements the routing rules using software like NGINX, Traefik, HAProxy, or Envoy.`