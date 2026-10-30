## Checking Cluster status, and exisiting pods

```bash
minikube status
kubectl get pods -o wide # -o wide gives extra info
```

## Creating a dedicated Namesapce for the exercise

```bash
kubectl create namespace labels-lab
kubectl get namespace # verify namesapce
```

## Apply the manifest:

```bash
kubectl apply -f labels-lab.yml
```

## Checking the Pods with their labels:

```bash
kubectl get pods -n labels-lab --show-labels -o wide
```

## Practice Set

### Find Frontend pods

```bash
kubectl get pods -n labels-lab -l "app=frontend"
```

### Find Backend pods

```bash
kubectl get pods -n labels-lab -l "app=backend"
```

### combine two conditions

```bash
kubectl get pods -n labels-lab -l "app=backend,environment=production"
```

### Find development pods

```bash
kubectl get pods -n labels-lab -l "environment=development"
```

## Use case for matchExpressions conditions

### Find pods running in development and production

Use In

```bash
kubectl get pods -n labels-lab -l "environment In (development,production)"
```

### Find pods those not in development

Use NotIn

```bash
kubectl get pods -m labels-lab -l "environment NotIn (development)"
```

### Find pods that have a tier label

Use Exist

```bash
kubectll get pods -n labels-lab -l "tier"
```

### Find Pod that do not have tier label

Use DoesNotExist

```bash
kubectl get pods -n labels-lab -l "!tier"
```

## Modifying labels from Pods

### Removing 'tier' label from worker-pod

```bash
kubectl label pod worker-pod -n labels-lab tier-
```

The trailing - remove the label.

Verify:

```bash
kubectl get pods -n labels-lab --show-labels
```

## Add and change labels

### Change worker-pod environment from development to staging

```bash
kubeclt label pod worker-pod -n labels-lab environment=staging --overwrite
```

## Clean up

### Remove all resources

```bash
kubectl delete namespace labels-lab
```

This deletes the namespace and its Pods
