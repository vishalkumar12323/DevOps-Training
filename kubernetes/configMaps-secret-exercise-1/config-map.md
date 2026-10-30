## Apply the app-config.yml and config-pod.yml manifest files
```bash
kubectl apply -f app-config.yml
kubectl apply -f config-pod.yml
```

### Inspect the result
```bash
kubectl get configmaps -n config-demo
kubectl describe configmap app-config -n config-demo

kubectl get pods -n config-demo
```

### Now Inspect the environment variables inside the container.
```bash
kubectl exec -n config-demo config-demo-pod -- printenv NODE_ENV
kubectl exec -n config-demo config-demo-pod -- printenv APP_NAME
kubectl exec -n config-demo config-demo-pod -- printenv LOG_LEVEL
```


## Kubernetes Secerts
A Secret is a Kubernetes object used to store sensitive information that applications need, example:
- Database usernames and passwords
- API keys and access tokens
- TLS certificates and private keys
- Credentials for accessing private container registries

### Create a secret.
```bash
kubectl create secret generic app-secret \
  --namespace=config-demo \
  --from-literal=DB_USER=demo_user \
  --from-literal=DB_PASSWORD='fake-password-123'
```

### Verify the secret.
```bash
kubectl get secrets -n config-demo
```

### Inspecting its metadata
```bash
kubectl describe secret app-secret -n config-demo
```

### Apply the secret-pod.yml
```bash
kubectl apply -f secret-pod.yml
```
### Check the Pod
```bash
kubectl get pods -n config-demo
```

### Verify the environment variables:
```bash
kubectl exec -n config-demo secret-demo-pod -- printenv DB_USER
kubectl exec -n config-demo secret-demo-pod -- printenv DB_PASSWORD
```