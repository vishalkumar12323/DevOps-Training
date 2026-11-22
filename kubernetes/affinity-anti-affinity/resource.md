# Affinity and Anti-Affinity
---
## What is Affinity in Kubernetes?
- ### A scheduling mechanism that allows you to express preferences or requirements about where Kuberenetes should place your Pods.

For example, suppose three application componnents
- Frontend
- Backend
- Database
1. Frontend Pods to run on nodes with SSD storage.
2. Backend Pods to run close to database Pods.
3. Two database replicas to run on different nodes for high availability.
---

## Types of Affinity
- ### Node Affinity
- ### Pod Affinity
- ### Pod Anti-Affinity
---

## Node Affinity
- ### Node Affinity allows you to schedule Pods onto nodes based on their labels.

Suppose a cluster has three nodes:
```bash
Node    Label
node-1  disk=ssd
node-2  disk=hdd
node-3  disk=ssd
```
We want to schedule an application only on SSD nodes, we can use Node Affinity.

### Two important Node Affinity rules
- `requiredDuringSchedulingIgnoredDuringExecution`: The Pod must satisfy the scheduling condition, If no node matches, the Pod remains Pending.

Example
```bash
affinity:
    nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
                - matchExpressions:
                    - key: disk
                      operator: In
                      values:
                        - ssd
```
Meaning: Only nodes with disk=ssd are eligible

- `preferredDuringSchedulingIgnoredDuringExecution`: K8s prefers matching nodes but can schedule the Pod on another eligible node if necessary.
Example
```bash
affinity:
    nodeAffinity:
        preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 80
              preference:
                matchExpressions:
                    - key: disk
                      operator: In
                      values:
                        - ssd
```
---
## Pod Affinity
- ### Pod affinity allows to schedule a pods near others pods that matches specific labels

Examples: Backend pods to run close to database pods.
```bash
affinity:
  podAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchLabels:
            app: db
        topologyKey: kubernetes.io/hostname
```
`topologyKey`: It tells Kubernetes the level at which Pods should be considered together.

Examples
```bash
  TopologyKey                               Meaning
kubernetes.io/hostname                    Same Node
topology.kubernetes.io/zone               Same availability zone
topology.kubernetes.io/region             Same region
```
---
## Pod Anti-Affinity
Anti-Affinity is the opposite of Pod Affinity
- ### It tells Kubernetes to avoid scheduling a Pod in the same topology domain as certain other Pods.

For Example: suppose you have three database replicas.
You want each replica to run on a different node to improve availability.
```bash
affinity:
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchLabels:
            app: db
        topologyKey: kubernetes.io/hostname
```
This means: Don't schedule this Pod on a node that already contains a matching app=db Pod.