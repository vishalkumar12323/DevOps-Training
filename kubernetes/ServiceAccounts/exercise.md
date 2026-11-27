# Hands-On Lab: ServiceAccount Authentication

### Lab Objectives
- Create a dedicated namespace.
- Create a ServiceAccount.
- Create RBAC permissions for that identity.
- Deploy a Pod using that ServiceAccount.
- Inspect the mounted token.
- Make an authenticated API request from inside the Pod.
- Disable token mounting and compare the behavior.
---

### Namespace
```bash
kubectl create ns sa-demo
# verify
kubectl get ns
```

### Create a ServiceAccount
```bash
kubectl create serviceaccount pod-inspector -n sa-demo
# verify
kubectl get serviceaccount -n sa-demo
# inspect
kubectl describe serviceaccount pod-inspector -n sa-demo
```

### Create Role
```bash
touch sa-role.yml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role

metadata:
  name: pod-inspector-role
  namespace: sa-demo

rules:
  - apiGroups: [""]
    resources: ["pods"]
    verbs: ["get", "list", "watch"]
```

### Create RoleBinding
```bash
touch sa-rolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding

metadata:
  name: pod-inspector-binding
  namespace: sa-demo

subjects:
  - kind: ServiceAccount
    name: pod-inspector
    namespace: sa-demo

roleRef:
  kind: Role
  name: pod-inspector-role
  apiGroup: rbac.authorization.k8s.io
```

### Create Pod the the ServiceAccount
```bash
touch sa-pod-.yaml
apiVersion: v1
kind: Pod

metadata:
  name: api-client
  namespace: sa-demo

spec:
  serviceAccountName: pod-inspector

  containers:
    - name: api-client
      image: curlimages/curl:8.12.1
      command: ["sleep", "3600"]
```

### Apply all and verify
```bash
kubectl apply -f .
# verify ServiceAccount
kubectl get pod api-client -n sa-demo -o jsonpath='{.spec.serviceAccountName}'
# verify pod
kubectl get pods -n sa-demo
```

### Inspect the mounted ServiceAccount token
```bash
kubeclt exec -it api-client -n sa-demo -- sh
# &&
ls -l /var/run/secrets/kubernetes.io/serviceaccount/
```

### Check the namespace
```bash
cat /var/run/secrets/kubernetes.io/serviceaccount/namespace
```

### Check token exists without printing its contant
```bash
test -s /var/run/secrets/kubernetes.io/serviceaccount/token \
  && echo "ServiceAccount token is mounted"
```

### Authenticate with the Kubernetes API
```bash
# * inside the container
TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)

curl --cacert /var/run/secrets/kubernetes.io/serviceaccount/ca.crt \
  -H "Authorization: Bearer $TOKEN" \
  https://kubernetes.default.svc/api/v1/namespaces/sa-demo/pods
```

### Disable automatic token mounting
Create new pod called: frontend-pod.yaml
```bash
touch frontend-pod.yaml

apiVersion: v1
kind: Pod

metadata:
  name: frontend-client
  namespace: sa-demo

spec:
  automountServiceAccountToken: false

  containers:
    - name: frontend
      image: curlimages/curl:8.12.1
      command: ["sleep", "3600"]
```

### Apply, verify and check token
```bash
kubectl apply -f frontend-pod.yaml

kubectl exec -it frontend-client -n sa-demo -- sh

ls -la /var/run/secrets/kubernetes.io/serviceaccount/
```