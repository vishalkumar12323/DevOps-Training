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

### Create a Role
`touch pod-reader-role.yaml`
```bash
apiVersion: rbac.authorization.k8s.io/v1
kind: Role

metadata:
  name: pod-reader-role
  namespace: rbac-demo

rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
```

### Apply and Verify
```bash
kubectl apply -f pod-reader-role.yml

kubectl get role -n rbac-demo

kubectl describe role pod-reader-role -n rbac-demo
```

### Create a RoleBinding
`touch pod-reader-binding.yaml`
```bash
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding

metadata:
  name: pod-reader-binding
  namespace: rbac-demo

subjects:
  - kind: ServiceAccount
    name: pod-reader
    namespace: rbac-demo

roleRef:
  kind: Role
  name: pod-reader-role
  apiGroup: rbac.authorization.k8s.io
```

### Apply & Verify
```bash
kubectl apply -f pod-reader-binding.yaml

kubectl get rolebinding -n rbac-demo
```

### Test RBAC permission.
```bash
kubectl auth can-i # Lets you check whether a particular identity is authorized to perform an operation.
```

- ### List Pods
    ```bash
    kubectl auth can-i list pods -n rbac-demo --as=system:serviceaccount:rbac-demo:pod-reader
    ```
    Expected output: yes

- ### Get Pods
    ```bash
    kubectl auth can-i get pods -n rbac-demo --as=system:serviceaccount:rbac-demo:pod-reader
    ```
    Expected output: yes

- ### Create Pods
    ```bash
    kubectl auth can-i create pods -n rbac-demo --as=system:serviceaccount:rbac-demo:pod-reader
    ```
    Expected output: no