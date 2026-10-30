# Rollbacks in Kubernetes.
- ### A Kubernetes rollback is a native mechanism that allows you to instantly revert an application deployment to a previous stable state

### Imagine you're deploying your backend API:
- Version 1: Your application works correctly.
- Version 2: You deploy a new feature.
- Problem: Version 2 introduces a bug, and your application starts failing.
You want to return to the previous working version without manually recreating the entire Deployment.

That's a rollback: reverting a Deployment to an earlier revision of its Pod template.

`ℹ️ Important: A rollback restores an earlier Deployment Pod template. It does not automatically undo database migrations, reverse external side effects, or guarantee that the previous version will work with the current database.`

### Check the rollout history:
```bash
kubectl rollout history deployment/my-app -n default
```

### To inspect a specific revision:
```bash
kubectl rollout history deployment/my-app -- revision=2 -n default
```
Use a revision number that actually appears in your history.

## Exercise: Rolling back a nginx deployment
### Apply the nginx-deployment.yml file to create a nginx Deployment:
```bash
kubectl apply -f nginx-deployment.yml
```

### Inspect the nginx Pod:
```bash
kubectl get pods -l "app=nginx-deployment"
```

### Inspect revision history:
```bash
kubectl rollout history deployment/nginx-deployment -n default
```

## Trigger a rolling update:

### Before changing the container image, first check the current container image:
```bash
kubectl get deployment nginx-deployment \
    -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```
`Output:`
```bash
nginx:stable
```

### Set the container image from nginx:stable to nginx:alpine
```bash
kubectl set image deployment/nginx-deployment \
    nginx=nginx:alpine \
    -n default
```

### Check container image:
```bash
kubectl get deployment nginx-deployment \
    -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```
`Output:`
```bash
nginx:alpine
```

### Inspect revision history again:
```bash
kubectl rollout history deployment/nginx-deployment -n default
```

### Perform the rollback
```bash
kubectl rollout undo deployment nginx-deployment -n default
```

### Check container image:
```bash
kubectl get deployment nginx-deployment \
    -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```
`Output:`
```bash
nginx:stable
```
