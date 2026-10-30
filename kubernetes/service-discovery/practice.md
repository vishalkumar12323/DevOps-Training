# A Service is an abstract way to expose an application running on a set of Pods as a single network service
### Imagine an application with two services
- Frontend: React application
- Backend: Node.js + Express API
backend runs inside a Kubernetes Pod. The frontend needs to send HTTP requests to it.
The problem is that Pod IP addresses can change when Pods are recreated or rescheduled. If frontend connects directly to a Pod IP, that connection may stop working.

Kubernetes solves this with a Service.

## Hands On:
### Create a namespace
```bash
kubectl create ns service-discovery-demo
# Verify
kubectl get ns
```

### Apply the web-server-deployment.yml
```bash
kubectl apply -f web-server-deployment.yml
```
### Checks the Pods
```bash
kubectl get pods -n service-discovery-demo -o wide
```

### Apply the web-service.yml
```bash
kubectl apply -f web-service.yml
# verify
kubectl get service -n service-discovery-demo
```

### Checks its endpoints
```bash
kubectl get endpointslice -n service-discovery-demo
```

### Discovering the service by starting a temporary client pod with curl
```bash
kubectl run curl-client \
  --image=curlimages/curl:8.12.1 \
  --restart=Never \
  -n service-discovery-demo \
  --command -- sleep 3600
```

### Send the HTTP request by using service name created above
```bash
kubectl exec -n service-discovery-demo curl-client -- \
  curl -s http://backend-service
```
Result: HTML containing the Nginx welcome page.