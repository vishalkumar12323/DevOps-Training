# Affinity and Anti Affinity
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