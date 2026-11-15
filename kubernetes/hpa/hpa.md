# Horizontal Pod Autoscaler (HPA)
- ### HPA is a kubernetes resource that automatically increases or decreases the number of pod replicas based on obsereved resource utilization or other metrics.

## How does HPA work?
`HPA operates through a control loop`
```
    1. Metrics Server
       collects cpu and memory usage from running pods.
            ↡
    2. HPA controller
       compare actual metrics with configured target value.
            ↡
    3. Scaling decision
       calculates the desired number of replicas.
            ↡
    4. Deployment
       updates the deployment's replicas count.
```
---
## HPA Scaling formula
```
Desired Replicas = [Current Replicas * (current metrics/target metrics)]
```
```
   Example:

   Suppose:
      - current replicas = 2
      - current average cpu utilization = 80%
      - target cpu utilization = 40%

   [2 * (80/40)] = 4

   Kubernets recommends increasing the replicas from 2 to 4.
```
