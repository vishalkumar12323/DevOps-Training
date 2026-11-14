# What is a DaemonSet?
### A DaemonSet is a Kubernetes workload resource that ensures a copy of a particular Pod runs on every eligible Node in a Kubernetes cluster.
Or
### A DaemonSet makes sure that a specific Pod runs on every node where it is supposed to run.

---

## Important: `A DaemonSet does not necessarily run on every node. Node selectors, affinity rules, and taints/tolerations can restrict which nodes are eligible.`

## Use Cases:
### DaemonSets are especially useful for software that needs to operate at the node level.

- Log collection: `Tools like Fluent Bit run on every node and collect container logs from that node.`

- Monitoring agents: `Node Exporter collects CPU, memory, disk, and other host-level metrics.`

- Networking: `Networking components such as Calico agents run on nodes to manage networking and network policies.`

- Security agents: `Security and runtime-monitoring agents can run on each node to observe node-level activity.`


## DaemonSet vs Deployment
This is one of the most important concepts to understand.

| Feature | Deployment | DaemonSet |
| --- | --- | --- |
| Purpose | Run a desired number of replicas | Run one Pod per eligible node |
| Pod placement | Scheduler chooses nodes | Controller targets eligible nodes |
| Scaling | Set replica count | Follows eligible node count |
| New node joins | No automatic extra replica | Automatically creates a Pod |
| Typical use | APIs, frontend, workers | Logging, monitoring, networking |

## Create and apply daemonset manifest
```bash
touch daemonset.yaml
kubectl apply -f daemonset.yaml
```

### Check Status
```bash
kubectl get daemonset -n daemonset-demo

kubectl describe daemonset node-agent -n daemonset-demo

# Inspect logs
kubectl logs -n daemonset-demo -l app=node-agent
```

### Test for automatic pod creation
```bash
# Delete the Pod menually
kubectl delete pod -n daemonset-demo -l app=node-agent

# Watch Pod
kubectl get pod -n daemonset-demo -w
```
---

## Advance Daemonsets
- Node labels
- Node selector
- Taints and tolerations
--- 

### Node Lables
`kubernetes nodes have labels that describe their characteristics`

For Example
```bash
Node            Labels

node-1          environment=production
node-2          environment=development
node-3          environment=production
```
A workload can use these labels to target specific nodes.

Check nodes labels
```bash
kubeclt get nodes --show-labels
```
Add a custom label
```bash
kubectl label nodes <node-name> environment=production
```
---
Node Selectors

A `nodeSelector` tells Kubernetes that a Pod must be scheduled only on nodes containing the specified labels.

`nodeSelector` added under `spec.template.spec`
```bash
spec:
    template:
        spec:
            nodeSelector:
                environment: production
            containers:
                .....
                .....
```
---
### Taints and tolerations
- Node labels attract workloads; taints repel workloads unless they tolerate the taint.