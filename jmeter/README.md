# Pruebas de carga con JMeter

El plan `covagro-load-test.jmx` autentica con JWT y ejecuta lecturas sobre productos, pedidos y stock bajo.

Ejemplo para Docker Compose:

```powershell
.\scripts\run_jmeter.ps1 -HostName localhost -Port 8000 -Scenario docker-compose -Nodes 1 -Replicas 1 -Users 25
```

Ejemplo para Kubernetes:

```powershell
.\scripts\run_jmeter.ps1 -HostName localhost -Port 30081 -Scenario k8s-2-nodes -Nodes 2 -Replicas 3 -Users 50
```

En Linux tambien puedes ejecutar directamente:

```bash
jmeter -n -t jmeter/covagro-load-test.jmx -l results/docker-compose-u25/samples.jtl -e -o results/docker-compose-u25/dashboard -JHOST=localhost -JPORT=8000 -JUSERS=25 -JRAMP_UP=30 -JDURATION=120
```

Si necesitas una prueba minima sin endpoints autenticados de lectura, usa el respaldo:

```bash
jmeter -n -t jmeter/simple-load-test.jmx -l results/simple-u25/samples.jtl -e -o results/simple-u25/dashboard -JHOST=localhost -JPORT=8000 -JUSERS=25 -JRAMP_UP=30 -JDURATION=120
```

Completa `jmeter/results_template.csv` con las metricas del dashboard HTML de JMeter:

- Average: tiempo medio de respuesta.
- Throughput: peticiones por segundo.
- Error %: porcentaje de errores.
- 95th pct: percentil 95.
