# Kubernetes ServiceAccounts
### A `ServiceAccount` is an identity provided by Kubernetes for processes running inside Pods.
Think about a backend application running inside a Kubernetes Pod.

Suppose your application needs to:
- Retrieve information about other Pods.
- Read ConfigMaps.
- Watch Kubernetes resources.
- Communicate with the Kubernetes API Server.
- Perform automated cluster operations.
How does Kubernetes know which application is making these requests?

This is where ServiceAccounts come in.

Each Pod can be associated with a ServiceAccount, which provides an identity for the processes running inside it.

- ServiceAccount provides an identity.
- RBAC determines what that identity is allowed to do.

### Default ServiceAccount
```bash
kubectl get serviceaccount
```