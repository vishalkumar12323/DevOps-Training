# Kubernetes DNS
### Kubernetes DNS is a built-in cluster service that acts as the backbone for internal service discovery.

## The Core mechanism
- ### The DNS Engine: `CoreDNS (running as a deployment inside the kube-system namespace) to watch the Kubernetes API server.`
- Automatic Records: `Every time a resource changes, CoreDNS dynamically updates its records`
- ### Pod Configuration: `The kubelet automatically injects the CoreDNS service IP into every pod's /etc/resolv.conf file, forcing internal network traffic to resolve locally first`

## Hands On:
### Discover a service using DNS

### Check CoreDNS
```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
```
### Inspect the DNS service
```bash
kubectl get service -n kube-system kube-dns
```

### Create a DNS testing pod
```bash
kubectl run dns-test --image=busybox:1.36 --restart=Never -n service-discovery-demo --command -- sleep 3600
```

### Resolve the service name
```bash
kubectl exec -n service-discovery-demo dns-test -- nslookup web-service
```
