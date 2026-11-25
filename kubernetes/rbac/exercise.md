# Practical Lab - RBAC permission
This lab objective is to create a ServiceAccount that can read Pods but cannot create or delete them.

### Lab Objectives
- Create a namespace named rbac-demo.
- Create a ServiceAccount named pod-reader.
- Create a Role with read-only Pod permissions.
- Bind the Role to the ServiceAccount.
- Test allowed and denied operations.
---

### Create a namespace
```bash
kubectl create ns rbac-demo
# verify
kubectl get ns
```

### Create a ServiceAccount
```bash
kubectl create serviceaccount pod-reader -n rbac-demo
# verify
kubectl get serviceaccount -n rbac-demo
```

