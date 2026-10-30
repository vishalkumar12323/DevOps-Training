# Kubernetes Resource Requests and Limits
Every container running inside k8s consumes resources such as CPU and memory.
- CPU is used to execute application code, process API requests, and perform computations.
- Memory (RAM) is used for objects, caches, buffers, and other runtime data.

## Check resource allocatable for master node `minikube`
```bash
kubectl describe node minikube
```

## Apply the nginx-resources.yml deployment
```bash
kubectl apply -f nginx-resources.yml
```

## Inspect the Pod.
```bash
kubectl get pod -n config-demo
```
```bash
kubectl describe pod -n config-demo -l app=nginx-resource
```
or
```bash
kubectl get deployment nginx-resources -n config-demo -o yaml
```

### Here's what each value means.
| configration    |   meaning |
|   ---     |   ---     |
|   cpu: "250m" request  |	0.25 CPU core
|   cpu: "500m" limit   |	0.5 CPU core
|   memory: "128Mi" request |	128 mebibytes of memory requested for scheduling
|   memory: "256Mi" limit   |	256 mebibytes of memory allowed


# Now, we do a test with opposite situation, reqesting more memory than minikube node can provide
pending-resources.yml
```bash
apiVersion: v1
kind: Pod

metadata:
  name: memory-pending
  namespace: config-demo

spec:
  containers:
    - name: nginx
      image: nginx:stable

      resources:
        requests:
          memory: "100Gi"
          cpu: "100m"
```

## Apply memory-test.yml
```bash
kubectl apply -f memory-test.yml
```

### Check Pod
```bash
kubectl get pod memory-pending -n config-demo
```
The Pod is in Pending state.

### Inspect
```bash
kubectl describe pod memory-pending -n config-demo
```
