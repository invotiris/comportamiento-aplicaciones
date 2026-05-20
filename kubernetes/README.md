# Despliegue en Kubernetes

Los manifiestos usan `kind`, aunque tambien funcionan con Minikube ajustando la carga de imagenes.

## Crear clusters

Un nodo:

```bash
kind create cluster --name covagro-1n --config kubernetes/kind/one-node.yaml
```

Dos nodos:

```bash
kind create cluster --name covagro-2n --config kubernetes/kind/two-nodes.yaml
```

Tres nodos:

```bash
kind create cluster --name covagro-3n --config kubernetes/kind/three-nodes.yaml
```

## Construir y cargar imagenes

```bash
docker build -t covagro-backend:local app/Backend
docker build -t covagro-frontend:local app/Frontend
kind load docker-image covagro-backend:local --name covagro-1n
kind load docker-image covagro-frontend:local --name covagro-1n
```

Cambia `covagro-1n` por `covagro-2n` o `covagro-3n` segun el escenario.

## Desplegar

```bash
kubectl apply -k kubernetes/base
kubectl -n covagro rollout status statefulset/postgres
kubectl -n covagro rollout status deployment/backend
kubectl -n covagro rollout status deployment/frontend
```

Servicios:

- Frontend: http://localhost:30080
- API: http://localhost:30081/api/

## Variar replicas

```bash
kubectl -n covagro scale deployment/backend --replicas=1
kubectl -n covagro scale deployment/backend --replicas=2
kubectl -n covagro scale deployment/backend --replicas=3
kubectl -n covagro get pods -o wide
```

Registra los resultados por combinacion: numero de nodos, replicas y carga JMeter.
