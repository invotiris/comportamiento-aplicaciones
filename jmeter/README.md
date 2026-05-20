# Pruebas de carga con JMeter

El plan `covagro-load-test.jmx` autentica con JWT y ejecuta lecturas sobre productos, pedidos y stock bajo.

Ejemplo para Docker Compose:

```powershell
.\scripts\run_jmeter.ps1 -BaseUrl http://localhost:8000 -Scenario docker-compose -Nodes 1 -Replicas 1 -Users 25
```

Ejemplo para Kubernetes:

```powershell
.\scripts\run_jmeter.ps1 -BaseUrl http://localhost:30081 -Scenario k8s-2-nodes -Nodes 2 -Replicas 3 -Users 50
```

Completa `jmeter/results_template.csv` con las metricas del dashboard HTML de JMeter:

- Average: tiempo medio de respuesta.
- Throughput: peticiones por segundo.
- Error %: porcentaje de errores.
- 95th pct: percentil 95.
