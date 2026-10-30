#  Rolling Updates ☸️
## What is a Rolling update?
- ### A Kubernetes rolling update is the default deployment strategy that allows you to update an application running in your cluster with zero downtime.

### `ℹ️ Important: Rolling updates help achieve minimal downtime, but they don't guarantee zero downtime. Readiness probes, sufficient capacity, application compatibility, and correct Service configuration all matter.`

## Rolling update strategy
|       Setting                            |                Meaning                    |
|        -------                           |               -------                     |
|       maxSurge                          |          Maximum number of Pods allowed above the desired replica count during an update.|
|       maxUnavailable            |          Maximum number of Pods allowed to be unavailable during an update.                      |


### Verify the deployment.
```bash
kubectl get deployments -n replicas-demo
```

### Inspect the image and replica configration
```bash
kubectl describe deployment nginx-deployment \
  -n replicas-demo
```

### Watch the Pods
```bash
kubectl get pods -n replicas-demo -w
```

### Trigger a rolling update
- Set the container image from nginx:stable to nginx:alpine
```bash
kubectl set image deployment/nginx-deployment \
  nginx=nginx:alpine \
  -n replicas-demo
```

### Wait for the rollout finish
```bash
kubectl rollout status deployment/nginx-deployment \
  -n replicas-demo
```

### Verify and Inspect the result
```bash
kubectl get deployment nginx-deployment -n replicas-demo

kubectl get deployment nginx-deployment \
  -n replicas-demo \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

### Explore the rollout history
```bash
kubectl rollout history deployment/nginx-deployment \
  -n replicas-demo
```