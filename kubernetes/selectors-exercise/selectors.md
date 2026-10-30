## Apply the backend-deployment.yml
```bash
kubectl apply -f backend-deployment.yml
```

### Check rollout report progress.
```bash
kubectl rollout status backend/backend-deployment -n selector-demo
```
You would see "deployment "backend-deployment" successfully rolled out"

### Inspect the pods and their labels
```bash
kubeclt get pods -n selector-demo --show-labels
```

## Finding Pods using selectors
```bash
kubectl get pods -n selector-demo --selector app=backend
```

```bash
kubectl get pods -n selector-demo -l environment=production
```

Using multiple selectors:
```bash
kubectl get pods -n selector-demo -l "app=backend,environment=production"
```


## Apply the backend-service.yml
```bash
kubectl apply -f backend-service.yml
```

### Inspect the service
```bash
kubectl get service -n selector-demo
# or
kubectl get service backend-service -n selector-demo
```

### Check endpoints
```bash
kubectl get endpointslice -n selector-demo -l kubernetes.io/service-name=backend-service
```

### Access nginx service on our browser
```bash
kubectl port-forward -n selector-demo service/backend-service 3000:80
```