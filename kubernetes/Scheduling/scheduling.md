# What is Kubernetes Scheduling?
### `Kubernetes scheduling is the process of deciding which worker node should run a newly created Pod.`

## Important components to understand
| Component     |   Responsibilty   |
| ---   | --- |
| kube-scheduler | Selects a node for pod |
| kubelet | Ensures assigned Pods run on its node |
| kubeapiserver | Stores and exposes cluster state |
| kube-controller-manager | Runs controllers that maintain desired state
