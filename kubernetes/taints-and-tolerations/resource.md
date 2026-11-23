# What are Taints and Tolerations?
- ### Taints and tolerations are Kubernetes scheduling mechanisms that control which Pods can be scheduled onto which Nodes.
Important: `A toleration does not guarantee that a Pod will be scheduled on a particular Node. It only removes the restriction imposed by a matching taint. Other scheduling rules still apply.`

## Taints Effects
Kubernetes supports three primary taint effects.

### NoSchedule
- New Pods that do not tolerate the taint cannot be scheduled on the Node.
- Existing Pods are not automatically evicted.

### PreferNoSchedule
- Kubernetes tries to avoid scheduling Pods on the tainted Node.
- It may still schedule them there if other suitable Nodes are unavailable.

### NoExecute
- New Pods without matching tolerations cannot be scheduled.
- Existing Pods without matching tolerations can be evicted.
- Pods with a toleration can remain for a specified duration using tolerationSeconds.
---

### How taints and tolerations work together
Considor the node
```bash
Node: minikube

Taint:
dedicated=backend:NoSchedule
```

Now considor two Pods
Pod A without toleration
```bash
apiVersion: v1
kind: Pod
metadata:
  name: frontend-pod
spec:
  containers:
    - name: nginx
      image: nginx
```

Pod B with toleration
```bash
apiVersion: v1
kind: Pod
metadata:
  name: backend-pod
spec:
  tolerations:
    - key: "dedicated"
      operator: "Equal"
      value: "backend"
      effect: "NoSchedule"
  containers:
    - name: nginx
      image: nginx
```
---
Toleration operators
| Operator | Meaning | 
| --- | --- | 
| Equal | Both key and value must match |
| Exists | Only the key must match; value is ignored |
---

### Check existing taints
```bash
kubectl describe node <node-name>
```
Check the Taints section

### Apply a taint
```bash
kubectl taint nodes minikube dedicated=backend:NoSchedule
```

### Remove the taint
```bash
kubectl taint nodes minikube dedicated:NoSchedule
```
---
## Advanced concepts - NoExecute and tolerationSeconds
New Pods without matching tolerations cannot be scheduled.
Existing Pods without matching tolerations can be evicted.

Example
```bash
toleration:
  - key: "dedicated"
    operator: "Equal"
    value: "true"
    effect: "NoExecute"
    tolerationSecond: 60
```
This means:
- The Pod tolerates the taint.
- It can remain on the Node for 60 seconds after the taint is applied.
- After that period, Kubernetes can evict it if the taint remains.
---

## Use cases
1. GPU Nodes

    Dedicated GPU Nodes should run machine-learning workloads rather than ordinary application workloads.

    Taint: gpu=true:NoSchedule

2. Dedicated Database Nodes

    Restrict scheduling to database workloads.

    Taint: dedicated=database:NoSchedule

3. Control Plane Nodes

    Kubernetes commonly uses taints to prevent ordinary application workloads from running on control-plane Nodes.

4. Node Maintenance

    NoExecute can help evict workloads from Nodes that need maintenance.