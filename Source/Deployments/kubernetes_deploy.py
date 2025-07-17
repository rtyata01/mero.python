"""
# Mock Kubernetes deployments and monitoring.

kubectl apply -f k8s/deployment/monitoring/prometheus-operator.yaml
kubectl apply -f k8s/deployment/monitoring/prometheus.yaml
kubectl apply -f k8s/deployment/monitoring/grafana.yaml
kubectl apply -f k8s/deployment/monitoring/servicemonitor.yaml

# Then your existing services:
kubectl apply -f k8s/deployment/search_service.yaml
kubectl apply -f k8s/deployment/worker_service.yaml
kubectl apply -f k8s/deployment/kafka_cluster.yaml

"""