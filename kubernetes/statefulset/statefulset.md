# Kubernetes Statefulset
### A StatefulSet manages Pods that need to maintain their identity even when they are deleted, restarted, or rescheduled.

## Typical applications included
- PosgreSQL Database
- MongoDB Replica Set
- Apache Kafka
- Redis Cluster
- Elasticsearch Cluster
- Zookeeper

## A quick comperison between Deployment vs StatefulSet
|Feature	 |   Deployment	  | StatefulSet |
|   ---      |     ---        |     ---     |
|Pod identity|	Not stable	  |   Stable    |
|Pod names	 |Generated	      |Predictable  |
|Startup order|	No guaranteed ordering|	Ordered by default|
|Storage	 | Can use PVCs	  |Supports per-Pod PVCs|
|Pod replacement|	New identity|	Same ordinal identity|
|Typical use |APIs, frontend  |	Databases, clusters   |


## Important StatefulSet Concepts

- ### Stable network identity
    A StatefulSet create Pods with stable, and predictable name.

    Example:
    ```bash
    postgres-0
    postgres-1
    postgres-2
    ```

- ### Stable storage
    Each StatefulSet replica can receive its own PersistentVolumeClaim through a volumeClaimTemplates configuration.

    For example
    ```bash
    postgres-0 → data-postgres-0
    postgres-1 → data-postgres-1
    postgres-2 → data-postgres-2
    ```

- ### Ordered Deployment
    By default, Statefulsets use ordered pod management
    
    For three replicas, the startup order is:
    ```bash
    postgres-0
        ↓
    postgres-1
        ↓
    postgres-2
    ```

- ### Ordered Termination
    Using the default Pod management policy `OrderedReady`, Pods are terminated in reverse order.
    ```bash
    postgres-2
        ↓
    postgres-1
        ↓
    postgres-0
    ```

- ### Headless Service
    StatefulSet commonly uses a Headless Service, that provide stable network identities.

    A regular service provide virtual IP that distributes traffic to matching Pods.

    A Headless service does not allocate a ClusterIP, instead DNS can resolve directly to the individual Pods.

    Example of a Headless Service
    ```bash
    apiVersion: v1
    kind: Service
    metadata:
        name: postgres-headless-service
        namespace: default
    spec:
        ClusterIP: none
        selector:
            app: postgres
        ports:
         - port: 5432
           name: postgres
    ```
    The DNS names can look like
    ```bash
    postgres-0.postgres-headless.default.svc.cluster.local

    postgres-1.postgres-headless.default.svc.cluster.local

    postgres-2.postgres-headless.default.svc.cluster.local
    ```