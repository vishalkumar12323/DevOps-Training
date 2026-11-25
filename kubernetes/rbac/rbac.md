# Role Based Access Control (RBAC)
### It is a kubernetes authorization machanism that determines:
- Who can access the Kubernetes API?
- What resources can they access?
- What operations can they perform on those resources?

Imaging a kubernetes cluster used by three developers.
|   Developers      |   Permission  |
|   ---             |   ---         |
|   Developer A     |   View Pods   |
|   Developer B     |   View and create Deployments |
|   Developer C     |   Manage Pods, Services, and Deployments  |
---

## RBAC main resources
Kubernetes RBAC has four important resource

### 1. Role
- Defines permissions within a particular namespace.
- Example: Allow reading Pods in development.
### 2. ClusterRole
- Defines permissions that can apply across namespaces or to cluster-scoped resources.

- Example: Allow reading Nodes across the cluster.

### 3. RoleBinding
- Connects a Role or ClusterRole to a user, group, or ServiceAccount within a namespace.

### 4. ClusterRoleBinding
- Connects a ClusterRole to a user, group, or ServiceAccount across the cluster.
---

## Role Permission
A Role contains set of rules

Each rule define three important things:

|   Field   |   Meaning  |  Example  |
|   ---     |   ---      |  ---      |
|  ApiGroups|   Kubernetes API groups   |   "" for core resource
|  Resources|   Resource being accessed |   pods    |
|  verbs    |   Allowed operations| get, list, watch    |

Role Example:
```bash
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: development
rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
```