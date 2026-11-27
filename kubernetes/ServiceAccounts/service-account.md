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
---

## How ServiceAccount Authentication works?
When a Pod uses a ServiceAccount, Kubernetes can automatically provide a token to the Pod.
This token is used to authenticate requests to the Kubernetes API Server.
The token is typically mounted inside the container at:

```bash
/var/run/secrets/kubernetes.io/serviceaccount/
```

The Directory contains:
token       Authentication Token
ca.cert     Certificate used to verify API Server
namespace   Pod's namespace
Older Kubernetes versions commonly created permanent Secret-based tokens automatically for ServiceAccounts.

Modern Kubernetes uses `projected, short-lived, automatically rotating ServiceAccount tokens` by default.

Example Assigning a ServiceAccount to a Pod:
```bash
apiVersion: v1
kind: Pod
metadata:
  name: backend-pod
  namespace: development

spec:
  serviceAccountName: backend-service-account
#   automountServiceAccountToken: false     # disable automatic token mounting
  containers:
    - name: backend
      image: nginx:latest
```