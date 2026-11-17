# What is Kubernetes Scheduling?
### `Kubernetes scheduling is the process of deciding which worker node should run a newly created Pod.`

## Important components to understand
| Component     |   Responsibilty   |
| ---   | --- |
| kube-scheduler | Selects a node for pod |
| kubelet | Ensures assigned Pods run on its node |
| kubeapiserver | Stores and exposes cluster state |
| kube-controller-manager | Runs controllers that maintain desired state


## Important scheduling concepts
-   nodeSelector
    
    The simplest way to tell Kubernetes which type of node should run a Pod.

    Example:
    ```bash
    spec:
        nodeSelector:
            environment: production
    ```

-   nodeName
    
    Directly specify a node's name, kubernetes directly assigns the Pod to the specified node.
    ```bash
    spec:
        nodeName: minikube
    ```

-   Resource Requests
    Tell kuberenets how much CPU and memory a Pod needs.
    ```bash
    resources:
        requests:
            cpu: "500m"
            memory: "512Mi"
    ```
