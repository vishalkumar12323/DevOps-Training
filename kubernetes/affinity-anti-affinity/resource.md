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