# Kubernetes - Labels and Selectors

Labels and selectors are one of the most important concepts in Kubernetes because they allow Kubernetes resources to identify and work with groups of Pods.

## What are Labels?

### A Label is a key-value pair that we attach to a kubernetes object, most commonly a Pod.

For Example:

```bash
labels:
    app: nginx
```

It means:

- This pod belongs to the nginx application.

### Create Label using simple nginx pod.

nginx-label-pod.yml

```bash
apiVersion: v1
kind: Pod

metadata:
  name: nginx-label-pod
  labels:
    app: nginx
    environment: development

spec:
  containers:
    - name: nginx
      image: nginx
```

A Pod can have multiple labels:

```bash
app: nginx
environment: development
version: v2
```

Create a Pod with label

```bash
kubectl apply -f nginx-label-pod.yml
```

Check the Pod

```bash
kubectl get pods
```

Inspect Pod labels:

```bash
kubectl get pods nginx-label-pod --show-labels
```

### Querying Pods using label

Show me Pods whose label app is nginx

```bash
kubectl get pods -l app=nginx
# or
kubectl get pods -l environment=development
```

## What are Selectors?

A selector is a rule used to find Kubernetes objects based on their labels.

### Basic Selectors:

Suppose we have three Pods:

```bash
Pod A
app=frontend

Pod B
app=backend

Pod C
app=frontend
```

If we use:

```bash
app=frontend
```

The result is:

```bash
Pod A
Pod C
```

### kubectl Selector:

```bash
kubectl get pods -l app=nginx
# or
kubectl get pods --selector app=nginx
```

Both command are equivalent

### Multiple labels:

Let's say out Pod look like this:

```bash
Pod A:
app=backend
environment=production

Pod B:
app=backend
environment=development

Pod C:
app=frontend
environment=production
```

we can use:

```bash
kubectl get pods -l app=backend
```

Result:

```bash
Pod A
Pod B
```

But we can make selector more specific:

```bash
kubectl get pods -l "app=backend, environment=production"
```

Result:

```bash
Pod A
```

### matchLabels

It means exact equality
Suppose:

```bash
matchLabels:
  app: backend
  environment: production
```

This means:

```bash
app == backend
AND
environment == production
```

### matchExpressions

Kubernetes provides a more powerful selector mechanism called matchExpressions.
We can express condition such as:

```bash
environment IN (production, staging)
```

For example:

```bash
selector:
  matchExpressions:
    - key: environment
      operator: In
      values:
        - production
        - staging
```

The four important operators:

```bash
In # Value must be one of the specified values.
NotIn # Value must not be one of the specified values.
Exists # The label must exist.
DoesNotExist # The label must not exist.
```

## Where are selector used?

Selectors aren't just something we use with kubectl.
Several Kubernetes resources use selectors.

### Service

A Service uses a selector to determine:

- Which Pods should receive traffic?

```bash
selector:
  app: backend
```

### Deployment

A Deployment uses a selector to determine:

- Which Pods belong to this Deployment?

```bash
selector:
  matchLabels:
    app: backend
```

### ReplicaSet

A ReplicaSet uses a selector to determine:

- Which Pods should I manage?

```bash
selector:
  matchLabels:
    app: backend
```
