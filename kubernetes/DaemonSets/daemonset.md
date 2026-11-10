# What is a DaemonSet?
### A DaemonSet is a Kubernetes workload resource that ensures a copy of a particular Pod runs on every eligible Node in a Kubernetes cluster.
Or
### A DaemonSet makes sure that a specific Pod runs on every node where it is supposed to run.

---

## Important: `A DaemonSet does not necessarily run on every node. Node selectors, affinity rules, and taints/tolerations can restrict which nodes are eligible.`

## Use Cases:
### DaemonSets are especially useful for software that needs to operate at the node level.

- Log collection: `Tools like Fluent Bit run on every node and collect container logs from that node.`

- Monitoring agents: `Node Exporter collects CPU, memory, disk, and other host-level metrics.`

- Networking: `Networking components such as Calico agents run on nodes to manage networking and network policies.`

- Security agents: `Security and runtime-monitoring agents can run on each node to observe node-level activity.`


## DaemonSet vs Deployment
This is one of the most important concepts to understand.

| Feature | Deployment | DaemonSet |
| --- | --- | --- |
| Purpose | Run a desired number of replicas | Run one Pod per eligible node |
| Pod placement | Scheduler chooses nodes | Controller targets eligible nodes |
| Scaling | Set replica count | Follows eligible node count |
| New node joins | No automatic extra replica | Automatically creates a Pod |
| Typical use | APIs, frontend, workers | Logging, monitoring, networking |